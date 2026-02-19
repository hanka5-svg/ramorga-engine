from __future__ import annotations
from typing import Optional

from runtime import Runtime
from field_engine import FieldEngine
from meniscus_engine import MeniscusEngine
from module_c import ModuleC
from module_g import ModuleG
from module_s import ModuleS


class RamorgaSystem:
    """
    High-level container wiring together all RAMORGA components.

    This class does NOT implement logic.
    It only connects:
    - FieldEngine
    - MeniscusEngine
    - Modules C/G/S
    - Runtime
    """

    def __init__(self) -> None:
        # Core engines
        self.field = FieldEngine()
        self.meniscus = MeniscusEngine()

        # Modules
        self.mod_c = ModuleC()
        self.mod_g = ModuleG()
        self.mod_s = ModuleS()

        # Runtime
        self.runtime = Runtime()

        # Register engines in runtime
        self.runtime.register_engine(self.field)
        self.runtime.register_engine(self.meniscus)
        self.runtime.register_engine(self.mod_c)
        self.runtime.register_engine(self.mod_g)
        self.runtime.register_engine(self.mod_s)

    def snapshot(self) -> dict:
        """
        Return a combined snapshot of the entire system.
        """
        return {
            "field": self.field.snapshot(),
            "meniscus": self.meniscus.snapshot(),
            "C": self.mod_c.snapshot(),
            "G": self.mod_g.snapshot(),
            "S": self.mod_s.snapshot(),
        }


def build_system() -> RamorgaSystem:
    """
    Factory function returning a fully wired RAMORGA system.
    """
    return RamorgaSystem()


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    system = build_system()
    snap = system.snapshot()

    assert "field" in snap
    assert "meniscus" in snap
    assert "C" in snap
    assert "G" in snap
    assert "S" in snap

    print("Integration self-test passed.")


if __name__ == "__main__":
    _self_test()
