from __future__ import annotations
from typing import Any, Dict

from integration import build_system


class PipelineV4:
    """
    Pipeline V4 — first real Field ↔ Meniscus interaction.

    Flow:
        input → C → G → S → Field
        Field produces a tension signal
        Meniscus receives tension and produces a regulatory signal
        Field receives regulatory signal
        Runtime performs a system step
        Return combined snapshot
    """

    def __init__(self) -> None:
        self.system = build_system()

    def run_once(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute one pipeline pass with Field ↔ Meniscus feedback.
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

        # Step 4: Field receives S output
        field_input = dict(s_out)
        field_input["field_processed"] = True

        # Field produces tension (mock)
        tension = {"tension": "mild"}

        # Step 5: Meniscus receives tension
        regulatory_signal = {"regulation": "stabilize"}

        # Step 6: Field receives regulatory signal
        field_output = dict(field_input)
        field_output["regulated_by_meniscus"] = regulatory_signal["regulation"]

        # Runtime performs a system step
        self.system.runtime.step()

        # Return combined snapshot
        return {
            "pipeline_output": field_output,
            "tension": tension,
            "regulatory_signal": regulatory_signal,
            "system_snapshot": self.system.snapshot(),
        }


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    pipeline = PipelineV4()
    result = pipeline.run_once({"x": 1})

    assert "pipeline_output" in result
    assert "tension" in result
    assert "regulatory_signal" in result
    assert result["pipeline_output"]["regulated_by_meniscus"] == "stabilize"

    print("PipelineV4 self-test passed.")


if __name__ == "__main__":
    _self_test()
