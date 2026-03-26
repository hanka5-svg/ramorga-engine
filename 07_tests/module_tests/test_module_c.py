import unittest
from module_c import ModuleC


class TestModuleC(unittest.TestCase):
    """Basic tests for the Module C skeleton."""

    def test_can_be_instantiated(self):
        module = ModuleC()
        self.assertIsNotNone(module)

    def test_initial_state_is_none(self):
        module = ModuleC()
        self.assertIsNone(module.state)

    def test_snapshot_returns_dict(self):
        module = ModuleC()
        snap = module.snapshot()
        self.assertIsInstance(snap, dict)


if __name__ == "__main__":
    unittest.main()
