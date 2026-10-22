import unittest
from pathlib import Path

SKILLS = Path(__file__).resolve().parents[1] / "skills"

class RuntimeGuidanceTests(unittest.TestCase):
    def test_cross_skill_router_has_chatgpt_tool_fallback(self):
        for name in ("grill-me", "grill-with-docs", "implement", "triage", "wayfinder"):
            with self.subTest(skill=name):
                text=(SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("## ChatGPT execution note", text)
                self.assertIn("skill-reading", text)
                self.assertIn("unavailable", text)

    def test_specialized_workflows_disclose_environment_requirements(self):
        for name in ("code-review", "implement-spec", "research", "wizard"):
            with self.subTest(skill=name):
                text=(SKILLS / name / "SKILL.md").read_text(encoding="utf-8")
                self.assertIn("## ChatGPT execution note", text)
                self.assertTrue(any(phrase in text.lower() for phrase in ("not claim", "never claim")), name)

if __name__ == "__main__":
    unittest.main()
