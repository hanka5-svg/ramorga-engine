from __future__ import annotations
from typing import Any, Dict, Optional, Protocol


class SState(Protocol):
    """Marker protocol for internal state of module S."""
    ...


class SInput(Protocol):
    """Marker protocol for inputs consumed by module S."""
    ...


class SOutput(Protocol):
    """Marker protocol for outputs produced by module S."""
    ...


class ModuleS:
    """
    Module S — Shape / Safety.

    Responsibilities:
    - enforce safety shaping on generative flow,
    - integrate regulatory signals from Meniscus,
    - maintain internal safety state,
    - expose a minimal interface for the engine.
    """

    def __init__(self, initial_state: Optional[SState] = None) -> None:
        self._state: Optional[SState] = initial_state

    @property
    def state(self) -> Optional[SState]:
        return self._state

    def process(self, data: SInput) -> SOutput:
        """
        Process input and return a safety-shaped output.
        """
        raise NotImplementedError("ModuleS.process is not implemented yet.")

    def snapshot(self) -> Dict[str, Any]:
        return {"state": repr(self._state)}


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    engine = ModuleS()
    assert engine.state is None
    snap = engine.snapshot()
    assert isinstance(snap, dict)
    print("ModuleS self-test passed.")


if __name__ == "__main__":
    _self_test()
