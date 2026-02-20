# field_state.py

from __future__ import annotations
from typing import Dict, Any, Tuple, Set
import math


Vec2 = Tuple[float, float]


def _sub(a: Vec2, b: Vec2) -> Vec2:
    return a[0] - b[0], a[1] - b[1]


def _length(a: Vec2) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1]) or 1e-9


class FieldState:
    """
    FieldState v3 — structural + energetic field representation.

    Stores:
    - node positions,
    - local tension (mean neighbor distance),
    - spatial gradients,
    - elastic energy (springs),
    - charge energy (Coulomb-like),
    - tension map (per-node energy contribution).

    This class does not perform physics. It interprets positions
    and adjacency provided by the physics backend.
    """

    def __init__(self) -> None:
        self._positions: Dict[str, Vec2] = {}
        self._neighbors: Dict[str, Set[str]] = {}
        self._rest_lengths: Dict[Tuple[str, str], float] = {}
        self._charges: Dict[str, float] = {}

        self._tension: Dict[str, float] = {}
        self._gradient: Dict[str, Vec2] = {}
        self._elastic_energy: float = 0.0
        self._charge_energy: float = 0.0
        self._tension_map: Dict[str, float] = {}

    # ------------------------------------------------------------------
    # Configuration
    # ------------------------------------------------------------------

    def set_neighbors(
        self,
        adjacency: Dict[str, Set[str]],
        rest_lengths: Dict[Tuple[str, str], float],
        charges: Dict[str, float],
    ) -> None:
        """
        Provide adjacency, rest lengths and charges.
        Required for energy computation.
        """
        self._neighbors = adjacency
        self._rest_lengths = rest_lengths
        self._charges = charges

    # ------------------------------------------------------------------

    def update_from_positions(self, positions: Dict[str, Vec2]) -> None:
        """
        Update positions and recompute all derived quantities.
        """
        self._positions = dict(positions)
        self._compute_tension()
        self._compute_gradient()
        self._compute_elastic_energy()
        self._compute_charge_energy()
        self._compute_tension_map()

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
                _length(_sub(pos, self._positions[nj]))
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

    def _compute_elastic_energy(self) -> None:
        """
        Elastic energy = sum( 0.5 * (dist - rest)^2 ) over edges.
        """
        total = 0.0

        for (a, b), rest in self._rest_lengths.items():
            if a not in self._positions or b not in self._positions:
                continue

            dist = _length(_sub(self._positions[a], self._positions[b]))
            stretch = dist - rest
            total += 0.5 * (stretch * stretch)

        self._elastic_energy = total

    # ------------------------------------------------------------------

    def _compute_charge_energy(self) -> None:
        """
        Charge energy = sum( q_i * q_j / dist ) over all pairs.
        """
        total = 0.0
        ids = list(self._positions.keys())

        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                a = ids[i]
                b = ids[j]
                if a not in self._charges or b not in self._charges:
                    continue

                q = self._charges[a] * self._charges[b]
                dist = _length(_sub(self._positions[a], self._positions[b]))
                total += q / dist

        self._charge_energy = total

    # ------------------------------------------------------------------

    def _compute_tension_map(self) -> None:
        """
        Per-node energy contribution = tension + gradient magnitude.
        """
        tension_map: Dict[str, float] = {}

        for nid in self._positions:
            t = self._tension.get(nid, 0.0)
            gx, gy = self._gradient.get(nid, (0.0, 0.0))
            gmag = math.sqrt(gx * gx + gy * gy)
            tension_map[nid] = t + gmag

        self._tension_map = tension_map

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def get_positions(self) -> Dict[str, Vec2]:
        return dict(self._positions)

    def get_tension(self) -> Dict[str, float]:
        return dict(self._tension)

    def get_gradient(self) -> Dict[str, Vec2]:
        return dict(self._gradient)

    def get_elastic_energy(self) -> float:
        return float(self._elastic_energy)

    def get_charge_energy(self) -> float:
        return float(self._charge_energy)

    def get_tension_map(self) -> Dict[str, float]:
        return dict(self._tension_map)

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"FieldState(nodes={len(self._positions)}, "
            f"E_elastic={self._elastic_energy:.3f}, "
            f"E_charge={self._charge_energy:.3f})"
        )
