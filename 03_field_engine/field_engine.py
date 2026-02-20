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

# --- Integration with FieldEnginePhysics ------------------------------------

from .field_engine_physics import (
    FieldEnginePhysics,
    Node,
    Edge,
)

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
        self._state: Optional[FieldState] = initial_state
        self._physics: Optional[FieldEnginePhysics] = None

    # ----------------------------------------------------------------------

    def attach_physics(
        self,
        nodes: Iterable[Node],
        edges: Iterable[Edge],
        *,
        k_charge: float = 1.0,
        k_coherence: float = 0.1,
        damping: float = 0.9,
        dt: float = 0.05,
    ) -> None:
        """
        Attach a concrete physics backend to the FieldEngine.

        This keeps the architectural interface clean while allowing
        real tension dynamics to run underneath.
        """
        self._physics = FieldEnginePhysics(
            nodes=nodes,
            edges=edges,
            k_charge=k_charge,
            k_coherence=k_coherence,
            damping=damping,
            dt=dt,
        )

    # ----------------------------------------------------------------------

    def step(self, steps: int = 1) -> None:
        """
        Advance the field by a number of physics steps.
        """
        if self._physics is None:
            raise RuntimeError("Physics backend not attached.")

        self._physics.step(steps)

        # update high-level FieldState if present
        if self._state is not None:
            self._state.update_from_positions(self._physics.get_positions())

    # ----------------------------------------------------------------------

    def get_positions(self) -> Dict[str, Any]:
        """
        Expose node positions from the physics backend.
        """
        if self._physics is None:
            return {}
        return self._physics.get_positions()
