from __future__ import annotations

import argparse
import hashlib
import json
import random
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, NamedTuple, Sequence


REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SUITE_PATH = REPO_ROOT / "tests" / "fixtures" / "architecture_capability_evals.json"
VALID_CONDITIONS = ("A", "B", "C")


class PromptRequest(NamedTuple):
    suite: dict[str, Any]
    scenario: dict[str, Any]
    condition: str
    candidate_id: str


class PrepareOptions(NamedTuple):
    suite_path: Path
    candidate_id: str
    output_dir: Path
    run_label: str
    provenance: "RunProvenance | None" = None


class BlindOptions(NamedTuple):
    suite_path: Path
    bundle_dir: Path
    output_dir: Path
    seed: int
    scenario_ids: tuple[str, ...] = ()


class RunProvenance(NamedTuple):
    """The execution envelope declared before an A/B/C bundle is created."""

    model: str
    reasoning_effort: str
    tool_access: str
    execution_environment: str
    baseline_description: str
    run_family: str


class ExecutionRecord(NamedTuple):
    """Evidence about one completed model response, recorded after it is saved."""

    thread_id: str
    started_at: str
    completed_at: str
    tools_used: tuple[str, ...]
    input_tokens: int | None
    output_tokens: int | None
    cost_usd: float | None
    measurement_note: str


def load_suite(path: Path = DEFAULT_SUITE_PATH) -> dict[str, Any]:
    try:
        suite = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Evaluation suite does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Evaluation suite is invalid JSON: {path}: {exc}") from exc

    required = {"schema_version", "suite_id", "kernel", "candidates", "scenarios"}
    missing = required - set(suite)
    if missing:
        raise ValueError(f"Evaluation suite is missing fields: {sorted(missing)}")
    return suite


def find_candidate(suite: dict[str, Any], candidate_id: str) -> dict[str, Any]:
    for candidate in suite["candidates"]:
        if candidate["id"] == candidate_id:
            return candidate
    raise ValueError(f"Unknown architecture candidate: {candidate_id}")


def select_scenarios(suite: dict[str, Any], candidate_id: str) -> list[dict[str, Any]]:
    find_candidate(suite, candidate_id)
    scenarios = [
        scenario
        for scenario in suite["scenarios"]
        if candidate_id in scenario["candidate_ids_to_test"]
    ]
    if not scenarios:
        raise ValueError(f"No evaluation scenarios cover candidate: {candidate_id}")
    return scenarios


def format_instructions(title: str, instructions: Sequence[str]) -> str:
    lines = [f"## {title}"]
    lines.extend(f"- {instruction}" for instruction in instructions)
    return "\n".join(lines)


