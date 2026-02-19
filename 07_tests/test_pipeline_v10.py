import unittest
from pipeline_v10 import PipelineV10


class TestPipelineV10(unittest.TestCase):
    """Integration tests for PipelineV10 — nonlinear multidimensional homeostasis."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV10()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_multiple_steps(self):
        pipeline = PipelineV10()
        result = pipeline.run({"x": 1}, steps=5)

        self.assertIn("history", result)
        self.assertEqual(len(result["history"]), 5)

    def test_nonlinear_tension_growth(self):
        pipeline = PipelineV10()
        result = pipeline.run({"x": 1}, steps=5)

        tensions_cog = [step["tension_cognitive"] for step in result["history"]]
        tensions_aff = [step["tension_affective"] for step in result["history"]]

        # Sigmoidal growth should produce non-linear increments
        self.assertTrue(any(tensions_cog[i] - tensions_cog[i-1] != tensions_cog[1] - tensions_cog[0]
                            for i in range(2, len(tensions_cog))))
        self.assertTrue(any(tensions_aff[i] - tensions_aff[i-1] != tensions_aff[1] - tensions_aff[0]
                            for i in range(2, len(tensions_aff))))

    def test_exponential_regulation_occurs(self):
        pipeline = PipelineV10()
        result = pipeline.run({"x": 1}, steps=5)

        reg_cog = [step["regulation_cognitive"] for step in result["history"]]
        reg_aff = [step["regulation_affective"] for step in result["history"]]

        # Regulation should include large negative values due to exp()
        self.assertTrue(any(r < -2 for r in reg_cog))
        self.assertTrue(any(r < -2 for r in reg_aff))

    def test_thresholds_adapt_nonlinearly(self):
        pipeline = PipelineV10()
        result = pipeline.run({"x": 1}, steps=5)

        thr_cog = [step["threshold_cognitive"] for step in result["history"]]
        thr_aff = [step["threshold_affective"] for step in result["history"]]

        # Thresholds should change smoothly (tanh-based)
        self.assertTrue(any(t != thr_cog[0] for t in thr_cog))
        self.assertTrue(any(t != thr_aff[0] for t in thr_aff))

    def test_sensitivities_adapt_nonlinearly(self):
        pipeline = PipelineV10()
        result = pipeline.run({"x": 1}, steps=5)

        sens_cog = [step["sensitivity_cognitive"] for step in result["history"]]
        sens_aff = [step["sensitivity_affective"] for step in result["history"]]

        # Sensitivities should evolve due to tanh(abs(reg))
        self.assertTrue(any(s != sens_cog[0] for s in sens_cog))
        self.assertTrue(any(s != sens_aff[0] for s in sens_aff))

    def test_system_snapshot_present_in_each_step(self):
        pipeline = PipelineV10()
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
        pipeline = PipelineV10()
        data = {"foo": "bar"}
        pipeline.run(data, steps=3)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
