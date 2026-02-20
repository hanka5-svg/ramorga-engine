# field_state.py

from __future__ import annotations
from typing import Dict, Any, Tuple
import math


Vec2 = Tuple[float, float]


def _sub(a: Vec2, b: Vec2) -> Vec2:
    return a[0] - b[0], a[1] - b[1]


def _length(a: Vec2) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1]) or 1e-9


class FieldState:
    """
    FieldState v2 — enriched field representation.

    Stores:
    - node positions,
    - local tension,
    - spatial gradients,
    - total field energy.

    This class does not perform physics. It only interprets the
    positions provided by the physics backend.
    """

    def __init__(self) -> None:
        self._positions: Dict[str, Vec2] = {}
        self._neighbors: Dict[str, set[str]] = {}
        self._tension: Dict[str, float] = {}
        self._gradient: Dict[str, Vec2] = {}
        self._energy: float = 0.0

    # ------------------------------------------------------------------

    def set_neighbors(self, adjacency: Dict[str, set[str]]) -> None:
        """
        Provide adjacency information (node -> neighbors).
        Required for tension and gradient computation.
        """
        self._neighbors = adjacency

    # ------------------------------------------------------------------

    def update_from_positions(self, positions: Dict[str, Vec2]) -> None:
        """
        Update positions and recompute derived quantities.
        """
        self._positions = dict(positions)
        self._compute_tension()
        self._compute_gradient()
        self._compute_energy()

    # ------------------------------------------------------------------
    # Derived quantities
    # ------------------------------------------------------------------

    def _compute_tension(self) -> None:
        """
        Local tension = mean distance to neighbors.
        """
        tension: Dict[str, float] = {}

        for nid, pos in self._positions.items():
            neigh = self._neighbors.get(nid, set())
            if not neigh:
                tension[nid] = 0.0
                continue

            distances = [
                _length(_sub(self._positions[nid], self._positions[nj]))
                for nj in neigh
                if nj in self._positions
            ]
            tension[nid] = sum(distances) / len(distances)

        self._tension = tension

    # ------------------------------------------------------------------

    def _compute_gradient(self) -> None:
        """
        Gradient = vector sum of neighbor differences.
        """
        gradient: Dict[str, Vec2] = {}

        for nid, pos in self._positions.items():
            neigh = self._neighbors.get(nid, set())
            if not neigh:
                gradient[nid] = (0.0, 0.0)
                continue

            gx = 0.0
            gy = 0.0
            for nj in neigh:
                if nj not in self._positions:
                    continue
                dx, dy = _sub(self._positions[nj], pos)
                gx += dx
                gy += dy

            gradient[nid] = (gx, gy)

        self._gradient = gradient

    # ------------------------------------------------------------------

    def _compute_energy(self) -> None:
        """
        Field energy = sum of local tension magnitudes.
        (Simple model; can be extended.)
        """
        self._energy = sum(self._tension.values())

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def get_positions(self) -> Dict[str, Vec2]:
        return dict(self._positions)

    def get_tension(self) -> Dict[str, float]:
        return dict(self._tension)

    def get_gradient(self) -> Dict[str, Vec2]:
        return dict(self._gradient)

    def get_energy(self) -> float:
        return float(self._energy)

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"FieldState(nodes={len(self._positions)}, "
            f"energy={self._energy:.3f})"
        )
