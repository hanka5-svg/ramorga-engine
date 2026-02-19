import unittest
from meniscus_engine import MeniscusEngine


class TestMeniscusEngine(unittest.TestCase):
    """Basic tests for the MeniscusEngine skeleton."""

    def test_can_be_instantiated(self):
        engine = MeniscusEngine()
        self.assertIsNotNone(engine)

    def test_initial_state_is_none(self):
        engine = MeniscusEngine()
        self.assertIsNone(engine.state)

    def test_snapshot_returns_dict(self):
        engine = MeniscusEngine()
        snap = engine.snapshot()
        self.assertIsInstance(snap, dict)


if __name__ == "__main__":
    unittest.main()
