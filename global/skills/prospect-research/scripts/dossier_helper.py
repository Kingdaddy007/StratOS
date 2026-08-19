#!/usr/bin/env python3
"""Create, validate, and score prospect-research dossier JSON files.

This helper is deliberately local and dependency-free. It never browses,
contacts prospects, uploads data, or sends messages.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


SCORE_LIMITS = {
    "visual_asset_quality": 25,
    "website_gap": 20,
    "business_maturity": 10,
    "active_online_presence": 15,
    "contact_accessibility": 20,
    "personalization_potential": 10,
}
ALLOWED_RECOMMENDED_ACTIONS = (
    "Prepare concept for review",
    "Verify manually",
    "Prepare light outreach draft for review",
    "Add to a local nurture proposal",
    "Do not target",
)
REQUIRED_FIELDS = (
    "studio_name",
    "country",
    "city",
    "segment",
    "website_url",
    "instagram_url",
    "founder_name",
    "contact_method",
    "website_status",
    "inspection_date",
    "evidence",
    "scores",
    "main_gap",
    "outreach_hook",
    "recommended_action",
)


def load_dossier(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"dossier not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"invalid JSON at {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise ValueError("dossier root must be a JSON object")
    return value


def validate_dossier(dossier: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    for field in REQUIRED_FIELDS:
        if field not in dossier:
            errors.append(f"missing field: {field}")
    evidence = dossier.get("evidence")
    if not isinstance(evidence, dict):
        errors.append("evidence must be an object")
    else:
        for source in ("instagram", "website", "completed_projects"):
            if not str(evidence.get(source, "")).strip():
                errors.append(f"missing evidence: {source}")
    scores = dossier.get("scores")
    if not isinstance(scores, dict):
        errors.append("scores must be an object")
    else:
        for name, maximum in SCORE_LIMITS.items():
            value = scores.get(name)
            if not isinstance(value, int) or isinstance(value, bool):
                errors.append(f"score {name} must be an integer")
            elif not 0 <= value <= maximum:
                errors.append(f"score {name} must be between 0 and {maximum}")
    team_size = dossier.get("team_size")
    if team_size is not None and (not isinstance(team_size, int) or team_size < 0):
        errors.append("team_size must be a non-negative integer or null")
    action = dossier.get("recommended_action")
    if action not in ALLOWED_RECOMMENDED_ACTIONS:
        errors.append(
            "recommended_action must be one of: "
            + ", ".join(ALLOWED_RECOMMENDED_ACTIONS)
        )
    if action == "Prepare concept for review":
        total = score_dossier(dossier)["total"]
        if total < 80:
            errors.append("concept review requires an Elite score of 80 or higher")
    return errors


def score_dossier(dossier: dict[str, Any]) -> dict[str, Any]:
    scores = dossier.get("scores", {})
    total = sum(int(scores.get(name, 0)) for name in SCORE_LIMITS)
    tier = "Elite" if total >= 80 else "Growth" if total >= 50 else "Low"
    return {"total": total, "tier": tier, "scores": scores}


def new_dossier() -> dict[str, Any]:
    return {
        "studio_name": "",
        "country": "",
        "city": "",
        "segment": "luxury residential interior design",
        "website_url": "",
        "instagram_url": "",
        "founder_name": "",
        "contact_method": "",
        "website_status": "",
        "inspection_date": "",
        "team_size": None,
        "dedicated_marketing_or_pr": None,
        "evidence": {"instagram": "", "website": "", "completed_projects": "", "premium_positioning": ""},
        "scores": {name: 0 for name in SCORE_LIMITS},
        "main_gap": "",
        "hero_concept_angle": "",
        "outreach_hook": "",
        "recommended_action": "Verify manually",
        "notes": "",
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    new_parser = subparsers.add_parser("new", help="write a blank dossier template")
    new_parser.add_argument("output", type=Path)
    validate_parser = subparsers.add_parser("validate", help="validate a dossier")
    validate_parser.add_argument("dossier", type=Path)
    score_parser = subparsers.add_parser("score", help="print validated dossier score")
    score_parser.add_argument("dossier", type=Path)
    args = parser.parse_args()
    try:
        if args.command == "new":
            if args.output.exists():
                raise ValueError(f"refusing to overwrite existing file: {args.output}")
            args.output.parent.mkdir(parents=True, exist_ok=True)
            args.output.write_text(json.dumps(new_dossier(), indent=2) + "\n", encoding="utf-8")
            print(f"created {args.output}")
            return 0
        dossier = load_dossier(args.dossier)
        errors = validate_dossier(dossier)
        if errors:
            for error in errors:
                print(f"error: {error}")
            return 1
        result = score_dossier(dossier)
        if args.command == "validate":
            print("valid dossier")
        else:
            print(json.dumps(result, indent=2))
        return 0
    except ValueError as exc:
        print(f"error: {exc}")
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
