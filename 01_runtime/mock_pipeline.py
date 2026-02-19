from __future__ import annotations
from typing import Any, Dict

from module_c import ModuleC
from module_g import ModuleG
from module_s import ModuleS
from field_engine import FieldEngine
from meniscus_engine import MeniscusEngine


class MockPipeline:
    """
    First mock data pipeline for RAMORGA.

    This pipeline does NOT implement real logic.
    It only demonstrates the flow of data through:

        C → G → S → Field → Meniscus

    Each module receives a simple dictionary and returns a modified dictionary.
    """

    def __init__(self) -> None:
        self.mod_c = ModuleC()
        self.mod_g = ModuleG()
        self.mod_s = ModuleS()
        self.field = FieldEngine()
        self.meniscus = MeniscusEngine()

    def run_once(self, input_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute one mock pipeline pass.
        """

        # Step 1: C processes input
        c_out = {"from": "C", "input": input_data}

        # Step 2: G processes C output
        g_out = {"from": "G", "input": c_out}

        # Step 3: S processes G output
        s_out = {"from": "S", "input": g_out}

        # Step 4: FieldEngine receives S output
        field_out = {"from": "Field", "input": s_out}

        # Step 5: MeniscusEngine receives Field output
        meniscus_out = {"from": "Meniscus", "input": field_out}

        return meniscus_out


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    pipeline = MockPipeline()
    result = pipeline.run_once({"hello": "world"})

    assert result["from"] == "Meniscus"
    assert "input" in result

    print("Mock pipeline self-test passed.")


if __name__ == "__main__":
    _self_test()
