import unittest
from pipeline_v8 import PipelineV8


class TestPipelineV8(unittest.TestCase):
    """Integration tests for PipelineV8 — multidimensional adaptive homeostasis."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV8()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_multiple_steps(self):
        pipeline = PipelineV8()
        result = pipeline.run({"x": 1}, steps=5)

        self.assertIn("history", result)
        self.assertEqual(len(result["history"]), 5)

    def test_both_tensions_evolve(self):
        pipeline = PipelineV8()
        result = pipeline.run({"x": 1}, steps=5)

        tensions_cog = [step["tension_cognitive"] for step in result["history"]]
        tensions_aff = [step["tension_affective"] for step in result["history"]]

        # Both dimensions must evolve over time
        self.assertTrue(any(t != tensions_cog[0] for t in tensions_cog))
        self.assertTrue(any(t != tensions_aff[0] for t in tensions_aff))

    def test_thresholds_adapt_independently(self):
        pipeline = PipelineV8()
        result = pipeline.run({"x": 1}, steps=5)

        thr_cog = [step["threshold_cognitive"] for step in result["history"]]
        thr_aff = [step["threshold_affective"] for step in result["history"]]

        # Thresholds should not remain constant
        self.assertTrue(any(t != thr_cog[0] for t in thr_cog))
        self.assertTrue(any(t != thr_aff[0] for t in thr_aff))

    def test_sensitivities_adapt_independently(self):
        pipeline = PipelineV8()
        result = pipeline.run({"x": 1}, steps=5)

        sens_cog = [step["sensitivity_cognitive"] for step in result["history"]]
        sens_aff = [step["sensitivity_affective"] for step in result["history"]]

        # Sensitivities should change over time
        self.assertTrue(any(s != sens_cog[0] for s in sens_cog))
        self.assertTrue(any(s != sens_aff[0] for s in sens_aff))

    def test_regulation_occurs_in_both_dimensions(self):
        pipeline = PipelineV8()
        result = pipeline.run({"x": 1}, steps=5)

        reg_cog = [step["regulation_cognitive"] for step in result["history"]]
        reg_aff = [step["regulation_affective"] for step in result["history"]]

        # Regulation should accumulate negative values in at least one dimension
        self.assertTrue(any(r < 0 for r in reg_cog))
        self.assertTrue(any(r < 0 for r in reg_aff))

    def test_system_snapshot_present_in_each_step(self):
        pipeline = PipelineV8()
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
        pipeline = PipelineV8()
        data = {"foo": "bar"}
        pipeline.run(data, steps=3)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
