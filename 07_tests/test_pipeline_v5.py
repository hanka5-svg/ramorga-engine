import unittest
from pipeline_v5 import PipelineV5


class TestPipelineV5(unittest.TestCase):
    """Integration tests for PipelineV5 — first homeostatic cycle."""

    def test_pipeline_can_be_instantiated(self):
        pipeline = PipelineV5()
        self.assertIsNotNone(pipeline)

    def test_pipeline_runs_once(self):
        pipeline = PipelineV5()
        result = pipeline.run_once({"x": 1})

        self.assertIn("pipeline_output", result)
        self.assertIn("tension", result)
        self.assertIn("regulatory_signal", result)
        self.assertIn("system_snapshot", result)

    def test_homeostatic_cycle_updates_state(self):
        pipeline = PipelineV5()
        result = pipeline.run_once({"x": 1})

        out = result["pipeline_output"]

        # After one cycle:
        # Field tension: +1 (from Field) + (-1 from Meniscus) = 0
        self.assertEqual(out["tension_after_regulation"], 0)

        # Meniscus regulation accumulates -1
        self.assertEqual(out["regulation_level"], -1)

    def test_tension_and_regulation_structures(self):
        pipeline = PipelineV5()
        result = pipeline.run_once({"x": 1})

        tension = result["tension"]
        regulation = result["regulatory_signal"]

        self.assertIn("tension_level", tension)
        self.assertIn("regulation_level", regulation)

        self.assertEqual(tension["tension_level"], 1)
        self.assertEqual(regulation["regulation_level"], -1)

    def test_system_snapshot_contains_all_components(self):
        pipeline = PipelineV5()
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
        pipeline = PipelineV5()
        data = {"foo": "bar"}
        pipeline.run_once(data)

        self.assertEqual(data, {"foo": "bar"})


if __name__ == "__main__":
    unittest.main()
