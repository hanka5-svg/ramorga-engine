# field_state.py

from __future__ import annotations
from typing import Dict, Any


class FieldState:
    """
    Minimal, explicit representation of the field state.

    Responsibilities:
    - store high-level field representation,
    - accept updates from physics backend,
    - expose stable interface for pipelines and modules.
    """

    def __init__(self) -> None:
        # canonical representation: node_id -> position (x, y)
        self._positions: Dict[str, Any] = {}

    # ------------------------------------------------------------------

    def update_from_positions(self, positions: Dict[str, Any]) -> None:
        """
        Update the field state using positions provided by the physics backend.
        """
        self._positions = dict(positions)

    # ------------------------------------------------------------------

    def get_positions(self) -> Dict[str, Any]:
        """
        Expose the current field positions.
        """
        return dict(self._positions)

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return f"FieldState(nodes={len(self._positions)})"
