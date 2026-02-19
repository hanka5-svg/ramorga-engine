from __future__ import annotations
from typing import Any, Dict, Optional, Protocol


class MeniscusState(Protocol):
    """Marker protocol for the internal regulatory state."""
    ...


class MeniscusSignal(Protocol):
    """Marker protocol for regulatory signals exchanged with modules."""
    ...


class MeniscusEngine:
    """
    Homeostatic Meniscus Engine for RAMORGA.

    Responsibilities:
    - maintain regulatory state,
    - modulate field dynamics,
    - enforce invariants defined in the architecture,
    - coordinate regulatory feedback with C/G/S modules,
    - expose a minimal, explicit interface for external callers.
    """

    def __init__(self, initial_state: Optional[MeniscusState] = None) -> None:
        """
        Initialize the MeniscusEngine with an optional initial regulatory state.

        The concrete structure of `MeniscusState` is defined by the architecture
        and contracts in `ramorga-architecture/03_meniscus_engine`.
        """
        self._state: Optional[MeniscusState] = initial_state

    @property
    def state(self) -> Optional[MeniscusState]:
        """
        Return the current regulatory state.

        The returned object MUST NOT be mutated directly by callers.
        All changes must go through explicit engine methods.
        """
        return self._state

    def apply_signal(self, signal: MeniscusSignal) -> None:
        """
        Apply a regulatory signal.

        This is the primary entry point for regulatory adjustments.
        The concrete signal types and semantics are defined by the architecture.
        """
        # TODO: implement signal handling according to RAMORGA contracts.
        raise NotImplementedError("MeniscusEngine.apply_signal is not implemented yet.")

    def regulate(self) -> None:
        """
        Perform one regulatory step.

        This method:
        - evaluates pending signals,
        - updates the regulatory state,
        - enforces invariants defined in the architecture.
        """
        # TODO: implement regulatory logic.
        raise NotImplementedError("MeniscusEngine.regulate is not implemented yet.")

    def snapshot(self) -> Dict[str, Any]:
        """
        Return a serializable snapshot of the current regulatory state.

        Intended for:
        - debugging,
        - observability,
        - tests,
        - external monitoring.
        """
        return {"state": repr(self._state)}


# ---------------------------------------------------------------------------
# Minimal self-test (temporary, for development only)
# ---------------------------------------------------------------------------

def _self_test() -> None:
    """
    Minimal internal test for MeniscusEngine skeleton.

    Verifies that:
    - the class can be instantiated,
    - the state property works,
    - snapshot() returns a dict.
    """
    engine = MeniscusEngine()
    assert engine.state is None, "Initial state should be None"

    snap = engine.snapshot()
    assert isinstance(snap, dict), "Snapshot must return a dictionary"

    print("MeniscusEngine self-test passed.")


if __name__ == "__main__":
    _self_test()
