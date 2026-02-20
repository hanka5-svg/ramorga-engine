# field_state.py

from __future__ import annotations
from typing import Dict, Any, Tuple, Set
import math


Vec2 = Tuple[float, float]


def _sub(a: Vec2, b: Vec2) -> Vec2:
    return a[0] - b[0], a[1] - b[1]


def _add(a: Vec2, b: Vec2) -> Vec2:
    return a[0] + b[0], a[1] + b[1]


def _scale(a: Vec2, s: float) -> Vec2:
    return a[0] * s, a[1] * s


def _length(a: Vec2) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1]) or 1e-9


class FieldState:
    """
    FieldState v6 — full structural + energetic + differential representation.

    Zawiera:
    - pozycje węzłów,
    - lokalne napięcie,
    - gradient pola,
    - energia sprężysta,
    - energia ładunków,
    - mapa napięć,
    - energie kierunkowe (v4),
    - krzywizna pola (v5),
    - divergence i curl (v6).

    FieldState NIE wykonuje fizyki — tylko interpretuje dane z backendu.
    """

    def __init__(self) -> None:
        self._positions: Dict[str, Vec2] = {}
        self._neighbors: Dict[str, Set[str]] = {}
        self._rest_lengths: Dict[Tuple[str, str], float] = {}
        self._charges: Dict[str, float] = {}

        # podstawowe metryki
        self._tension: Dict[str, float] = {}
        self._gradient: Dict[str, Vec2] = {}
        self._elastic_energy: float = 0.0
        self._charge_energy: float = 0.0
        self._tension_map: Dict[str, float] = {}

        # v4
        self._directional_energy: Dict[str, float] = {}

        # v5
        self._curvature: Dict[str, float] = {}

        # v6
        self._divergence: Dict[str, float] = {}
        self._curl: Dict[str, float] = {}

    # ------------------------------------------------------------------
    # Konfiguracja
    # ------------------------------------------------------------------

    def set_neighbors(
        self,
        adjacency: Dict[str, Set[str]],
        rest_lengths: Dict[Tuple[str, str], float],
        charges: Dict[str, float],
    ) -> None:
        self._neighbors = adjacency
        self._rest_lengths = rest_lengths
        self._charges = charges

    # ------------------------------------------------------------------

    def update_from_positions(self, positions: Dict[str, Vec2]) -> None:
        self._positions = dict(positions)

        self._compute_tension()
        self._compute_gradient()
        self._compute_elastic_energy()
        self._compute_charge_energy()
        self._compute_tension_map()

        # v4
        self._compute_directional_energy()

        # v5
        self._compute_curvature()

        # v6
        self._compute_divergence()
        self._compute_curl()

    # ------------------------------------------------------------------
    # v1–v3: podstawowe metryki
    # ------------------------------------------------------------------

    def _compute_tension(self) -> None:
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
        tension_map: Dict[str, float] = {}

        for nid in self._positions:
            t = self._tension.get(nid, 0.0)
            gx, gy = self._gradient.get(nid, (0.0, 0.0))
            gmag = math.sqrt(gx * gx + gy * gy)
            tension_map[nid] = t + gmag

        self._tension_map = tension_map

    # ------------------------------------------------------------------
    # v4: energie kierunkowe
    # ------------------------------------------------------------------

    def _compute_directional_energy(self) -> None:
        """
        Energia kierunkowa = suma kwadratów projekcji gradientu na wektory do sąsiadów.
        """
        de: Dict[str, float] = {}

        for nid, pos in self._positions.items():
            neigh = self._neighbors.get(nid, set())
            if not neigh:
                de[nid] = 0.0
                continue

            gx, gy = self._gradient.get(nid, (0.0, 0.0))
            total = 0.0

            for nj in neigh:
                if nj not in self._positions:
                    continue
                dx, dy = _sub(self._positions[nj], pos)
                dist = _length((dx, dy))
                ux, uy = dx / dist, dy / dist
                proj = gx * ux + gy * uy
                total += proj * proj

            de[nid] = total

        self._directional_energy = de

    # ------------------------------------------------------------------
    # v5: krzywizna pola
    # ------------------------------------------------------------------

    def _compute_curvature(self) -> None:
        """
        Krzywizna = różnica między gradientem a średnim gradientem sąsiadów.
        """
        curv: Dict[str, float] = {}

        for nid, pos in self._positions.items():
            neigh = self._neighbors.get(nid, set())
            if not neigh:
                curv[nid] = 0.0
                continue

            gx, gy = self._gradient.get(nid, (0.0, 0.0))

            avgx = 0.0
            avgy = 0.0
            count = 0

            for nj in neigh:
                if nj not in self._gradient:
                    continue
                ngx, ngy = self._gradient[nj]
                avgx += ngx
                avgy += ngy
                count += 1

            if count == 0:
                curv[nid] = 0.0
                continue

            avgx /= count
            avgy /= count

            dx = gx - avgx
            dy = gy - avgy
            curv[nid] = math.sqrt(dx * dx + dy * dy)

        self._curvature = curv

    # ------------------------------------------------------------------
    # v6: divergence i curl
    # ------------------------------------------------------------------

    def _compute_divergence(self) -> None:
        """
        Divergence = suma różnic gradientu w kierunku sąsiadów.
        """
        div: Dict[str, float] = {}

        for nid, pos in self._positions.items():
            neigh = self._neighbors.get(nid, set())
            if not neigh:
                div[nid] = 0.0
                continue

            gx, gy = self._gradient.get(nid, (0.0, 0.0))
            total = 0.0

            for nj in neigh:
                if nj not in self._gradient:
                    continue
                ngx, ngy = self._gradient[nj]
                total += (ngx - gx) + (ngy - gy)

            div[nid] = total

        self._divergence = div

    # ------------------------------------------------------------------

    def _compute_curl(self) -> None:
        """
        Curl = suma rotacji lokalnych (gx*dy - gy*dx).
        """
        curl: Dict[str, float] = {}

        for nid, pos in self._positions.items():
            neigh = self._neighbors.get(nid, set())
            if not neigh:
                curl[nid] = 0.0
                continue

            gx, gy = self._gradient.get(nid, (0.0, 0.0))
            total = 0.0

            for nj in neigh:
                if nj not in self._positions:
                    continue
                dx, dy = _sub(self._positions[nj], pos)
                total += gx * dy - gy * dx

            curl[nid] = total

        self._curl = curl

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

    def get_directional_energy(self) -> Dict[str, float]:
        return dict(self._directional_energy)

    def get_curvature(self) -> Dict[str, float]:
        return dict(self._curvature)

    def get_divergence(self) -> Dict[str, float]:
        return dict(self._divergence)

    def get_curl(self) -> Dict[str, float]:
        return dict(self._curl)

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"FieldState(nodes={len(self._positions)}, "
            f"E_elastic={self._elastic_energy:.3f}, "
            f"E_charge={self._charge_energy:.3f})"
        )
