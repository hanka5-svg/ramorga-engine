import unittest
from mock_pipeline import MockPipeline


class TestMockPipeline(unittest.TestCase):
    """Integration tests for the mock data pipeline."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = MockPipeline()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_once(self):
        pipeline = MockPipeline()
        result = pipeline.run_once({"hello": "world"})

        self.assertIsInstance(result, dict)
        self.assertIn("from", result)
        self.assertEqual(result["from"], "Meniscus")

    def test_pipeline_structure_is_nested(self):
        pipeline = MockPipeline()
        result = pipeline.run_once({"x": 1})

        # Meniscus → Field → S → G → C → input
        self.assertIn("input", result)
        lvl_field = result["input"]
        self.assertIn("input", lvl_field)
        lvl_s = lvl_field["input"]
        self.assertIn("input", lvl_s)
        lvl_g = lvl_s["input"]
        self.assertIn("input", lvl_g)
        lvl_c = lvl_g["input"]
        self.assertIn("input", lvl_c)

    def test_pipeline_preserves_original_data(self):
        pipeline = MockPipeline()
        data = {"foo": "bar"}
        result = pipeline.run_once(data)

        # Navigate down to original input
        lvl_field = result["input"]
        lvl_s = lvl_field["input"]
        lvl_g = lvl_s["input"]
        lvl_c = lvl_g["input"]
        original = lvl_c["input"]

        self.assertEqual(original, data)


if __name__ == "__main__":
    unittest.main()
