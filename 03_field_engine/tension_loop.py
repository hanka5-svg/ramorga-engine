# tension_loop.py

from __future__ import annotations
from typing import Optional, Dict

from .field_engine_physics import FieldEnginePhysics
from .field_state import FieldState


class TensionLoop:
    """
    TensionLoop v10 — pełna regulacja pola RAMORGA w czasie rzeczywistym.

    Zawiera:
    - v2: lokalne sprzężenia zwrotne,
    - v3: regulacja kierunkowa,
    - v4: stabilizacja gradientowa,
    - v5: homeostaza (lokalna + globalna),
    - v6: stabilizacja spektralna / oscylacje fazowe,
    - v7: sprzężenia wielowarstwowe (C/G/S/Meniscus),
    - v8: adaptacja długoterminowa,
    - v9: modulacja kontekstowa,
    - v10: pełna regulacja pola w czasie rzeczywistym.

    Pętla:
        physics → state → regulation → homeostasis → adaptation → context → realtime
    """

    def __init__(self) -> None:
        self._physics: Optional[FieldEnginePhysics] = None
        self._state: Optional[FieldState] = None

        # v2–v5
        self._feedback_map: Dict[str, float] = {}
        self._directional_feedback: Dict[str, float] = {}
        self._stabilization_map: Dict[str, float] = {}
        self._homeostasis_map: Dict[str, float] = {}

        self._global_tension: float = 0.0
        self._global_energy: float = 0.0

        # v6
        self._spectral_stability: Dict[str, float] = {}
        self._phase_map: Dict[str, float] = {}

        # v7
        self._layer_coupling: Dict[str, float] = {}

        # v8
        self._long_term_adaptation: Dict[str, float] = {}

        # v9
        self._context_modulation: Dict[str, float] = {}

        # v10
        self._realtime_control: Dict[str, float] = {}

    # ------------------------------------------------------------------
    # Podpinanie backendów
    # ------------------------------------------------------------------

    def attach(self, physics: FieldEnginePhysics, state: FieldState) -> None:
        self._physics = physics
        self._state = state

    # ------------------------------------------------------------------
    # Główna pętla
    # ------------------------------------------------------------------

    def step(self, dt: float = 1.0) -> None:
        if self._physics is None or self._state is None:
            raise RuntimeError("TensionLoop not attached.")

        # 1) Fizyczny krok
        self._physics.step(1)
        positions = self._physics.get_positions()

        # 2) Aktualizacja stanu pola
        self._state.update_from_positions(positions)

        # 3) v2–v5: klasyczna regulacja + homeostaza
        self._apply_local_feedback()
        self._apply_directional_regulation()
        self._apply_gradient_stabilization()
        self._apply_homeostasis()

        # 4) v6: stabilizacja spektralna / oscylacje fazowe
        self._apply_spectral_stabilization(dt)

        # 5) v7: sprzężenia wielowarstwowe (C/G/S/Meniscus)
        self._apply_multilayer_coupling()

        # 6) v8: adaptacja długoterminowa
        self._apply_long_term_adaptation(dt)

        # 7) v9: modulacja kontekstowa
        self._apply_context_modulation()

        # 8) v10: pełna regulacja w czasie rzeczywistym
        self._apply_realtime_regulation(dt)

    # ------------------------------------------------------------------
    # v2: lokalne sprzężenia zwrotne
    # ------------------------------------------------------------------

    def _apply_local_feedback(self) -> None:
        tension = self._state.get_tension()
        curvature = self._state.get_curvature()
        directional = self._state.get_directional_energy()
        neighbors = self._state._neighbors

        feedback: Dict[str, float] = {}

        w1 = 1.0
        w2 = 0.7
        w3 = 0.5
        w4 = 1.2

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
        positions = self._state.get_positions()

        directional_feedback: Dict[str, float] = {}
        w_dir = 0.8

        for nid, (gx, gy) in gradient.items():
            neigh = neighbors.get(nid, set())
            if not neigh:
                directional_feedback[nid] = 0.0
                continue

            total = 0.0
            px, py = positions[nid]

            for nj in neigh:
                if nj not in positions:
                    continue
                qx, qy = positions[nj]
                dx = qx - px
                dy = qy - py
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
    # v5: homeostaza
    # ------------------------------------------------------------------

    def _apply_homeostasis(self) -> None:
        tension_map = self._feedback_map
        directional = self._directional_feedback
        stabilization = self._stabilization_map

        homeo: Dict[str, float] = {}

        E_el = self._state.get_elastic_energy()
        E_ch = self._state.get_charge_energy()
        self._global_energy = E_el + E_ch

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
    # v6: stabilizacja spektralna / oscylacje fazowe
    # ------------------------------------------------------------------

    def _apply_spectral_stabilization(self, dt: float) -> None:
        """
        Prosty model: faza ~ zintegrowane napięcie, stabilizacja ~ tłumienie
        szybkich zmian fazy.
        """
        phase: Dict[str, float] = {}
        spectral: Dict[str, float] = {}

        base = self._homeostasis_map or self._feedback_map

        w_phase = 0.1
        w_damp = 0.05

        for nid, val in base.items():
            prev_phase = self._phase_map.get(nid, 0.0)
            new_phase = prev_phase + w_phase * val * dt
            phase[nid] = new_phase

            # tłumienie oscylacji
            spectral[nid] = -w_damp * (new_phase * new_phase)

        self._phase_map = phase
        self._spectral_stability = spectral

    # ------------------------------------------------------------------
    # v7: sprzężenia wielowarstwowe (C/G/S/Meniscus)
    # ------------------------------------------------------------------

    def _apply_multilayer_coupling(self) -> None:
        """
        Tu zakładamy, że FieldState może w przyszłości udostępniać
        metryki warstw C/G/S/Meniscus. Na razie modelujemy to jako
        funkcję homeostazy + energii.
        """
        coupling: Dict[str, float] = {}

        w_homeo = 1.0
        w_energy = 0.2
        w_spec = 0.5

        for nid in self._homeostasis_map:
            h = self._homeostasis_map.get(nid, 0.0)
            s = self._spectral_stability.get(nid, 0.0)
            coupling[nid] = (
                w_homeo * h +
                w_spec * s -
                w_energy * self._global_energy
            )

        self._layer_coupling = coupling

    # ------------------------------------------------------------------
    # v8: adaptacja długoterminowa
    # ------------------------------------------------------------------

    def _apply_long_term_adaptation(self, dt: float) -> None:
        """
        Prosty model pamięci: adaptacja[n] = poprzednia + alpha * coupling[n].
        """
        adaptation: Dict[str, float] = {}
        alpha = 0.01 * dt

        for nid, val in self._layer_coupling.items():
            prev = self._long_term_adaptation.get(nid, 0.0)
            adaptation[nid] = prev + alpha * val

        self._long_term_adaptation = adaptation

    # ------------------------------------------------------------------
    # v9: modulacja kontekstowa
    # ------------------------------------------------------------------

    def _apply_context_modulation(self) -> None:
        """
        Kontekst = funkcja homeostazy + adaptacji.
        """
        context: Dict[str, float] = {}

        w_h = 0.7
        w_a = 0.3

        for nid in self._homeostasis_map:
            h = self._homeostasis_map.get(nid, 0.0)
            a = self._long_term_adaptation.get(nid, 0.0)
            context[nid] = w_h * h + w_a * a

        self._context_modulation = context

    # ------------------------------------------------------------------
    # v10: pełna regulacja pola w czasie rzeczywistym
    # ------------------------------------------------------------------

    def _apply_realtime_regulation(self, dt: float) -> None:
        """
        Łączy wszystkie warstwy w sygnał sterujący dla pola.
        """
        control: Dict[str, float] = {}

        w_fb = 1.0
        w_dir = 0.5
        w_stab = 0.5
        w_homeo = 0.8
        w_spec = 0.4
        w_ctx = 0.6

        for nid in self._feedback_map:
            fb = self._feedback_map.get(nid, 0.0)
            d = self._directional_feedback.get(nid, 0.0)
            st = self._stabilization_map.get(nid, 0.0)
            h = self._homeostasis_map.get(nid, 0.0)
            sp = self._spectral_stability.get(nid, 0.0)
            ctx = self._context_modulation.get(nid, 0.0)

            control[nid] = (
                w_fb * fb +
                w_dir * d +
                w_stab * st +
                w_homeo * h +
                w_spec * sp +
                w_ctx * ctx
            ) * dt

        self._realtime_control = control

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

    def get_spectral_stability(self) -> Dict[str, float]:
        return dict(self._spectral_stability)

    def get_phase_map(self) -> Dict[str, float]:
        return dict(self._phase_map)

    def get_layer_coupling(self) -> Dict[str, float]:
        return dict(self._layer_coupling)

    def get_long_term_adaptation(self) -> Dict[str, float]:
        return dict(self._long_term_adaptation)

    def get_context_modulation(self) -> Dict[str, float]:
        return dict(self._context_modulation)

    def get_realtime_control(self) -> Dict[str, float]:
        return dict(self._realtime_control)

    def get_global_tension(self) -> float:
        return float(self._global_tension)

    def get_global_energy(self) -> float:
        return float(self._global_energy)
