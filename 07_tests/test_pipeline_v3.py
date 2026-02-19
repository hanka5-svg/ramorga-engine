import unittest
from pipeline_v3 import PipelineV3


class TestPipelineV3(unittest.TestCase):
    """Integration tests for PipelineV3 with Runtime involvement."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV3()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_once(self):
        pipeline = PipelineV3()
        result = pipeline.run_once({"x": 1})

        self.assertIn("pipeline_output", result)
        self.assertIn("system_snapshot", result)

    def test_pipeline_output_structure(self):
        pipeline = PipelineV3()
        result = pipeline.run_once({"x": 1})
        out = result["pipeline_output"]

        self.assertIn("tone", out)
        self.assertIn("generated", out)
        self.assertIn("safe", out)
        self.assertIn("field_processed", out)
        self.assertIn("regulated", out)

    def test_pipeline_logic_values(self):
        pipeline = PipelineV3()
        result = pipeline.run_once({"x": 1})
        out = result["pipeline_output"]

        self.assertEqual(out["tone"], "cognitive")
        self.assertTrue(out["generated"])
        self.assertTrue(out["safe"])
        self.assertTrue(out["field_processed"])
        self.assertTrue(out["regulated"])

    def test_system_snapshot_contains_all_components(self):
        pipeline = PipelineV3()
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
        pipeline = PipelineV3()
        data = {"foo": "bar"}
        pipeline.run_once(data)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
