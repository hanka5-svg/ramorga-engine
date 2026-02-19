from __future__ import annotations
from typing import Any, Dict

from module_c import ModuleC
from module_g import ModuleG
from module_s import ModuleS
from field_engine import FieldEngine
from meniscus_engine import MeniscusEngine


class PipelineV2:
    """
    Second pipeline with minimal real logic.

    Each module performs a simple transformation on the data:
        C → adds cognitive tone
        G → marks generative flow
        S → marks safety shaping
        Field → marks field processing
        Meniscus → marks regulatory processing
    """

    def __init__(self) -> None:
        self.mod_c = ModuleC()
        self.mod_g = ModuleG()
        self.mod_s = ModuleS()
        self.field = FieldEngine()
        self.meniscus = MeniscusEngine()

    def run_once(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute one pipeline pass with minimal logic.
        """

        # Step 1: C
        c_out = dict(data)
        c_out["tone"] = "cognitive"

        # Step 2: G
        g_out = dict(c_out)
        g_out["generated"] = True

        # Step 3: S
        s_out = dict(g_out)
        s_out["safe"] = True

        # Step 4: Field
        field_out = dict(s_out)
        field_out["field_processed"] = True

        # Step 5: Meniscus
        meniscus_out = dict(field_out)
        meniscus_out["regulated"] = True

        return meniscus_out


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    pipeline = PipelineV2()
    result = pipeline.run_once({"x": 1})

    assert result["tone"] == "cognitive"
    assert result["generated"] is True
    assert result["safe"] is True
    assert result["field_processed"] is True
    assert result["regulated"] is True

    print("PipelineV2 self-test passed.")


if __name__ == "__main__":
    _self_test()
