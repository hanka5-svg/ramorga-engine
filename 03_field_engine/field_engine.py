from __future__ import annotations
from typing import Any, Dict, Optional, Protocol


class FieldEvent(Protocol):
    """Marker protocol for events processed by the FieldEngine."""
    ...


class FieldState(Protocol):
    """Marker protocol for field state representation."""
    ...


class FieldEngine:
    """
    Core engine for RAMORGA field dynamics.

    Responsibilities:
    - maintain internal representation of the field state,
    - propagate changes through the field,
    - integrate tension loops,
    - coordinate interactions with C/G/S modules and Meniscus,
    - expose a minimal, explicit interface for external callers.
    """

    def __init__(self, initial_state: Optional[FieldState] = None) -> None:
        """
        Initialize the FieldEngine with an optional initial field state.

        The concrete structure of `FieldState` is defined by the architecture
        and contracts in `ramorga-architecture/02_field_engine`.
        """
        self._state: Optional[FieldState] = initial_state

    @property
    def state(self) -> Optional[FieldState]:
        """
        Return the current field state.

        The returned object MUST NOT be mutated in-place by callers.
        Any change to the field MUST go through explicit engine methods.
        """
        return self._state

    def apply_event(self, event: FieldEvent) -> None:
        """
        Apply a single event to the field.

        This method is the primary entry point for changing the field.
        The concrete event types and their semantics are defined by
        the architecture and module contracts.
        """
        # TODO: implement event handling according to RAMORGA contracts.
        raise NotImplementedError("FieldEngine.apply_event is not implemented yet.")

    def propagate(self) -> None:
        """
        Propagate field changes and update internal state.

        This method performs one propagation step:
        - evaluates pending changes,
        - updates the field state,
        - enforces invariants defined in the architecture.
        """
        # TODO: implement propagation logic.
        raise NotImplementedError("FieldEngine.propagate is not implemented yet.")

    def snapshot(self) -> Dict[str, Any]:
        """
        Return a serializable snapshot of the current field state.

        This is intended for:
        - debugging,
        - observability,
        - tests,
        - external monitoring.

        The exact structure is defined by the architecture layer.
        """
        # TODO: return a meaningful snapshot of the field state.
        return {"state": repr(self._state)}
