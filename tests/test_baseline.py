"""Minimal first-run smoke test for the sandbox's CI wiring."""
from pathlib import Path
import unittest


class SandboxBaseline(unittest.TestCase):
    def test_readme_and_agent_instructions_present(self):
        root = Path(__file__).resolve().parent.parent
        self.assertTrue((root / "README.md").is_file())
        self.assertTrue((root / "AGENTS.md").is_file())


if __name__ == "__main__":
    unittest.main()
