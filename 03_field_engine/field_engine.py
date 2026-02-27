from __future__ import annotations
from typing import Any, Dict, Optional, Protocol, Iterable

from .field_engine_physics import (
    FieldEnginePhysics,
    Node,
    Edge,
)


# ----------------------------------------------------------------------
# Architectural Protocols
# ----------------------------------------------------------------------

class FieldEvent(Protocol):
    """Marker protocol for events processed by the FieldEngine."""
    ...


class FieldState(Protocol):
    """Marker protocol for field state representation."""
    def update_from_positions(self, positions: Dict[str, Any]) -> None:
        ...


# ----------------------------------------------------------------------
# FieldEngine Implementation
# ----------------------------------------------------------------------

class FieldEngine:
    """
    Core engine for RAMORGA field dynamics.

    Responsibilities:
    - maintain internal representation of the field state,
    - propagate changes through the field,
    - integrate physics backend,
    - enforce architectural invariants,
    - expose a minimal, explicit interface for external callers.
    """

    def __init__(self, initial_state: Optional[FieldState] = None) -> None:
        self._state: Optional[FieldState] = initial_state
        self._physics: Optional[FieldEnginePhysics] = None

    # ------------------------------------------------------------------

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
        """
        self._physics = FieldEnginePhysics(
            nodes=nodes,
            edges=edges,
            k_charge=k_charge,
            k_coherence=k_coherence,
            damping=damping,
            dt=dt,
        )

    # ------------------------------------------------------------------

    def step(self, steps: int = 1) -> None:
        """
        Advance the field by a number of physics steps.
        """
        if self._physics is None:
            raise RuntimeError("Physics backend not attached.")

        self._physics.step(steps)

        if self._state is not None:
            self._state.update_from_positions(self._physics.get_positions())

    # ------------------------------------------------------------------

    def get_positions(self) -> Dict[str, Any]:
        """
        Expose node positions from the physics backend.
        """
        if self._physics is None:
            return {}
        return self._physics.get_positions()
