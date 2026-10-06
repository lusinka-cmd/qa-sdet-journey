import json
import tempfile
import unittest
from pathlib import Path

import agent


class AgentUnitTests(unittest.TestCase):
    def test_loads_requirements_and_existing_cases(self):
        requirements, cases = agent.load_inputs()
        self.assertIn("locked user", requirements)
        self.assertEqual(len(cases), 3)

    def test_request_contains_criteria_and_inputs(self):
        payload = agent.build_request("The user can log in.", [{"id": "TC-1"}], "model-test")
        self.assertEqual(payload["model"], "model-test")
        self.assertIn("traceable to a requirement", payload["instructions"])
        self.assertIn("TC-1", payload["input"])
        self.assertEqual(payload["text"]["format"]["type"], "json_object")

    def test_extracts_text_from_responses_api_shape(self):
        response = {"output": [{"type": "message", "content": [
            {"type": "output_text", "text": '{"coverage_gaps": []}'}
        ]}]}
        self.assertEqual(agent.extract_output_text(response), '{"coverage_gaps": []}')

    def test_rejects_incomplete_report(self):
        with self.assertRaises(ValueError):
            agent.validate_report({"coverage_gaps": []})

    def test_saves_report_and_drafts_without_executing_them(self):
        report = {
            "requirement_summary": "Login checks",
            "coverage_gaps": [],
            "possible_duplicates": [],
            "draft_tests": [{"name": "test_locked", "covers": "Locked user", "code": "def test_locked(page):\n    assert True", "assumptions": []}],
            "human_review": ["Confirm selectors"],
        }
        with tempfile.TemporaryDirectory() as tmp:
            report_path, tests_path = agent.save_report(report, Path(tmp))
            self.assertEqual(json.loads(report_path.read_text(encoding="utf-8")), report)
            draft = tests_path.read_text(encoding="utf-8")
            self.assertIn("not executed", draft)
            self.assertIn("def test_locked(page):", draft)


if __name__ == "__main__":
    unittest.main()
