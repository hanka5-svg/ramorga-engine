import unittest
from integration import build_system


class TestRamorgaIntegration(unittest.TestCase):
    """Integration tests for the full RAMORGA system."""

    def test_system_can_be_built(self):
        system = build_system()
        self.assertIsNotNone(system)

    def test_all_components_exist(self):
        system = build_system()

        self.assertIsNotNone(system.field)
        self.assertIsNotNone(system.meniscus)
        self.assertIsNotNone(system.mod_c)
        self.assertIsNotNone(system.mod_g)
        self.assertIsNotNone(system.mod_s)
        self.assertIsNotNone(system.runtime)

    def test_snapshot_contains_all_components(self):
        system = build_system()
        snap = system.snapshot()

        self.assertIn("field", snap)
        self.assertIn("meniscus", snap)
        self.assertIn("C", snap)
        self.assertIn("G", snap)
        self.assertIn("S", snap)

        self.assertIsInstance(snap["field"], dict)
        self.assertIsInstance(snap["meniscus"], dict)
        self.assertIsInstance(snap["C"], dict)
        self.assertIsInstance(snap["G"], dict)
        self.assertIsInstance(snap["S"], dict)

    def test_runtime_step_runs_without_errors(self):
        system = build_system()

        # This should not raise any exceptions
        try:
            system.runtime.step()
        except Exception as e:
            self.fail(f"Runtime step raised an exception: {e}")

    def test_runtime_can_run_multiple_steps(self):
        system = build_system()

        try:
            system.runtime.run(steps=3)
        except Exception as e:
            self.fail(f"Runtime run(steps=3) raised an exception: {e}")


if __name__ == "__main__":
    unittest.main()
