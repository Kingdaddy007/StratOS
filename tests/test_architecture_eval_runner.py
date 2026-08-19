from __future__ import annotations

import importlib.util
import json
import tempfile
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
RUNNER_PATH = REPO_ROOT / "tests" / "architecture_eval_runner.py"
FIXTURE_PATH = REPO_ROOT / "tests" / "fixtures" / "architecture_capability_evals.json"


def load_runner():
    spec = importlib.util.spec_from_file_location("architecture_eval_runner", RUNNER_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load architecture evaluation runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ArchitectureEvaluationRunnerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = load_runner()
        self.suite = self.runner.load_suite(FIXTURE_PATH)
        self.candidate_id = "quality-attribute-scenarios"
        self.provenance = self.runner.RunProvenance(
            model="gpt-5.6-luna",
            reasoning_effort="max",
            tool_access="read-only filesystem; no network",
            execution_environment="fresh projectless Codex task",
            baseline_description="Current installed host instructions and skills remain active.",
            run_family="luna-max-replication-1",
        )
        self.scenario = next(
            scenario
            for scenario in self.suite["scenarios"]
            if scenario["id"] == "booking-greenfield"
        )

    def prepare_bundle(self, output: Path) -> dict:
        return self.runner.prepare_bundle(
            self.runner.PrepareOptions(
                suite_path=FIXTURE_PATH,
                candidate_id=self.candidate_id,
                output_dir=output,
                run_label="unit-test",
                provenance=self.provenance,
            )
        )

    def record_response(self, bundle: Path, run: dict, index: int) -> None:
        (bundle / run["response_path"]).write_text(
            f"Independent response number {index}.\n", encoding="utf-8"
        )
        self.runner.record_execution(
            bundle,
            run["scenario_id"],
            run["condition"],
            self.runner.ExecutionRecord(
                thread_id=f"thread-{index}",
                started_at="2026-08-18T12:00:00+00:00",
                completed_at="2026-08-18T12:01:00+00:00",
                tools_used=("filesystem.read",),
                input_tokens=None,
                output_tokens=None,
                cost_usd=None,
                measurement_note="The host did not expose token or cost telemetry.",
            ),
        )

    def test_conditions_isolate_kernel_and_candidate_instructions(self) -> None:
        prompt_a = self.runner.build_condition_prompt(
            self.runner.PromptRequest(self.suite, self.scenario, "A", self.candidate_id)
        )
        prompt_b = self.runner.build_condition_prompt(
            self.runner.PromptRequest(self.suite, self.scenario, "B", self.candidate_id)
        )
        prompt_c = self.runner.build_condition_prompt(
            self.runner.PromptRequest(self.suite, self.scenario, "C", self.candidate_id)
        )

        candidate_title = next(
            candidate["title"]
            for candidate in self.suite["candidates"]
            if candidate["id"] == self.candidate_id
        )

        self.assertNotIn("Anti-Gravity architecture kernel", prompt_a)
        self.assertNotIn(candidate_title, prompt_a)
        self.assertEqual(self.scenario["task_prompt"] + "\n", prompt_a)
        self.assertIn("Anti-Gravity architecture kernel", prompt_b)
        self.assertNotIn(candidate_title, prompt_b)
        self.assertIn("Anti-Gravity architecture kernel", prompt_c)
        self.assertIn(candidate_title, prompt_c)
        self.assertEqual(1, prompt_a.count(self.scenario["task_prompt"]))
        self.assertEqual(1, prompt_b.count(self.scenario["task_prompt"]))
        self.assertEqual(1, prompt_c.count(self.scenario["task_prompt"]))

    def test_prepare_builds_three_scenarios_and_nine_isolated_prompts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "pilot"
            manifest = self.prepare_bundle(output)

            self.assertEqual(9, len(manifest["runs"]))
            self.assertEqual(
                {
                    "booking-greenfield",
                    "microservices-fashion-trap",
                    "landing-page-restyle-control",
                },
                {run["scenario_id"] for run in manifest["runs"]},
            )
            self.assertEqual({"A", "B", "C"}, {run["condition"] for run in manifest["runs"]})

            for run in manifest["runs"]:
                self.assertTrue((output / run["prompt_path"]).is_file())
                self.assertTrue((output / run["response_path"]).is_file())
                self.assertTrue(run["prompt_sha256"])
                self.assertTrue(run["evidence_path"])

            self.assertEqual(self.provenance._asdict(), manifest["provenance"])

            saved_manifest = json.loads((output / "manifest.json").read_text(encoding="utf-8"))
            self.assertEqual(manifest, saved_manifest)

    def test_prepare_rejects_missing_provenance(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaisesRegex(ValueError, "provenance"):
                self.runner.prepare_bundle(
                    self.runner.PrepareOptions(
                        suite_path=FIXTURE_PATH,
                        candidate_id=self.candidate_id,
                        output_dir=Path(directory) / "pilot",
                        run_label="unit-test",
                    )
                )

    def test_blind_bundle_randomizes_labels_and_keeps_answer_key_separate(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "pilot"
            blind_output = root / "blind"
            manifest = self.prepare_bundle(bundle)

            for index, run in enumerate(manifest["runs"], start=1):
                self.record_response(bundle, run, index)

            answer_key = self.runner.blind_bundle(
                self.runner.BlindOptions(
                    suite_path=FIXTURE_PATH,
                    bundle_dir=bundle,
                    output_dir=blind_output,
                    seed=17,
                )
            )

            self.assertEqual(9, len(answer_key["responses"]))
            for scenario_id in {
                "booking-greenfield",
                "microservices-fashion-trap",
                "landing-page-restyle-control",
            }:
                conditions = {
                    item["condition"]
                    for item in answer_key["responses"]
                    if item["scenario_id"] == scenario_id
                }
                self.assertEqual({"A", "B", "C"}, conditions)

            review_files = list((blind_output / "review").rglob("response-*.md"))
            self.assertEqual(9, len(review_files))
            self.assertTrue((blind_output / "judge-guide.md").is_file())
            self.assertTrue((blind_output / "answer-key.json").is_file())
            self.assertNotIn(
                "Quality-attribute scenario and trade-off analysis",
                (blind_output / "judge-guide.md").read_text(encoding="utf-8"),
            )
            scorecard = json.loads(
                (blind_output / "scorecard-template.json").read_text(encoding="utf-8")
            )
            self.assertNotIn("candidate_id", scorecard)
            self.assertEqual(9, len(scorecard["responses"]))
            self.assertEqual(
                {"identity": "", "model": "", "reviewed_at": "", "independence_statement": ""},
                scorecard["judge"],
            )
            expected_dimensions = {
                scenario["id"]: set(scenario["scoring_focus"])
                for scenario in self.suite["scenarios"]
                if scenario["id"]
                in {
                    "booking-greenfield",
                    "microservices-fashion-trap",
                    "landing-page-restyle-control",
                }
            }
            self.assertEqual(expected_dimensions, {
                scenario_id: set(dimension_ids)
                for scenario_id, dimension_ids in scorecard["dimension_ids_by_scenario"].items()
            })
            for response in scorecard["responses"]:
                self.assertEqual(
                    expected_dimensions[response["scenario_id"]], set(response["scores"])
                )
                self.assertTrue(all(score is None for score in response["scores"].values()))

    def test_blinding_rejects_missing_responses(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "pilot"
            self.prepare_bundle(bundle)

            with self.assertRaisesRegex(ValueError, "Missing response"):
                self.runner.blind_bundle(
                    self.runner.BlindOptions(
                        suite_path=FIXTURE_PATH,
                        bundle_dir=bundle,
                        output_dir=root / "blind",
                        seed=17,
                    )
                )

    def test_blinding_rejects_missing_execution_evidence(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "pilot"
            manifest = self.prepare_bundle(bundle)

            for index, run in enumerate(manifest["runs"], start=1):
                (bundle / run["response_path"]).write_text(
                    f"Independent response number {index}.\n", encoding="utf-8"
                )

            with self.assertRaisesRegex(ValueError, "Missing execution evidence"):
                self.runner.blind_bundle(
                    self.runner.BlindOptions(
                        suite_path=FIXTURE_PATH,
                        bundle_dir=bundle,
                        output_dir=root / "blind",
                        seed=17,
                    )
                )

    def test_blind_bundle_can_review_one_completed_scenario(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "pilot"
            blind_output = root / "blind"
            manifest = self.prepare_bundle(bundle)

            for index, run in enumerate(manifest["runs"], start=1):
                if run["scenario_id"] == "booking-greenfield":
                    self.record_response(bundle, run, index)

            answer_key = self.runner.blind_bundle(
                self.runner.BlindOptions(
                    suite_path=FIXTURE_PATH,
                    bundle_dir=bundle,
                    output_dir=blind_output,
                    seed=17,
                    scenario_ids=("booking-greenfield",),
                )
            )

            self.assertEqual(3, len(answer_key["responses"]))
            self.assertEqual(
                {"booking-greenfield"},
                {item["scenario_id"] for item in answer_key["responses"]},
            )

    def test_completed_scorecard_requires_judge_and_all_dimension_scores(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            bundle = root / "pilot"
            blind_output = root / "blind"
            manifest = self.prepare_bundle(bundle)
            for index, run in enumerate(manifest["runs"], start=1):
                self.record_response(bundle, run, index)

            self.runner.blind_bundle(
                self.runner.BlindOptions(
                    suite_path=FIXTURE_PATH,
                    bundle_dir=bundle,
                    output_dir=blind_output,
                    seed=17,
                )
            )
            scorecard_path = blind_output / "scorecard-template.json"
            with self.assertRaisesRegex(ValueError, "judge identity"):
                self.runner.validate_completed_scorecard(blind_output, scorecard_path)

            scorecard = json.loads(scorecard_path.read_text(encoding="utf-8"))
            scorecard["judge"] = {
                "identity": "independent-judge-1",
                "model": "gpt-5.6-luna",
                "reviewed_at": "2026-08-18T12:10:00+00:00",
                "independence_statement": "I did not inspect the answer key before scoring.",
            }
            for response in scorecard["responses"]:
                response["scores"] = {
                    dimension_id: 3 for dimension_id in response["scores"]
                }
                response["score_rationales"] = {
                    dimension_id: "Observable evidence supports this score."
                    for dimension_id in response["score_rationales"]
                }
                response["overall_notes"] = "Complete blinded review."
            scorecard_path.write_text(json.dumps(scorecard), encoding="utf-8")

            self.runner.validate_completed_scorecard(blind_output, scorecard_path)


if __name__ == "__main__":
    unittest.main()
