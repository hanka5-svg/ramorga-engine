from __future__ import annotations
from typing import Any, Dict, List

from integration import build_system


class PipelineV8:
    """
    Pipeline V8 — multidimensional adaptive homeostasis.

    Two tension dimensions:
        - cognitive
        - affective

    Each with:
        - its own threshold
        - its own regulation sensitivity
        - its own adaptive dynamics
    """

    def __init__(self) -> None:
        self.system = build_system()

        # Field tensions
        self.tension_cognitive = 0
        self.tension_affective = 0

        # Adaptive thresholds
        self.threshold_cognitive = 1
        self.threshold_affective = 1

        # Meniscus sensitivities
        self.sensitivity_cognitive = 1
        self.sensitivity_affective = 1

        # Accumulated regulation
        self.regulation_cognitive = 0
        self.regulation_affective = 0

    def run(self, data: Dict[str, Any], steps: int = 5) -> Dict[str, Any]:
        """
        Execute N multidimensional adaptive homeostatic cycles.
        """

        history: List[Dict[str, Any]] = []

        for _ in range(steps):
            # Step 1: Field increases both tensions
            self.tension_cognitive += 1
            self.tension_affective += 1

            # Step 2: Meniscus regulates each dimension separately
            reg_cog = -1 * self.sensitivity_cognitive if self.tension_cognitive > self.threshold_cognitive else 0
            reg_aff = -1 * self.sensitivity_affective if self.tension_affective > self.threshold_affective else 0

            self.regulation_cognitive += reg_cog
            self.regulation_affective += reg_aff

            # Step 3: Field applies regulation
            self.tension_cognitive += reg_cog
            self.tension_affective += reg_aff

            # Step 4: Adapt thresholds
            if self.tension_cognitive > self.threshold_cognitive:
                self.threshold_cognitive += 1
            else:
                self.threshold_cognitive = max(1, self.threshold_cognitive - 0.1)

            if self.tension_affective > self.threshold_affective:
                self.threshold_affective += 1
            else:
                self.threshold_affective = max(1, self.threshold_affective - 0.1)

            # Step 5: Adapt sensitivities
            if reg_cog != 0:
                self.sensitivity_cognitive += 0.1
            else:
                self.sensitivity_cognitive = max(1, self.sensitivity_cognitive - 0.05)

            if reg_aff != 0:
                self.sensitivity_affective += 0.1
            else:
                self.sensitivity_affective = max(1, self.sensitivity_affective - 0.05)

            # Step 6: Runtime performs a system step
            self.system.runtime.step()

            # Save snapshot
            history.append({
                "tension_cognitive": self.tension_cognitive,
                "tension_affective": self.tension_affective,
                "threshold_cognitive": self.threshold_cognitive,
                "threshold_affective": self.threshold_affective,
                "regulation_cognitive": self.regulation_cognitive,
                "regulation_affective": self.regulation_affective,
                "sensitivity_cognitive": self.sensitivity_cognitive,
                "sensitivity_affective": self.sensitivity_affective,
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
    pipeline = PipelineV8()
    result = pipeline.run({"x": 1}, steps=3)

    assert "history" in result
    assert len(result["history"]) == 3

    print("PipelineV8 self-test passed.")


if __name__ == "__main__":
    _self_test()
