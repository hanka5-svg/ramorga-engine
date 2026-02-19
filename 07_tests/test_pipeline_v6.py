import unittest
from pipeline_v6 import PipelineV6


class TestPipelineV6(unittest.TestCase):
    """Integration tests for PipelineV6 — multi-step homeostatic cycle."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV6()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_multiple_steps(self):
        pipeline = PipelineV6()
        result = pipeline.run({"x": 1}, steps=5)

        self.assertIn("history", result)
        self.assertEqual(len(result["history"]), 5)

    def test_tension_and_regulation_evolve_over_time(self):
        pipeline = PipelineV6()
        result = pipeline.run({"x": 1}, steps=5)

        history = result["history"]

        # Each step should produce a dict with tension and regulation
        for step in history:
            self.assertIn("tension", step)
            self.assertIn("regulation", step)

        # Tension should always return to 0 after regulation
        tensions = [step["tension"] for step in history]
        self.assertTrue(all(t == 0 for t in tensions))

        # Regulation should accumulate negative values
        regulations = [step["regulation"] for step in history]
        self.assertEqual(regulations, [-1, -2, -3, -4, -5])

    def test_system_snapshot_present_in_each_step(self):
        pipeline = PipelineV6()
        result = pipeline.run({"x": 1}, steps=3)

        for step in result["history"]:
            snap = step["system_snapshot"]

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

    def test_pipeline_does_not_mutate_input(self):
        pipeline = PipelineV6()
        data = {"foo": "bar"}
        pipeline.run(data, steps=3)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
