from __future__ import annotations
from typing import Any, Dict, List
import math

from integration import build_system


class PipelineV10:
    """
    Pipeline V10 — nonlinear multidimensional homeostasis.

    Nonlinearities:
        - sigmoidal tension growth
        - exponential regulation strength
        - tanh-based adaptive thresholds
        - tanh-based adaptive sensitivities
    """

    def __init__(self) -> None:
        self.system = build_system()

        # Field tensions
        self.tension_cognitive = 0.0
        self.tension_affective = 0.0

        # Adaptive thresholds
        self.threshold_cognitive = 1.0
        self.threshold_affective = 1.0

        # Meniscus sensitivities
        self.sensitivity_cognitive = 1.0
        self.sensitivity_affective = 1.0

        # Accumulated regulation
        self.regulation_cognitive = 0.0
        self.regulation_affective = 0.0

    def _sigmoid(self, x: float) -> float:
        return 1 / (1 + math.exp(-x))

    def run(self, data: Dict[str, Any], steps: int = 5) -> Dict[str, Any]:
        """
        Execute N nonlinear homeostatic cycles.
        """

        history: List[Dict[str, Any]] = []

        for _ in range(steps):
            # Step 1: Nonlinear tension growth (sigmoidal saturation)
            self.tension_cognitive += 1 * (1 - self._sigmoid(self.tension_cognitive))
            self.tension_affective += 1 * (1 - self._sigmoid(self.tension_affective))

            # Step 2: Cross-coupling (same as V9)
            self.tension_cognitive += 0.2 * self.tension_affective
            self.tension_affective += 0.2 * self.tension_cognitive

            # Step 3: Nonlinear regulation (exponential)
            reg_cog = -math.exp(self.sensitivity_cognitive) if self.tension_cognitive > self.threshold_cognitive else 0
            reg_aff = -math.exp(self.sensitivity_affective) if self.tension_affective > self.threshold_affective else 0

            # Step 4: Cross-coupling of regulation
            reg_cog += -0.1 * reg_aff
            reg_aff += -0.1 * reg_cog

            self.regulation_cognitive += reg_cog
            self.regulation_affective += reg_aff

            # Step 5: Apply regulation
            self.tension_cognitive += reg_cog
            self.tension_affective += reg_aff

            # Step 6: Nonlinear threshold adaptation (tanh)
            self.threshold_cognitive += 0.2 * math.tanh(self.tension_cognitive - self.threshold_cognitive)
            self.threshold_affective += 0.2 * math.tanh(self.tension_affective - self.threshold_affective)

            # Step 7: Nonlinear sensitivity adaptation (tanh)
            self.sensitivity_cognitive += 0.05 * math.tanh(abs(reg_cog))
            self.sensitivity_affective += 0.05 * math.tanh(abs(reg_aff))

            # Step 8: Runtime step
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
    pipeline = PipelineV10()
    result = pipeline.run({"x": 1}, steps=3)

    assert "history" in result
    assert len(result["history"]) == 3

    print("PipelineV10 self-test passed.")


if __name__ == "__main__":
    _self_test()
