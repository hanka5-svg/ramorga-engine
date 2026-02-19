import unittest
from runtime import Runtime


class DummyEngine:
    """Minimal dummy engine for testing the Runtime loop."""
    def __init__(self):
        self.propagated = False
        self.regulated = False

    def propagate(self):
        self.propagated = True

    def regulate(self):
        self.regulated = True

    def snapshot(self):
        return {"ok": True}


class TestRuntime(unittest.TestCase):
    """Basic tests for the Runtime event loop."""

    def test_can_be_instantiated(self):
        rt = Runtime()
        self.assertIsNotNone(rt)

    def test_register_engine(self):
        rt = Runtime()
        dummy = DummyEngine()
        rt.register_engine(dummy)
        self.assertIn(dummy, rt._engines)

    def test_single_step_calls_propagate_and_regulate(self):
        rt = Runtime()
        dummy = DummyEngine()
        rt.register_engine(dummy)

        rt.step()

        self.assertTrue(dummy.propagated)
        self.assertTrue(dummy.regulated)

    def test_run_fixed_number_of_steps(self):
        rt = Runtime()
        dummy = DummyEngine()
        rt.register_engine(dummy)

        rt.run(steps=3)

        # After 3 steps, both flags must be True
        self.assertTrue(dummy.propagated)
        self.assertTrue(dummy.regulated)

    def test_stop_interrupts_loop(self):
        rt = Runtime()
        dummy = DummyEngine()
        rt.register_engine(dummy)

        # Stop immediately
        rt.stop()
        rt.run(steps=5)

        # No propagation should occur
        self.assertFalse(dummy.propagated)
        self.assertFalse(dummy.regulated)


if __name__ == "__main__":
    unittest.main()
