import unittest
from module_g import ModuleG


class TestModuleG(unittest.TestCase):
    """Basic tests for the Module G skeleton."""

    def test_can_be_instantiated(self):
        module = ModuleG()
        self.assertIsNotNone(module)

    def test_initial_state_is_none(self):
        module = ModuleG()
        self.assertIsNone(module.state)

    def test_snapshot_returns_dict(self):
        module = ModuleG()
        snap = module.snapshot()
        self.assertIsInstance(snap, dict)


if __name__ == "__main__":
    unittest.main()
