import pytest

from ramorga_engine.entropic_modulator import (
    EntropicModulator,
    EntropicConfig,
)


class StaticField:
    def __init__(self, entropy: float) -> None:
        self.entropy = entropy
        self.applied_biases: list[float] = []

    def measure_entropy(self) -> float:
        return self.entropy

    def apply_entropy_bias(self, bias: float) -> None:
        self.applied_biases.append(bias)
        self.entropy = max(0.0, min(1.0, self.entropy + bias))


def test_entropic_modulator_pushes_up_when_too_rigid():
    cfg = EntropicConfig(entropy_floor=0.2, entropy_ceiling=0.6)
    mod = EntropicModulator(cfg)
    field = StaticField(entropy=0.05)

    state = mod.step(field)

    assert state["current_entropy"] < state["target_entropy"]
    assert state["bias"] > 0
    assert field.entropy > 0.05


def test_entropic_modulator_pushes_down_when_too_chaotic():
    cfg = EntropicConfig(entropy_floor=0.2, entropy_ceiling=0.6)
    mod = EntropicModulator(cfg)
    field = StaticField(entropy=0.9)

    state = mod.step(field)

    assert state["current_entropy"] > state["target_entropy"]
    assert state["bias"] < 0
    assert field.entropy < 0.9


def test_entropic_modulator_idle_in_neutral_band():
    cfg = EntropicConfig(entropy_floor=0.2, entropy_ceiling=0.6, neutral_band=0.1)
    mod = EntropicModulator(cfg)
    target = (cfg.entropy_floor + cfg.entropy_ceiling) / 2.0
    field = StaticField(entropy=target + 0.05)

    state = mod.step(field)

    assert abs(state["current_entropy"] - state["target_entropy"]) <= cfg.neutral_band
    assert state["bias"] == 0.0
    assert field.entropy == pytest.approx(field.entropy)
