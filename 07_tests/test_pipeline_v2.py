import unittest
from pipeline_v2 import PipelineV2


class TestPipelineV2(unittest.TestCase):
    """Integration tests for the second pipeline with minimal logic."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV2()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_once(self):
        pipeline = PipelineV2()
        result = pipeline.run_once({"x": 1})

        self.assertIsInstance(result, dict)
        self.assertIn("tone", result)
        self.assertIn("generated", result)
        self.assertIn("safe", result)
        self.assertIn("field_processed", result)
        self.assertIn("regulated", result)

    def test_pipeline_logic_values(self):
        pipeline = PipelineV2()
        result = pipeline.run_once({"x": 1})

        self.assertEqual(result["tone"], "cognitive")
        self.assertTrue(result["generated"])
        self.assertTrue(result["safe"])
        self.assertTrue(result["field_processed"])
        self.assertTrue(result["regulated"])

    def test_pipeline_preserves_original_data(self):
        pipeline = PipelineV2()
        data = {"foo": "bar"}
        result = pipeline.run_once(data)

        # Original keys must still be present
        self.assertIn("foo", result)
        self.assertEqual(result["foo"], "bar")

    def test_pipeline_does_not_mutate_input(self):
        pipeline = PipelineV2()
        data = {"a": 1}
        pipeline.run_once(data)

        # Input must remain unchanged
        self.assertEqual(data, {"a": 1})


if __name__ == "__main__":
    unittest.main()
