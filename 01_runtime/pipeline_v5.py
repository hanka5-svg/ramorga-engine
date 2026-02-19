from __future__ import annotations
from typing import Any, Dict

from integration import build_system


class PipelineV5:
    """
    Pipeline V5 — first true homeostatic cycle with state updates.

    Flow:
        input → C → G → S → Field
        Field increases tension
        Meniscus receives tension and produces regulation
        Field updates tension based on regulation
        Meniscus updates its regulation level
        Runtime performs a system step
        Return updated states
    """

    def __init__(self) -> None:
        self.system = build_system()

        # Initialize simple internal states
        self.field_tension = 0
        self.meniscus_regulation = 0

    def run_once(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute one homeostatic cycle.
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

        # Step 4: Field receives S output and increases tension
        self.field_tension += 1
        tension = {"tension_level": self.field_tension}

        # Step 5: Meniscus receives tension and generates regulation
        regulation_value = -1 if self.field_tension > 0 else 0
        self.meniscus_regulation += regulation_value
        regulatory_signal = {"regulation_level": self.meniscus_regulation}

        # Step 6: Field updates tension based on regulation
        self.field_tension += regulation_value

        # Runtime performs a system step
        self.system.runtime.step()

        # Return combined snapshot
        return {
            "pipeline_output": {
                "tone": c_out["tone"],
                "generated": g_out["generated"],
                "safe": s_out["safe"],
                "tension_after_regulation": self.field_tension,
                "regulation_level": self.meniscus_regulation,
            },
            "tension": tension,
            "regulatory_signal": regulatory_signal,
            "system_snapshot": self.system.snapshot(),
        }


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    pipeline = PipelineV5()
    result = pipeline.run_once({"x": 1})

    assert "pipeline_output" in result
    assert "tension" in result
    assert "regulatory_signal" in result
    assert result["pipeline_output"]["tension_after_regulation"] == 0

    print("PipelineV5 self-test passed.")


if __name__ == "__main__":
    _self_test()
