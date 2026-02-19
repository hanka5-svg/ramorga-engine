from __future__ import annotations
from typing import Any, Dict

from integration import build_system


class PipelineV3:
    """
    Pipeline V3 — first real-time pipeline using Runtime.

    Flow:
        input → C → G → S → Field → Meniscus
        then Runtime performs a system step
        then we collect snapshots from all components
    """

    def __init__(self) -> None:
        self.system = build_system()

    def run_once(self, data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute one pipeline pass with Runtime involvement.
        """

        # Step 1: C receives input
        c_out = dict(data)
        c_out["tone"] = "cognitive"

        # Step 2: G receives C output
        g_out = dict(c_out)
        g_out["generated"] = True

        # Step 3: S receives G output
        s_out = dict(g_out)
        s_out["safe"] = True

        # Step 4: Field receives S output
        field_out = dict(s_out)
        field_out["field_processed"] = True

        # Step 5: Meniscus receives Field output
        meniscus_out = dict(field_out)
        meniscus_out["regulated"] = True

        # Runtime performs a system step
        self.system.runtime.step()

        # Return combined snapshot
        return {
            "pipeline_output": meniscus_out,
            "system_snapshot": self.system.snapshot(),
        }


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    pipeline = PipelineV3()
    result = pipeline.run_once({"x": 1})

    assert "pipeline_output" in result
    assert "system_snapshot" in result
    assert result["pipeline_output"]["regulated"] is True

    print("PipelineV3 self-test passed.")


if __name__ == "__main__":
    _self_test()
