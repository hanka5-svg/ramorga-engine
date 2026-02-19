import unittest
from pipeline_v7 import PipelineV7


class TestPipelineV7(unittest.TestCase):
    """Integration tests for PipelineV7 — adaptive homeostasis."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV7()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_multiple_steps(self):
        pipeline = PipelineV7()
        result = pipeline.run({"x": 1}, steps=5)

        self.assertIn("history", result)
        self.assertEqual(len(result["history"]), 5)

    def test_adaptive_threshold_and_sensitivity_change(self):
        pipeline = PipelineV7()
        result = pipeline.run({"x": 1}, steps=5)

        thresholds = [step["threshold"] for step in result["history"]]
        sensitivities = [step["sensitivity"] for step in result["history"]]

        # Threshold should not be constant
        self.assertTrue(any(t != thresholds[0] for t in thresholds))

        # Sensitivity should not be constant
        self.assertTrue(any(s != sensitivities[0] for s in sensitivities))

    def test_regulation_depends_on_history(self):
        pipeline = PipelineV7()
        result = pipeline.run({"x": 1}, steps=5)

        tensions = [step["tension"] for step in result["history"]]
        regulations = [step["regulation"] for step in result["history"]]

        # Regulation should accumulate negative values when tension > threshold
        self.assertTrue(any(r < 0 for r in regulations))

        # Tension should sometimes be reduced by regulation
        self.assertTrue(any(t < i + 1 for i, t in enumerate(tensions)))

    def test_system_snapshot_present_in_each_step(self):
        pipeline = PipelineV7()
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
        pipeline = PipelineV7()
        data = {"foo": "bar"}
        pipeline.run(data, steps=3)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
