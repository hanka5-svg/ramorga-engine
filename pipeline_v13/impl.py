# pipeline_v13/impl.py
# Pełna implementacja PipelineV13 zgodna z:
# - state_invariants.md
# - data_contracts.md
# - execution_flow.md
# - state_machine.md
# - test_pipeline_v13.py

from __future__ import annotations

from dataclasses import asdict
from typing import Any, Dict, Optional, Tuple

from field_state.impl import FieldState, FieldStateManager, FieldStateError


class PipelineError(Exception):
    """Błąd sekwencji wykonawczej lub trybu pipeline."""
    pass


class SnapshotManager:
    """
    Minimalna implementacja snapshot_manager zgodna z data_contracts.md:

    - save(state) -> dict (pełna serializacja)
    - restore(snapshot) -> FieldState (bit-po-bicie)
    """

    def save(self, state: FieldState) -> Dict[str, Any]:
        if state is None:
            raise PipelineError("Cannot snapshot None state")
        return asdict(state)

    def restore(self, snapshot: Dict[str, Any]) -> FieldState:
        if not isinstance(snapshot, dict):
            raise PipelineError("Snapshot must be a dict")
        return FieldState(
            energy_level=snapshot["energy_level"],
            tension_map=dict(snapshot["tension_map"]),
            entropy_signature=dict(snapshot["entropy_signature"]),
            ritual_flags=dict(snapshot["ritual_flags"]),
        )


