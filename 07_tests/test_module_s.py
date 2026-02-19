import unittest
from module_s import ModuleS


class TestModuleS(unittest.TestCase):
    """Basic tests for the Module S skeleton."""

    def test_can_be_instantiated(self):
        module = ModuleS()
        self.assertIsNotNone(module)

    def test_initial_state_is_none(self):
        module = ModuleS()
        self.assertIsNone(module.state)

    def test_snapshot_returns_dict(self):
        module = ModuleS()
        snap = module.snapshot()
        self.assertIsInstance(snap, dict)


if __name__ == "__main__":
    unittest.main()
