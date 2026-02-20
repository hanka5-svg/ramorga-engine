# tension_loop.py

from __future__ import annotations
from typing import Optional, Dict

from .field_engine_physics import FieldEnginePhysics
from .field_state import FieldState


class TensionLoop:
    """
    TensionLoop v5 — pełna homeostaza RAMORGA.

    Zawiera:
    - v2: lokalne sprzężenia zwrotne,
    - v3: regulacja kierunkowa,
    - v4: stabilizacja gradientowa,
    - v5: homeostaza (lokalna + globalna).

    Pętla:
        physics → state → regulation → homeostasis → feedback
    """

    def __init__(self) -> None:
        self._physics: Optional[FieldEnginePhysics] = None
        self._state: Optional[FieldState] = None

        self._feedback_map: Dict[str, float] = {}
        self._directional_feedback: Dict[str, float] = {}
        self._stabilization_map: Dict[str, float] = {}
        self._homeostasis_map: Dict[str, float] = {}

        self._global_tension: float = 0.0
        self._global_energy: float = 0.0

    # ------------------------------------------------------------------
    # Podpinanie backendów
    # ------------------------------------------------------------------

    def attach(self, physics: FieldEnginePhysics, state: FieldState) -> None:
        self._physics = physics
        self._state = state

    # ------------------------------------------------------------------
    # Główna pętla
    # ------------------------------------------------------------------

    def step(self) -> None:
        if self._physics is None or self._state is None:
            raise RuntimeError("TensionLoop not attached.")

        # 1) Pobierz pozycje z fizyki
        positions = self._physics.get_positions()

        # 2) Zaktualizuj stan pola
        self._state.update_from_positions(positions)

        # 3) Regulacje v2, v3, v4
        self._apply_local_feedback()          # v2
        self._apply_directional_regulation()  # v3
        self._apply_gradient_stabilization()  # v4

        # 4) Homeostaza v5
        self._apply_homeostasis()

    # ------------------------------------------------------------------
    # v2: lokalne sprzężenia zwrotne
    # ------------------------------------------------------------------

    def _apply_local_feedback(self) -> None:
        tension = self._state.get_tension()
        curvature = self._state.get_curvature()
        directional = self._state.get_directional_energy()
        neighbors = self._state._neighbors

        feedback: Dict[str, float] = {}

        w1 = 1.0   # napięcie
        w2 = 0.7   # krzywizna
        w3 = 0.5   # energia kierunkowa
        w4 = 1.2   # różnica napięcia z sąsiadami

        for nid in tension:
            t = tension.get(nid, 0.0)
            c = curvature.get(nid, 0.0)
            d = directional.get(nid, 0.0)

            neigh = neighbors.get(nid, set())
            if neigh:
                neigh_t = [tension.get(nj, 0.0) for nj in neigh]
                mean_neigh = sum(neigh_t) / len(neigh_t)
            else:
                mean_neigh = 0.0

            diff = t - mean_neigh

            feedback[nid] = (
                w1 * t +
                w2 * c +
                w3 * d +
                w4 * diff
            )

        self._feedback_map = feedback

        if feedback:
            self._global_tension = sum(feedback.values()) / len(feedback)
        else:
            self._global_tension = 0.0

    # ------------------------------------------------------------------
    # v3: regulacja kierunkowa
    # ------------------------------------------------------------------

    def _apply_directional_regulation(self) -> None:
        gradient = self._state.get_gradient()
        neighbors = self._state._neighbors

        directional_feedback: Dict[str, float] = {}

        w_dir = 0.8

        for nid, (gx, gy) in gradient.items():
            neigh = neighbors.get(nid, set())
            if not neigh:
                directional_feedback[nid] = 0.0
                continue

            total = 0.0
            for nj in neigh:
                if nj not in self._state.get_positions():
                    continue

                dx, dy = (
                    self._state.get_positions()[nj][0] - self._state.get_positions()[nid][0],
                    self._state.get_positions()[nj][1] - self._state.get_positions()[nid][1],
                )

                align = gx * dx + gy * dy
                total += align

            directional_feedback[nid] = w_dir * total

        self._directional_feedback = directional_feedback

    # ------------------------------------------------------------------
    # v4: stabilizacja gradientowa
    # ------------------------------------------------------------------

    def _apply_gradient_stabilization(self) -> None:
        gradient = self._state.get_gradient()
        neighbors = self._state._neighbors

        stabilization: Dict[str, float] = {}

        w_stab = 0.6

        for nid, (gx, gy) in gradient.items():
            neigh = neighbors.get(nid, set())
            if not neigh:
                stabilization[nid] = 0.0
                continue

            avgx = 0.0
            avgy = 0.0
            count = 0

            for nj in neigh:
                if nj not in gradient:
                    continue
                ngx, ngy = gradient[nj]
                avgx += ngx
                avgy += ngy
                count += 1

            if count == 0:
                stabilization[nid] = 0.0
                continue

            avgx /= count
            avgy /= count

            dx = gx - avgx
            dy = gy - avgy

            stabilization[nid] = -w_stab * (dx * dx + dy * dy)

        self._stabilization_map = stabilization

    # ------------------------------------------------------------------
    # v5: pełna homeostaza RAMORGA
    # ------------------------------------------------------------------

    def _apply_homeostasis(self) -> None:
        """
        Homeostaza:
        - kompensacja globalna,
        - autoregulacja lokalna,
        - tłumienie oscylacji,
        - stabilizacja energii.
        """

        tension_map = self._feedback_map
        directional = self._directional_feedback
        stabilization = self._stabilization_map

        homeo: Dict[str, float] = {}

        # globalna energia pola
        E_el = self._state.get_elastic_energy()
        E_ch = self._state.get_charge_energy()
        self._global_energy = E_el + E_ch

        # wagi homeostazy
        w_local = 1.0
        w_dir = 0.6
        w_stab = 0.8
        w_energy = 0.4

        for nid in tension_map:
            local = tension_map.get(nid, 0.0)
            dreg = directional.get(nid, 0.0)
            stab = stabilization.get(nid, 0.0)

            homeo[nid] = (
                w_local * local +
                w_dir * dreg +
                w_stab * stab -
                w_energy * self._global_energy
            )

        self._homeostasis_map = homeo

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def get_feedback_map(self) -> Dict[str, float]:
        return dict(self._feedback_map)

    def get_directional_feedback(self) -> Dict[str, float]:
        return dict(self._directional_feedback)

    def get_stabilization_map(self) -> Dict[str, float]:
        return dict(self._stabilization_map)

    def get_homeostasis_map(self) -> Dict[str, float]:
        return dict(self._homeostasis_map)

    def get_global_tension(self) -> float:
        return float(self._global_tension)

    def get_global_energy(self) -> float:
        return float(self._global_energy)
