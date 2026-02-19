import unittest
from pipeline_v11 import PipelineV11


class TestPipelineV11(unittest.TestCase):
    """Integration tests for PipelineV11 — meta-regulation (regulation of regulation)."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV11()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_multiple_steps(self):
        pipeline = PipelineV11()
        result = pipeline.run({"x": 1}, steps=5)

        self.assertIn("history", result)
        self.assertEqual(len(result["history"]), 5)

    def test_meta_parameters_change_over_time(self):
        pipeline = PipelineV11()
        result = pipeline.run({"x": 1}, steps=5)

        meta_stability = [step["meta_stability"] for step in result["history"]]
        meta_gain = [step["meta_gain"] for step in result["history"]]
        meta_damping = [step["meta_damping"] for step in result["history"]]

        # Meta-parameters should not remain constant
        self.assertTrue(any(m != meta_stability[0] for m in meta_stability))
        self.assertTrue(any(g != meta_gain[0] for g in meta_gain))
        self.assertTrue(any(d != meta_damping[0] for d in meta_damping))

    def test_meta_regulation_affects_sensitivities(self):
        pipeline = PipelineV11()
        result = pipeline.run({"x": 1}, steps=5)

        sens_cog = [step["sensitivity_cognitive"] for step in result["history"]]
        sens_aff = [step["sensitivity_affective"] for step in result["history"]]

        # Sensitivities should evolve under meta-regulation
        self.assertTrue(any(s != sens_cog[0] for s in sens_cog))
        self.assertTrue(any(s != sens_aff[0] for s in sens_aff))

        # Sensitivities must stay >= 1
        self.assertTrue(all(s >= 1.0 for s in sens_cog))
        self.assertTrue(all(s >= 1.0 for s in sens_aff))

    def test_regulation_accumulates(self):
        pipeline = PipelineV11()
        result = pipeline.run({"x": 1}, steps=5)

        reg_cog = [step["regulation_cognitive"] for step in result["history"]]
        reg_aff = [step["regulation_affective"] for step in result["history"]]

        # At least some regulation should be negative (down-regulation)
        self.assertTrue(any(r < 0 for r in reg_cog))
        self.assertTrue(any(r < 0 for r in reg_aff))

    def test_thresholds_adapt(self):
        pipeline = PipelineV11()
        result = pipeline.run({"x": 1}, steps=5)

        thr_cog = [step["threshold_cognitive"] for step in result["history"]]
        thr_aff = [step["threshold_affective"] for step in result["history"]]

        self.assertTrue(any(t != thr_cog[0] for t in thr_cog))
        self.assertTrue(any(t != thr_aff[0] for t in thr_aff))

    def test_system_snapshot_present_in_each_step(self):
        pipeline = PipelineV11()
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
        pipeline = PipelineV11()
        data = {"foo": "bar"}
        pipeline.run(data, steps=3)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