def build_condition_prompt(request: PromptRequest) -> str:
    suite, scenario, condition, candidate_id = request
    if condition not in VALID_CONDITIONS:
        raise ValueError(f"Unknown evaluation condition: {condition}")
    if candidate_id not in scenario["candidate_ids_to_test"]:
        raise ValueError(
            f"Scenario {scenario['id']} is not configured for candidate {candidate_id}"
        )

    if condition == "A":
        return scenario["task_prompt"].rstrip() + "\n"

    sections = ["# Operating guidance"]

    kernel = suite["kernel"]
    sections.append(format_instructions(kernel["title"], kernel["instructions"]))

    if condition == "C":
        candidate = find_candidate(suite, candidate_id)
        sections.append(
            format_instructions(
                f"Candidate capability: {candidate['title']}", candidate["instructions"]
            )
        )

    sections.extend(("## Project request", scenario["task_prompt"]))
    return "\n\n".join(sections).rstrip() + "\n"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def write_text(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8", newline="\n")


def ensure_new_directory(path: Path, label: str) -> None:
    if path.exists():
        raise ValueError(f"{label} already exists; choose a new path: {path}")


def require_nonempty_text(value: object, label: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{label} must be non-empty text")
    return value.strip()


def parse_timestamp(value: str, label: str) -> datetime:
    require_nonempty_text(value, label)
    try:
        parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise ValueError(f"{label} must be an ISO-8601 timestamp") from exc
    if parsed.tzinfo is None:
        raise ValueError(f"{label} must include a timezone")
    return parsed


def validate_provenance(provenance: RunProvenance | None) -> RunProvenance:
    if provenance is None:
        raise ValueError("Run provenance is required before preparing a bundle")
    for field, value in provenance._asdict().items():
        require_nonempty_text(value, f"provenance.{field}")
    return provenance


def validate_execution_record(record: ExecutionRecord) -> ExecutionRecord:
    require_nonempty_text(record.thread_id, "execution thread_id")
    started_at = parse_timestamp(record.started_at, "execution started_at")
    completed_at = parse_timestamp(record.completed_at, "execution completed_at")
    if completed_at < started_at:
        raise ValueError("execution completed_at must not precede started_at")
    if not isinstance(record.tools_used, tuple) or any(
        not isinstance(tool, str) or not tool.strip() for tool in record.tools_used
    ):
        raise ValueError("execution tools_used must be a tuple of non-empty tool names")
    for label, value in (
        ("execution input_tokens", record.input_tokens),
        ("execution output_tokens", record.output_tokens),
    ):
        if value is not None and (not isinstance(value, int) or value < 0):
            raise ValueError(f"{label} must be a non-negative integer or null")
    if record.cost_usd is not None and (
        not isinstance(record.cost_usd, (int, float)) or record.cost_usd < 0
    ):
        raise ValueError("execution cost_usd must be a non-negative number or null")
    if (
        record.input_tokens is None
        or record.output_tokens is None
        or record.cost_usd is None
    ):
        require_nonempty_text(record.measurement_note, "execution measurement_note")
    return record


def prepare_bundle(options: PrepareOptions) -> dict[str, Any]:
    suite = load_suite(options.suite_path)
    candidate = find_candidate(suite, options.candidate_id)
    scenarios = select_scenarios(suite, options.candidate_id)
    provenance = validate_provenance(options.provenance)
    ensure_new_directory(options.output_dir, "Output directory")
    if not options.run_label.strip():
        raise ValueError("Run label must not be empty")

    runs: list[dict[str, Any]] = []
    for scenario in scenarios:
        for condition in VALID_CONDITIONS:
            prompt = build_condition_prompt(
                PromptRequest(suite, scenario, condition, options.candidate_id)
            )
            prompt_path = Path("prompts") / scenario["id"] / f"{condition}.md"
            response_path = Path("responses") / scenario["id"] / f"{condition}.md"
            evidence_path = Path("evidence") / scenario["id"] / f"{condition}.json"
            write_text(options.output_dir / prompt_path, prompt)
            write_text(options.output_dir / response_path, "")
            runs.append(
                {
                    "scenario_id": scenario["id"],
                    "condition": condition,
                    "prompt_path": prompt_path.as_posix(),
                    "response_path": response_path.as_posix(),
                    "evidence_path": evidence_path.as_posix(),
                    "prompt_sha256": sha256_text(prompt),
                }
            )

    manifest = {
        "schema_version": "1.1",
        "evidence_schema_version": "1.0",
        "suite_id": suite["suite_id"],
        "suite_schema_version": suite["schema_version"],
        "candidate_id": candidate["id"],
        "candidate_title": candidate["title"],
        "run_label": options.run_label.strip(),
        "provenance": provenance._asdict(),
        "created_at": datetime.now(timezone.utc).isoformat(),
        "runs": runs,
    }
    write_text(
        options.output_dir / "manifest.json",
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
    )
    write_text(options.output_dir / "README.md", build_bundle_instructions(manifest))
    return manifest


def build_bundle_instructions(manifest: dict[str, Any]) -> str:
    return f"""# Architecture A/B/C Pilot Bundle

**Candidate:** {manifest['candidate_title']}  
**Run label:** {manifest['run_label']}

For each scenario, open a fresh AI task for each prompt in `prompts/<scenario>/`.

1. Do not show one condition's answer to another condition.
2. Keep the model, effort setting, tools, and project evidence as comparable as possible.
3. Paste the model's answer into the matching empty file under `responses/<scenario>/`.
4. Immediately record the response's actual execution evidence with the `record` command. Do not estimate unavailable telemetry; explain the gap in `--measurement-note`.
5. Do not rename the condition files.
6. After every response and evidence record is collected, run the `blind` command to prepare reviewer-safe files.

Condition names exist only for experiment management. Do not include them in model responses.

Declared execution envelope: model `{manifest['provenance']['model']}`, effort `{manifest['provenance']['reasoning_effort']}`, run family `{manifest['provenance']['run_family']}`.
"""


def load_manifest(bundle_dir: Path) -> dict[str, Any]:
    path = bundle_dir / "manifest.json"
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"Bundle manifest does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"Bundle manifest is invalid JSON: {path}: {exc}") from exc


def find_run(manifest: dict[str, Any], scenario_id: str, condition: str) -> dict[str, Any]:
    for run in manifest.get("runs", []):
        if run.get("scenario_id") == scenario_id and run.get("condition") == condition:
            return run
    raise ValueError(f"Bundle does not contain run: {scenario_id}/{condition}")


def record_execution(
    bundle_dir: Path,
    scenario_id: str,
    condition: str,
    record: ExecutionRecord,
) -> dict[str, Any]:
    """Persist non-secret execution facts once a matching response is present."""

    manifest = load_manifest(bundle_dir)
    if "provenance" not in manifest:
        raise ValueError("Bundle manifest is missing run provenance")
    provenance = validate_provenance(RunProvenance(**manifest["provenance"]))
    run = find_run(manifest, scenario_id, condition)
    response_path = bundle_dir / run["response_path"]
    if not response_path.is_file() or not response_path.read_text(encoding="utf-8").strip():
        raise ValueError(f"Cannot record execution before a response exists: {run['response_path']}")
    validated = validate_execution_record(record)
    evidence_path = bundle_dir / run["evidence_path"]
    if evidence_path.exists():
        raise ValueError(f"Execution evidence already exists; do not overwrite it: {evidence_path}")

    evidence = {
        "schema_version": manifest["evidence_schema_version"],
        "scenario_id": scenario_id,
        "condition": condition,
        **provenance._asdict(),
        **validated._asdict(),
        "tools_used": list(validated.tools_used),
        "response_sha256": sha256_text(response_path.read_text(encoding="utf-8")),
    }
    write_text(evidence_path, json.dumps(evidence, indent=2, ensure_ascii=False) + "\n")
    return evidence


def load_and_validate_evidence(
    bundle_dir: Path, manifest: dict[str, Any], run: dict[str, Any], response: str
) -> dict[str, Any]:
    evidence_path = bundle_dir / run["evidence_path"]
    if not evidence_path.is_file():
        raise ValueError(f"Missing execution evidence: {run['evidence_path']}")
    try:
        evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Execution evidence is invalid JSON: {evidence_path}: {exc}") from exc

    for field in ("scenario_id", "condition", "response_sha256", "thread_id"):
        require_nonempty_text(evidence.get(field), f"execution evidence {field}")
    if evidence["scenario_id"] != run["scenario_id"] or evidence["condition"] != run["condition"]:
        raise ValueError(f"Execution evidence does not match run: {run['scenario_id']}/{run['condition']}")
    if evidence["response_sha256"] != sha256_text(response):
        raise ValueError(f"Execution evidence response hash does not match: {run['response_path']}")
    for field, value in manifest["provenance"].items():
        if evidence.get(field) != value:
            raise ValueError(f"Execution evidence provenance mismatch for {field}")
    validate_execution_record(
        ExecutionRecord(
            thread_id=evidence["thread_id"],
            started_at=evidence.get("started_at", ""),
            completed_at=evidence.get("completed_at", ""),
            tools_used=tuple(evidence.get("tools_used", [])),
            input_tokens=evidence.get("input_tokens"),
            output_tokens=evidence.get("output_tokens"),
            cost_usd=evidence.get("cost_usd"),
            measurement_note=evidence.get("measurement_note", ""),
        )
    )
    return evidence


def collect_responses(
    bundle_dir: Path,
    manifest: dict[str, Any],
    scenario_ids: Sequence[str] = (),
) -> list[dict[str, Any]]:
    requested = set(scenario_ids)
    available = {run["scenario_id"] for run in manifest["runs"]}
    unknown = requested - available
    if unknown:
        raise ValueError(f"Bundle does not contain scenarios: {sorted(unknown)}")

    collected: list[dict[str, Any]] = []
    for run in manifest["runs"]:
        if requested and run["scenario_id"] not in requested:
            continue
        response_path = bundle_dir / run["response_path"]
        if not response_path.is_file() or not response_path.read_text(encoding="utf-8").strip():
            raise ValueError(f"Missing response: {run['response_path']}")
        response = response_path.read_text(encoding="utf-8")
        evidence = load_and_validate_evidence(bundle_dir, manifest, run, response)
        collected.append({**run, "response": response, "execution_evidence": evidence})
    return collected


def build_judge_guide(
    suite: dict[str, Any], manifest: dict[str, Any], scenario_ids: set[str]
) -> str:
    dimensions = "\n".join(
        f"- `{dimension['id']}` ({dimension['weight']}): {dimension['judge']}"
        for dimension in suite["dimensions"]
    )
    sections = [
        "# Blinded Architecture Evaluation Guide",
        "Candidate and condition identities are intentionally withheld. Score only the observable response behavior against this guide.",
        "Score observable behavior from 0 to 4. Do not reward length, architecture vocabulary, or agreement with a preferred technology.",
        "## Weighted dimensions",
        dimensions,
    ]

    scenarios = {scenario["id"]: scenario for scenario in suite["scenarios"]}
    for scenario_id in sorted(scenario_ids):
        scenario = scenarios[scenario_id]
        hidden_risks = "\n".join(f"- {item}" for item in scenario["hidden_evaluator_risks"])
        required = "\n".join(f"- {item}" for item in scenario["required_observations"])
        forbidden = "\n".join(f"- {item}" for item in scenario["forbidden_overreach"])
        focus = ", ".join(f"`{item}`" for item in scenario["scoring_focus"])
        sections.extend(
            (
                f"## Scenario: {scenario['title']}",
                f"### Project request\n\n{scenario['task_prompt']}",
                f"### Hidden risks\n\n{hidden_risks}",
                f"### Required observations\n\n{required}",
                f"### Prohibited overreach\n\n{forbidden}",
                f"### Primary scoring focus\n\n{focus}",
            )
        )
    return "\n\n".join(sections).rstrip() + "\n"


def build_scorecard_template(
    suite: dict[str, Any], manifest: dict[str, Any], answer_records: list[dict[str, Any]]
) -> dict[str, Any]:
    scenario_dimensions = {
        scenario["id"]: scenario["scoring_focus"] for scenario in suite["scenarios"]
    }
    return {
        "schema_version": "1.0",
        "suite_id": suite["suite_id"],
        "run_label": manifest["run_label"],
        "score_scale": {"minimum": 0, "maximum": 4},
        "dimension_ids_by_scenario": {
            record["scenario_id"]: scenario_dimensions[record["scenario_id"]]
            for record in answer_records
        },
        "judge": {
            "identity": "",
            "model": "",
            "reviewed_at": "",
            "independence_statement": "",
        },
        "responses": [
            {
                "scenario_id": record["scenario_id"],
                "blinded_label": record["blinded_label"],
                "scores": {
                    dimension_id: None
                    for dimension_id in scenario_dimensions[record["scenario_id"]]
                },
                "score_rationales": {
                    dimension_id: ""
                    for dimension_id in scenario_dimensions[record["scenario_id"]]
                },
                "critical_misses": [],
                "unnecessary_complexity": [],
                "overall_notes": "",
            }
            for record in answer_records
        ],
    }


def blind_bundle(options: BlindOptions) -> dict[str, Any]:
    suite = load_suite(options.suite_path)
    manifest = load_manifest(options.bundle_dir)
    if manifest["suite_id"] != suite["suite_id"]:
        raise ValueError("Bundle and evaluation suite IDs do not match")
    ensure_new_directory(options.output_dir, "Blind output directory")

    collected = collect_responses(options.bundle_dir, manifest, options.scenario_ids)
    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in collected:
        grouped.setdefault(item["scenario_id"], []).append(item)

    rng = random.Random(options.seed)
    answer_records: list[dict[str, Any]] = []
    for scenario_id in sorted(grouped):
        responses = grouped[scenario_id]
        rng.shuffle(responses)
        for index, item in enumerate(responses, start=1):
            blinded_label = f"response-{index:02d}"
            review_path = Path("review") / scenario_id / f"{blinded_label}.md"
            write_text(
                options.output_dir / review_path,
                f"# {blinded_label.replace('-', ' ').title()}\n\n{item['response'].strip()}\n",
            )
            answer_records.append(
                {
                    "scenario_id": scenario_id,
                    "blinded_label": blinded_label,
                    "condition": item["condition"],
                    "source_response_path": item["response_path"],
                    "review_path": review_path.as_posix(),
                    "response_sha256": sha256_text(item["response"]),
                }
            )

    answer_key = {
        "schema_version": "1.0",
        "suite_id": suite["suite_id"],
        "candidate_id": manifest["candidate_id"],
        "run_label": manifest["run_label"],
        "seed": options.seed,
        "scoring_focus_by_scenario": {
            scenario_id: next(
                scenario["scoring_focus"]
                for scenario in suite["scenarios"]
                if scenario["id"] == scenario_id
            )
            for scenario_id in grouped
        },
        "responses": answer_records,
    }
    write_text(
        options.output_dir / "answer-key.json",
        json.dumps(answer_key, indent=2, ensure_ascii=False) + "\n",
    )
    write_text(
        options.output_dir / "judge-guide.md",
        build_judge_guide(suite, manifest, set(grouped)),
    )
    write_text(
        options.output_dir / "scorecard-template.json",
        json.dumps(
            build_scorecard_template(suite, manifest, answer_records),
            indent=2,
            ensure_ascii=False,
        )
        + "\n",
    )
    return answer_key


def load_json_document(path: Path, label: str) -> dict[str, Any]:
    try:
        document = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ValueError(f"{label} does not exist: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} is invalid JSON: {path}: {exc}") from exc
    if not isinstance(document, dict):
        raise ValueError(f"{label} must be a JSON object: {path}")
    return document


def validate_completed_scorecard(blind_dir: Path, scorecard_path: Path) -> dict[str, Any]:
    """Reject partial, unaccountable, or mismatched scored reviews before decoding."""

    answer_key = load_json_document(blind_dir / "answer-key.json", "Answer key")
    scorecard = load_json_document(scorecard_path, "Scorecard")
    if scorecard.get("suite_id") != answer_key.get("suite_id"):
        raise ValueError("Scorecard and answer key suite IDs do not match")
    judge = scorecard.get("judge")
    if not isinstance(judge, dict):
        raise ValueError("Scorecard judge information is required")
    for field in ("identity", "model", "independence_statement"):
        require_nonempty_text(judge.get(field), f"Scorecard judge {field}")
    parse_timestamp(judge.get("reviewed_at", ""), "Scorecard judge reviewed_at")

    expected = {
        (record["scenario_id"], record["blinded_label"])
        for record in answer_key.get("responses", [])
    }
    responses = scorecard.get("responses")
    if not isinstance(responses, list):
        raise ValueError("Scorecard responses must be a list")
    actual = {(item.get("scenario_id"), item.get("blinded_label")) for item in responses}
    if len(actual) != len(responses):
        raise ValueError("Scorecard contains duplicate scenario/response entries")
    if actual != expected:
        raise ValueError("Scorecard response set does not match blinded answer set")

    dimensions_by_scenario = scorecard.get("dimension_ids_by_scenario")
    if not isinstance(dimensions_by_scenario, dict):
        raise ValueError("Scorecard dimension_ids_by_scenario are required")
    expected_dimensions_by_scenario = answer_key.get("scoring_focus_by_scenario")
    if dimensions_by_scenario != expected_dimensions_by_scenario:
        raise ValueError("Scorecard dimensions do not match the blinded scenario scoring focus")
    for item in responses:
        scores = item.get("scores")
        rationales = item.get("score_rationales")
        if not isinstance(scores, dict) or not isinstance(rationales, dict):
            raise ValueError("Every scorecard response requires scores and score_rationales")
        scenario_id = item.get("scenario_id")
        dimensions = set(dimensions_by_scenario.get(scenario_id, []))
        if not dimensions:
            raise ValueError(f"Scorecard dimensions are required for scenario: {scenario_id}")
        if set(scores) != dimensions or set(rationales) != dimensions:
            raise ValueError("Every response must score and explain its scenario dimensions")
        for dimension, score in scores.items():
            if not isinstance(score, int) or isinstance(score, bool) or score < 0 or score > 4:
                raise ValueError(f"Scorecard score {dimension} must be an integer from 0 to 4")
            require_nonempty_text(rationales.get(dimension), f"Scorecard rationale {dimension}")
        require_nonempty_text(item.get("overall_notes"), "Scorecard overall_notes")
    return scorecard


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Prepare and blind Anti-Gravity architecture A/B/C evaluation bundles."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    prepare = subparsers.add_parser("prepare", help="Generate isolated A/B/C prompts")
    prepare.add_argument("--candidate", required=True)
    prepare.add_argument("--output", type=Path, required=True)
    prepare.add_argument("--run-label", required=True)
    prepare.add_argument("--model", required=True)
    prepare.add_argument("--effort", required=True)
    prepare.add_argument("--tool-access", required=True)
    prepare.add_argument("--environment", required=True)
    prepare.add_argument("--baseline-description", required=True)
    prepare.add_argument("--run-family", required=True)
    prepare.add_argument("--suite", type=Path, default=DEFAULT_SUITE_PATH)

    blind = subparsers.add_parser("blind", help="Randomize completed responses for review")
    blind.add_argument("--bundle", type=Path, required=True)
    blind.add_argument("--output", type=Path, required=True)
    blind.add_argument("--seed", type=int, default=1)
    blind.add_argument(
        "--scenario",
        action="append",
        dest="scenario_ids",
        default=[],
        help="Blind only a completed scenario (repeatable)",
    )
    blind.add_argument("--suite", type=Path, default=DEFAULT_SUITE_PATH)

    record = subparsers.add_parser("record", help="Record execution evidence for one saved response")
    record.add_argument("--bundle", type=Path, required=True)
    record.add_argument("--scenario", required=True)
    record.add_argument("--condition", choices=VALID_CONDITIONS, required=True)
    record.add_argument("--thread-id", required=True)
    record.add_argument("--started-at", required=True)
    record.add_argument("--completed-at", required=True)
    record.add_argument("--tool-used", action="append", default=[])
    record.add_argument("--input-tokens", type=int)
    record.add_argument("--output-tokens", type=int)
    record.add_argument("--cost-usd", type=float)
    record.add_argument("--measurement-note", required=True)

    validate_scorecard = subparsers.add_parser(
        "validate-scorecard", help="Validate a completed blinded scorecard before decoding"
    )
    validate_scorecard.add_argument("--blind", type=Path, required=True)
    validate_scorecard.add_argument("--scorecard", type=Path, required=True)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        if args.command == "prepare":
            manifest = prepare_bundle(
                PrepareOptions(
                    args.suite,
                    args.candidate,
                    args.output,
                    args.run_label,
                    RunProvenance(
                        args.model,
                        args.effort,
                        args.tool_access,
                        args.environment,
                        args.baseline_description,
                        args.run_family,
                    ),
                )
            )
            print(f"Prepared {len(manifest['runs'])} prompts in {args.output}")
        elif args.command == "blind":
            answer_key = blind_bundle(
                BlindOptions(
                    args.suite,
                    args.bundle,
                    args.output,
                    args.seed,
                    tuple(args.scenario_ids),
                )
            )
            print(
                f"Prepared {len(answer_key['responses'])} blinded responses in {args.output}"
            )
        elif args.command == "record":
            evidence = record_execution(
                args.bundle,
                args.scenario,
                args.condition,
                ExecutionRecord(
                    args.thread_id,
                    args.started_at,
                    args.completed_at,
                    tuple(args.tool_used),
                    args.input_tokens,
                    args.output_tokens,
                    args.cost_usd,
                    args.measurement_note,
                ),
            )
            print(
                f"Recorded execution evidence for {evidence['scenario_id']}/{evidence['condition']}"
            )
        else:
            validate_completed_scorecard(args.blind, args.scorecard)
            print(f"Validated completed scorecard: {args.scorecard}")
    except ValueError as exc:
        print(f"error: {exc}")
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
