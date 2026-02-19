from __future__ import annotations
from typing import Any, Dict, List

from integration import build_system


class PipelineV7:
    """
    Pipeline V7 — adaptive homeostasis based on history.

    New elements:
        - Field has a tension threshold that adapts over time.
        - Meniscus has a regulation sensitivity that adapts based on workload.
        - Regulation strength depends on sensitivity.
        - Threshold and sensitivity evolve with each step.

    This is the first adaptive cycle in RAMORGA.
    """

    def __init__(self) -> None:
        self.system = build_system()

        # Internal states
        self.field_tension = 0
        self.tension_threshold = 1

        self.meniscus_regulation = 0
        self.regulation_sensitivity = 1

    def run(self, data: Dict[str, Any], steps: int = 5) -> Dict[str, Any]:
        """
        Execute N adaptive homeostatic cycles.
        """

        history: List[Dict[str, Any]] = []

        for _ in range(steps):
            # Step 1: Field increases tension
            self.field_tension += 1

            # Step 2: Meniscus generates regulation depending on sensitivity
            if self.field_tension > self.tension_threshold:
                regulation_value = -1 * self.regulation_sensitivity
            else:
                regulation_value = 0

            self.meniscus_regulation += regulation_value

            # Step 3: Field applies regulation
            self.field_tension += regulation_value

            # Step 4: Adaptation
            # Field threshold increases if tension repeatedly exceeds it
            if self.field_tension > self.tension_threshold:
                self.tension_threshold += 1
            else:
                self.tension_threshold = max(1, self.tension_threshold - 0.1)

            # Meniscus sensitivity increases if it had to regulate
            if regulation_value != 0:
                self.regulation_sensitivity += 0.1
            else:
                self.regulation_sensitivity = max(1, self.regulation_sensitivity - 0.05)

            # Step 5: Runtime performs a system step
            self.system.runtime.step()

            # Save snapshot
            history.append({
                "tension": self.field_tension,
                "threshold": self.tension_threshold,
                "regulation": self.meniscus_regulation,
                "sensitivity": self.regulation_sensitivity,
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
    pipeline = PipelineV7()
    result = pipeline.run({"x": 1}, steps=3)

    assert "history" in result
    assert len(result["history"]) == 3

    print("PipelineV7 self-test passed.")


if __name__ == "__main__":
    _self_test()
