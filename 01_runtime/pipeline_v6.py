from __future__ import annotations
from typing import Any, Dict, List

from integration import build_system


class PipelineV6:
    """
    Pipeline V6 — multi-step homeostatic cycle.

    Flow per step:
        Field tension increases
        Meniscus generates regulation
        Field applies regulation
        Meniscus updates its regulation state
        Runtime performs a system step

    After N steps, return the full history of states.
    """

    def __init__(self) -> None:
        self.system = build_system()

        # Internal states
        self.field_tension = 0
        self.meniscus_regulation = 0

    def run(self, data: Dict[str, Any], steps: int = 5) -> Dict[str, Any]:
        """
        Execute N homeostatic cycles.
        """

        history: List[Dict[str, Any]] = []

        for _ in range(steps):
            # Step 1: Field increases tension
            self.field_tension += 1

            # Step 2: Meniscus generates regulation
            regulation_value = -1 if self.field_tension > 0 else 0
            self.meniscus_regulation += regulation_value

            # Step 3: Field applies regulation
            self.field_tension += regulation_value

            # Step 4: Runtime performs a system step
            self.system.runtime.step()

            # Save snapshot
            history.append({
                "tension": self.field_tension,
                "regulation": self.meniscus_regulation,
                "system_snapshot": self.system.snapshot(),
            })

        return {
            "input": data,
            "steps": steps,
            "history": history,
        }


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    pipeline = PipelineV6()
    result = pipeline.run({"x": 1}, steps=3)

    assert "history" in result
    assert len(result["history"]) == 3

    print("PipelineV6 self-test passed.")


if __name__ == "__main__":
    _self_test()
