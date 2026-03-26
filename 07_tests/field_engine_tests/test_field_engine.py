import unittest
from field_engine import FieldEngine


class TestFieldEngine(unittest.TestCase):
    """Basic tests for the FieldEngine skeleton."""

    def test_initial_state_is_none(self):
        engine = FieldEngine()
        self.assertIsNone(engine.state)

    def test_snapshot_returns_dict(self):
        engine = FieldEngine()
        snap = engine.snapshot()
        self.assertIsInstance(snap, dict)


if __name__ == "__main__":
    unittest.main()