class PipelineV13:
    """
    Deterministyczny pipeline RAMORGA-ENGINE.

    Tryby:
    - init
    - single_step
    - multi_step

    Kontrakt run():
    - run(mode="init", params, snapshot=False) -> (FieldState, Optional[dict])
    - run(mode="single_step", state, params, snapshot=False) -> (FieldState, Optional[dict])
    - run(mode="multi_step", state, params, steps, snapshot=False) -> (FieldState, Optional[dict])
    """

    def __init__(self, fsm: FieldStateManager) -> None:
        if fsm is None:
            raise PipelineError("FieldStateManager is required")
        self.fsm = fsm
        self.snapshot_manager = SnapshotManager()

    # ------------------------------------------------------------------ #
    # API GŁÓWNE
    # ------------------------------------------------------------------ #

    def run(
        self,
        *,
        mode: str,
        state: Optional[FieldState] = None,
        params: Optional[Dict[str, Any]] = None,
        steps: int = 1,
        snapshot: bool = False,
        event_input: Optional[Dict[str, Any]] = None,
    ) -> Tuple[FieldState, Optional[Dict[str, Any]]]:
        """
        Główna metoda wykonawcza PipelineV13.
        Zwraca (FieldState, Optional[Snapshot]).
        """
        params = params or {}

        if mode == "init":
            return self._run_init(params=params, snapshot=snapshot)

        if mode == "single_step":
            return self._run_single_step(
                state=state,
                params=params,
                snapshot=snapshot,
                event_input=event_input,
            )

        if mode == "multi_step":
            return self._run_multi_step(
                state=state,
                params=params,
                steps=steps,
                snapshot=snapshot,
                event_input=event_input,
            )

        raise PipelineError(f"Unknown mode: {mode!r}")

    # ------------------------------------------------------------------ #
    # INIT
    # ------------------------------------------------------------------ #

    def _run_init(
        self,
        *,
        params: Dict[str, Any],
        snapshot: bool,
    ) -> Tuple[FieldState, Optional[Dict[str, Any]]]:
        state = self.fsm.init(params)
        self.fsm.validate(state)

        snap = self.snapshot_manager.save(state) if snapshot else None
        return state, snap

    # ------------------------------------------------------------------ #
    # SINGLE STEP
    # ------------------------------------------------------------------ #

    def _run_single_step(
        self,
        *,
        state: Optional[FieldState],
        params: Dict[str, Any],
        snapshot: bool,
        event_input: Optional[Dict[str, Any]],
    ) -> Tuple[FieldState, Optional[Dict[str, Any]]]:
        if state is None:
            raise PipelineError("state is required for single_step")

        self.fsm.validate(state)

        new_state = self._run_step(
            state=state,
            params=params,
            event_input=event_input,
        )

        self.fsm.validate(new_state)

        snap = self.snapshot_manager.save(new_state) if snapshot else None
        return new_state, snap

    # ------------------------------------------------------------------ #
    # MULTI STEP
    # ------------------------------------------------------------------ #

    def _run_multi_step(
        self,
        *,
        state: Optional[FieldState],
        params: Dict[str, Any],
        steps: int,
        snapshot: bool,
        event_input: Optional[Dict[str, Any]],
    ) -> Tuple[FieldState, Optional[Dict[str, Any]]]:
        if state is None:
            raise PipelineError("state is required for multi_step")

        if steps < 1:
            raise PipelineError("steps must be >= 1")

        self.fsm.validate(state)

        current = state
        for i in range(steps):
            current = self._run_step(
                state=current,
                params=params,
                event_input=event_input,
            )
            self.fsm.validate(current)

        snap = self.snapshot_manager.save(current) if snapshot else None
        return current, snap

    # ------------------------------------------------------------------ #
    # POJEDYNCZY KROK (TENSION → ENERGY → ENTROPY → RITUAL)
    # ------------------------------------------------------------------ #

    def _run_step(
        self,
        *,
        state: FieldState,
        params: Dict[str, Any],
        event_input: Optional[Dict[str, Any]],
    ) -> FieldState:
        """
        Wykonuje jeden krok regulacji:

        tension_loop → energy_regulator → entropic_modulator → ritual_detector
        """

        s1 = self._run_tension_loop(state, params.get("tension", {}))
        s2 = self._run_energy_regulator(s1, params.get("energy", {}))
        s3 = self._run_entropic_modulator(s2, params.get("entropy", {}))
        s4 = self._run_ritual_detector(s3, params.get("rituals", {}), event_input)

        return s4

    # ------------------------------------------------------------------ #
    # MODUŁY (MINIMALNE, DETERMINISTYCZNE ZACHOWANIE)
    # ------------------------------------------------------------------ #

    def _run_tension_loop(
        self,
        state: FieldState,
        tension_params: Dict[str, Any],
    ) -> FieldState:
        """
        Minimalna, deterministyczna implementacja tension_loop.

        Tu tylko zachowujemy mapę napięć (lub lekko ją modyfikujemy w sposób
        deterministyczny, jeśli kiedyś będzie potrzeba).
        Na razie: no-op na tension_map.
        """
        return FieldState(
            energy_level=state.energy_level,
            tension_map=dict(state.tension_map),
            entropy_signature=dict(state.entropy_signature),
            ritual_flags=dict(state.ritual_flags),
        )

    def _run_energy_regulator(
        self,
        state: FieldState,
        energy_params: Dict[str, Any],
    ) -> FieldState:
        """
        Minimalna, deterministyczna implementacja energy_regulator.

        Prosty model:
        - zwiększamy energię o stałą wartość (domyślnie 1.0),
        - clamp do [E_min, E_max].
        """
        delta = float(energy_params.get("delta", 1.0))
        e_min = float(energy_params.get("energy_min", self.fsm.DEFAULT_ENERGY_MIN))
        e_max = float(energy_params.get("energy_max", self.fsm.DEFAULT_ENERGY_MAX))

        new_energy = state.energy_level + delta
        new_energy = max(e_min, min(e_max, new_energy))

        return FieldState(
            energy_level=new_energy,
            tension_map=dict(state.tension_map),
            entropy_signature=dict(state.entropy_signature),
            ritual_flags=dict(state.ritual_flags),
        )

    def _run_entropic_modulator(
        self,
        state: FieldState,
        entropy_params: Dict[str, Any],
    ) -> FieldState:
        """
        Minimalna, deterministyczna implementacja entropic_modulator.

        Prosty model:
        - zapisujemy aktualny poziom energii w sygnaturze entropii,
        - brak losowości.
        """
        entropy_signature = dict(state.entropy_signature)
        entropy_signature["energy_level"] = state.energy_level

        return FieldState(
            energy_level=state.energy_level,
            tension_map=dict(state.tension_map),
            entropy_signature=entropy_signature,
            ritual_flags=dict(state.ritual_flags),
        )

    def _run_ritual_detector(
        self,
        state: FieldState,
        ritual_params: Dict[str, Any],
        event_input: Optional[Dict[str, Any]],
    ) -> FieldState:
        """
        Minimalna, deterministyczna implementacja ritual_detector.

        Prosty model:
        - brak aktywnych rytuałów (wszystko False),
        - zależność tylko od state + event_input (tu: ignorujemy event_input).
        """
        ritual_flags = dict(state.ritual_flags)

        # Można tu kiedyś dodać logikę, na razie: wszystko False.
        for k in ritual_flags.keys():
            ritual_flags[k] = False

        return FieldState(
            energy_level=state.energy_level,
            tension_map=dict(state.tension_map),
            entropy_signature=dict(state.entropy_signature),
            ritual_flags=ritual_flags,
        )
