# pipeline_v13/impl.py
# Szkielet implementacji PipelineV13 zgodny ze spec.md
# Brak logiki — tylko struktura, interfejs i kontrakty.

from typing import Any, Optional, Dict, List

from ..field_state.impl import FieldState
from ..tension_loop.impl import TensionLoop
from ..energy_regulator.impl import EnergyRegulator
from ..entropic_modulator.impl import EntropicModulator
from ..ritual_detector.impl import RitualDetector
from ..snapshot_manager.impl import SnapshotManager


class PipelineV13:
    """Główny moduł wykonawczy RAMORGA — integracja wszystkich modułów."""

    def __init__(self):
        self.tension_loop = TensionLoop()
        self.energy_regulator = EnergyRegulator()
        self.entropic_modulator = EntropicModulator()
        self.ritual_detector = RitualDetector()
        self.snapshot_manager = SnapshotManager()

    # ---------------------------------------------------------
    # Tryby pracy
    # ---------------------------------------------------------

    def run(
        self,
        mode: str,
        state: Optional[FieldState],
        params: Dict[str, Any],
        steps: int = 1,
        snapshot: Optional[str] = None,
        event_input: Optional[Any] = None,
    ) -> Dict[str, Any]:
        """
        Główna funkcja pipeline.
        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("PipelineV13.run() not implemented")

    # ---------------------------------------------------------
    # Pojedynczy krok regulacji
    # ---------------------------------------------------------

    def _single_step(
        self,
        state: FieldState,
        params: Dict[str, Any],
        event_input: Optional[Any] = None,
    ) -> FieldState:
        """
        Wykonuje jeden krok regulacji pola.
        Kolejność modułów zgodna ze spec.md.
        """
        raise NotImplementedError("PipelineV13._single_step() not implemented")

    # ---------------------------------------------------------
    # Snapshoty
    # ---------------------------------------------------------

    def _maybe_snapshot(self, state: FieldState, mode: str) -> Optional[Any]:
        """
        Obsługa snapshotów zgodnie z trybem.
        """
        raise NotImplementedError("PipelineV13._maybe_snapshot() not implemented")

    # ---------------------------------------------------------
    # Determinizm (test_mode)
    # ---------------------------------------------------------

    def _enforce_determinism(self):
        """
        Wymusza deterministyczność modułów.
        """
        raise NotImplementedError("PipelineV13._enforce_determinism() not implemented")
