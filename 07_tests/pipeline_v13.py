# pipeline_v13.py

from __future__ import annotations
from typing import Dict, Any

from ..03_field_engine.field_engine import FieldEngine
from ..03_field_engine.field_engine_physics import FieldEnginePhysics
from ..03_field_engine.field_state import FieldState
from ..03_field_engine.tension_loop import TensionLoop


class PipelineV13:
    """
    PipelineV13 — pełna integracja z TensionLoop v10.

    Odpowiedzialności:
    - inicjalizacja fizyki pola,
    - inicjalizacja stanu pola,
    - inicjalizacja pętli regulacyjnej,
    - wykonywanie kroków regulacji,
    - udostępnianie snapshotów pola.
    """

    def __init__(
        self,
        nodes,
        edges,
        *,
        k_charge: float = 1.0,
        k_coherence: float = 0.1,
        damping: float = 0.9,
        dt: float = 0.05,
    ) -> None:

        # 1) Stan pola
        self._state = FieldState()

        # 2) Backend fizyczny
        self._physics = FieldEnginePhysics(
            nodes=nodes,
            edges=edges,
            k_charge=k_charge,
            k_coherence=k_coherence,
            damping=damping,
            dt=dt,
        )

        # 3) Silnik pola (interfejs)
        self._engine = FieldEngine(initial_state=self._state)

        # 4) Pętla regulacyjna v10
        self._loop = TensionLoop()
        self._loop.attach(self._physics, self._state)

        self._dt = dt

    # ------------------------------------------------------------------

    def step(self, steps: int = 1) -> None:
        """
        Wykonuje pełną pętlę regulacyjną v10.
        """
        for _ in range(steps):
            self._loop.step(dt=self._dt)

    # ------------------------------------------------------------------

    def snapshot(self) -> Dict[str, Any]:
        """
        Zwraca pełny stan pola po kroku regulacyjnym.
        """
        return {
            "positions": self._state.get_positions(),
            "tension": self._state.get_tension(),
            "gradient": self._state.get_gradient(),
            "homeostasis": self._loop.get_homeostasis_map(),
            "spectral": self._loop.get_spectral_stability(),
            "phase": self._loop.get_phase_map(),
            "layer_coupling": self._loop.get_layer_coupling(),
            "adaptation": self._loop.get_long_term_adaptation(),
            "context": self._loop.get_context_modulation(),
            "realtime_control": self._loop.get_realtime_control(),
            "global_tension": self._loop.get_global_tension(),
            "global_energy": self._loop.get_global_energy(),
        }
