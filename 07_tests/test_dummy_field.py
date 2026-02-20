import random


class DummyField:
    def __init__(self) -> None:
        self._entropy = 0.3
        self._history: list[float] = []

    def measure_entropy(self) -> float:
        # in real engine this would be derived from distribution of responses / states
        noise = random.uniform(-0.02, 0.02)
        value = max(0.0, min(1.0, self._entropy + noise))
        self._history.append(value)
        return value

    def apply_entropy_bias(self, bias: float) -> None:
        # positive bias → push entropy up, negative → down
        self._entropy = max(0.0, min(1.0, self._entropy + bias))

    @property
    def history(self) -> list[float]:
        return self._history
