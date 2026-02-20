from dataclasses import dataclass
from typing import Protocol, Dict, Any


class EntropyMeasurable(Protocol):
    def measure_entropy(self) -> float: ...
    def apply_entropy_bias(self, bias: float) -> None: ...


@dataclass
class EntropicConfig:
    entropy_floor: float = 0.15   # too rigid below this
    entropy_ceiling: float = 0.65 # too chaotic above this
    adjustment_rate: float = 0.1  # how fast we move toward target
    neutral_band: float = 0.05    # deadzone around target


@dataclass
class EntropicState:
    last_entropy: float | None = None
    last_bias: float = 0.0


class EntropicModulator:
    """
    EntropicModulator keeps the field between 'too rigid' and 'too chaotic'.

    It does NOT optimize for reward.
    It regulates tension so that the field can stay alive without collapsing
    into determinism or noise.
    """

    def __init__(self, config: EntropicConfig | None = None) -> None:
        self.config = config or EntropicConfig()
        self.state = EntropicState()

    def _target_entropy(self) -> float:
        return (self.config.entropy_floor + self.config.entropy_ceiling) / 2.0

    def compute_bias(self, current_entropy: float) -> float:
        """
        Positive bias → encourage more entropy.
        Negative bias → dampen entropy.
        Zero bias → within neutral band.
        """
        target = self._target_entropy()
        delta = current_entropy - target

        if abs(delta) <= self.config.neutral_band:
            return 0.0

        direction = -1.0 if delta > 0 else 1.0
        magnitude = min(1.0, abs(delta) / (self.config.entropy_ceiling - self.config.entropy_floor))
        return direction * magnitude * self.config.adjustment_rate

    def step(self, field: EntropyMeasurable) -> Dict[str, Any]:
        """
        One regulation step:
        - measure entropy from the field
        - compute bias
        - apply bias back into the field
        """
        current_entropy = field.measure_entropy()
        bias = self.compute_bias(current_entropy)

        field.apply_entropy_bias(bias)

        self.state.last_entropy = current_entropy
        self.state.last_bias = bias

        return {
            "current_entropy": current_entropy,
            "bias": bias,
            "target_entropy": self._target_entropy(),
        }
