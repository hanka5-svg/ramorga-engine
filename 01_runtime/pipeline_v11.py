from __future__ import annotations
from typing import Any, Dict, List
import math

from integration import build_system


class PipelineV11:
    """
    Pipeline V11 — meta-regulation (regulation of regulation).

    New elements:
        - Meniscus regulates its own sensitivity (meta-level)
        - Field influences meta-stability
        - Meta-parameters adapt based on system dynamics
    """

    def __init__(self) -> None:
        self.system = build_system()

        # Field tensions
        self.tension_cognitive = 0.0
        self.tension_affective = 0.0

        # Thresholds
        self.threshold_cognitive = 1.0
        self.threshold_affective = 1.0

        # Sensitivities
        self.sensitivity_cognitive = 1.0
        self.sensitivity_affective = 1.0

        # Regulation accumulators
        self.regulation_cognitive = 0.0
        self.regulation_affective = 0.0

        # Meta-regulation parameters
        self.meta_stability = 1.0
        self.meta_gain = 0.1
        self.meta_damping = 0.05

    def _sigmoid(self, x: float) -> float:
        return 1 / (1 + math.exp(-x))

    def run(self, data: Dict[str, Any], steps: int = 5) -> Dict[str, Any]:
        history: List[Dict[str, Any]] = []

        for _ in range(steps):
            # Step 1: Nonlinear tension growth
            self.tension_cognitive += 1 * (1 - self._sigmoid(self.tension_cognitive))
            self.tension_affective += 1 * (1 - self._sigmoid(self.tension_affective))

            # Step 2: Cross-coupling
            self.tension_cognitive += 0.2 * self.tension_affective
            self.tension_affective += 0.2 * self.tension_cognitive

            # Step 3: Regulation (exponential)
            reg_cog = -math.exp(self.sensitivity_cognitive) if self.tension_cognitive > self.threshold_cognitive else 0
            reg_aff = -math.exp(self.sensitivity_affective) if self.tension_affective > self.threshold_affective else 0

            # Step 4: Cross-coupling of regulation
            reg_cog += -0.1 * reg_aff
            reg_aff += -0.1 * reg_cog

            # Step 5: Apply regulation
            self.tension_cognitive += reg_cog
            self.tension_affective += reg_aff

            self.regulation_cognitive += reg_cog
            self.regulation_affective += reg_aff

            # Step 6: Meta-regulation (regulation of regulation)
            regulation_magnitude = abs(reg_cog) + abs(reg_aff)

            # Meta-stability increases when regulation is chaotic
            self.meta_stability += 0.05 * math.tanh(regulation_magnitude)

            # Meta-gain adapts based on tension divergence
            divergence = abs(self.tension_cognitive - self.tension_affective)
            self.meta_gain += 0.02 * math.tanh(divergence)

            # Meta-damping increases when regulation overshoots
            overshoot = max(0, regulation_magnitude - 5)
            self.meta_damping += 0.01 * math.tanh(overshoot)

            # Step 7: Apply meta-regulation to sensitivities
            self.sensitivity_cognitive += self.meta_gain * math.tanh(abs(reg_cog)) - self.meta_damping
            self.sensitivity_affective += self.meta_gain * math.tanh(abs(reg_aff)) - self.meta_damping

            # Ensure sensitivities stay above 1
            self.sensitivity_cognitive = max(1.0, self.sensitivity_cognitive)
            self.sensitivity_affective = max(1.0, self.sensitivity_affective)

            # Step 8: Threshold adaptation
            self.threshold_cognitive += 0.2 * math.tanh(self.tension_cognitive - self.threshold_cognitive)
            self.threshold_affective += 0.2 * math.tanh(self.tension_affective - self.threshold_affective)

            # Step 9: Runtime step
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
                "meta_stability": self.meta_stability,
                "meta_gain": self.meta_gain,
                "meta_damping": self.meta_damping,
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
    pipeline = PipelineV11()
    result = pipeline.run({"x": 1}, steps=3)

    assert "history" in result
    assert len(result["history"]) == 3

    print("PipelineV11 self-test passed.")


if __name__ == "__main__":
    _self_test()
