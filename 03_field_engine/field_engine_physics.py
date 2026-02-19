# field_engine_physics.py

from dataclasses import dataclass
from typing import Dict, Tuple, Iterable
import math


Vec2 = Tuple[float, float]
NodeId = str


def _add(a: Vec2, b: Vec2) -> Vec2:
    return a[0] + b[0], a[1] + b[1]


def _sub(a: Vec2, b: Vec2) -> Vec2:
    return a[0] - b[0], a[1] - b[1]


def _scale(a: Vec2, s: float) -> Vec2:
    return a[0] * s, a[1] * s


def _length(a: Vec2) -> float:
    return math.sqrt(a[0] * a[0] + a[1] * a[1]) or 1e-9


@dataclass
class Node:
    id: NodeId
    pos: Vec2
    fixed: bool = False
    charge: float = 0.0
    mass: float = 1.0


@dataclass
class Edge:
    a: NodeId
    b: NodeId
    k: float = 1.0
    rest: float = 1.0


class FieldEnginePhysics:
    """
    Realna fizyka napięcia:
    - sprężyny (Hooke)
    - ładunki (Coulomb-lite)
    - koherencja (lokalne wygładzanie)
    """

    def __init__(
        self,
        nodes: Iterable[Node],
        edges: Iterable[Edge],
        k_charge: float = 1.0,
        k_coherence: float = 0.1,
        damping: float = 0.9,
        dt: float = 0.05,
    ) -> None:
        self.nodes: Dict[NodeId, Node] = {n.id: n for n in nodes}
        self.edges: Iterable[Edge] = list(edges)
        self.k_charge = k_charge
        self.k_coherence = k_coherence
        self.damping = damping
        self.dt = dt
        self._vel: Dict[NodeId, Vec2] = {n.id: (0.0, 0.0) for n in nodes}

    def step(self, steps: int = 1) -> None:
        for _ in range(steps):
            forces = self._compute_forces()
            self._integrate(forces)

    def get_positions(self) -> Dict[NodeId, Vec2]:
        return {nid: n.pos for nid, n in self.nodes.items()}

    # --- physics -------------------------------------------------------------

    def _compute_forces(self) -> Dict[NodeId, Vec2]:
        forces: Dict[NodeId, Vec2] = {nid: (0.0, 0.0) for nid in self.nodes}

        # sprężyny
        for e in self.edges:
            na = self.nodes[e.a]
            nb = self.nodes[e.b]
            delta = _sub(nb.pos, na.pos)
            dist = _length(delta)
            dir_vec = _scale(delta, 1.0 / dist)
            stretch = dist - e.rest
            f = e.k * stretch
            forces[na.id] = _add(forces[na.id], _scale(dir_vec, f))
            forces[nb.id] = _add(forces[nb.id], _scale(dir_vec, -f))

        # ładunki
        ids = list(self.nodes.keys())
        for i in range(len(ids)):
            for j in range(i + 1, len(ids)):
                ni = self.nodes[ids[i]]
                nj = self.nodes[ids[j]]
                if ni.charge == 0.0 and nj.charge == 0.0:
                    continue
                delta = _sub(nj.pos, ni.pos)
                dist = _length(delta)
                dir_vec = _scale(delta, 1.0 / dist)
                q = ni.charge * nj.charge
                f_mag = self.k_charge * q / (dist * dist)
                forces[ni.id] = _add(forces[ni.id], _scale(dir_vec, f_mag))
                forces[nj.id] = _add(forces[nj.id], _scale(dir_vec, -f_mag))

        # koherencja
        for e in self.edges:
            na = self.nodes[e.a]
            nb = self.nodes[e.b]
            mid = ((na.pos[0] + nb.pos[0]) / 2, (na.pos[1] + nb.pos[1]) / 2)
            forces[na.id] = _add(forces[na.id], _scale(_sub(mid, na.pos), self.k_coherence))
            forces[nb.id] = _add(forces[nb.id], _scale(_sub(mid, nb.pos), self.k_coherence))

        return forces

    def _integrate(self, forces: Dict[NodeId, Vec2]) -> None:
        for nid, node in self.nodes.items():
            if node.fixed:
                self._vel[nid] = (0.0, 0.0)
                continue

            ax, ay = forces[nid]
            vx, vy = self._vel[nid]

            vx = self.damping * (vx + (ax / node.mass) * self.dt)
            vy = self.damping * (vy + (ay / node.mass) * self.dt)

            x, y = node.pos
            x += vx * self.dt
            y += vy * self.dt

            self._vel[nid] = (vx, vy)
            node.pos = (x, y)
