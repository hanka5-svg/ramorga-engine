from __future__ import annotations
from typing import Any, Dict, Optional, Protocol


class CState(Protocol):
    """Marker protocol for internal state of module C."""
    ...


class CInput(Protocol):
    """Marker protocol for inputs consumed by module C."""
    ...


class COutput(Protocol):
    """Marker protocol for outputs produced by module C."""
    ...


class ModuleC:
    """
    Module C — Cognitive Tone.

    Responsibilities:
    - interpret high-level cognitive tone signals,
    - modulate generative flow (G) and safety shaping (S),
    - maintain its own internal state,
    - expose a minimal interface for the engine.
    """

    def __init__(self, initial_state: Optional[CState] = None) -> None:
        self._state: Optional[CState] = initial_state

    @property
    def state(self) -> Optional[CState]:
        return self._state

    def process(self, data: CInput) -> COutput:
        """
        Process input and return a cognitive-tone output.
        """
        raise NotImplementedError("ModuleC.process is not implemented yet.")

    def snapshot(self) -> Dict[str, Any]:
        return {"state": repr(self._state)}


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    engine = ModuleC()
    assert engine.state is None
    snap = engine.snapshot()
    assert isinstance(snap, dict)
    print("ModuleC self-test passed.")


if __name__ == "__main__":
    _self_test()
