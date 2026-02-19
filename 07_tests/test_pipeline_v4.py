import unittest
from pipeline_v4 import PipelineV4


class TestPipelineV4(unittest.TestCase):
    """Integration tests for PipelineV4 with Field ↔ Meniscus interaction."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV4()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_once(self):
        pipeline = PipelineV4()
        result = pipeline.run_once({"x": 1})

        self.assertIn("pipeline_output", result)
        self.assertIn("tension", result)
        self.assertIn("regulatory_signal", result)
        self.assertIn("system_snapshot", result)

    def test_pipeline_output_structure(self):
        pipeline = PipelineV4()
        result = pipeline.run_once({"x": 1})
        out = result["pipeline_output"]

        self.assertIn("tone", out)
        self.assertIn("generated", out)
        self.assertIn("safe", out)
        self.assertIn("field_processed", out)
        self.assertIn("regulated_by_meniscus", out)

    def test_feedback_loop_values(self):
        pipeline = PipelineV4()
        result = pipeline.run_once({"x": 1})

        tension = result["tension"]
        regulation = result["regulatory_signal"]
        out = result["pipeline_output"]

        self.assertEqual(tension["tension"], "mild")
        self.assertEqual(regulation["regulation"], "stabilize")
        self.assertEqual(out["regulated_by_meniscus"], "stabilize")

    def test_system_snapshot_contains_all_components(self):
        pipeline = PipelineV4()
        result = pipeline.run_once({"x": 1})
        snap = result["system_snapshot"]

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
        pipeline = PipelineV4()
        data = {"foo": "bar"}
        pipeline.run_once(data)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
