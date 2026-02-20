# tension_loop.py

from __future__ import annotations
from typing import Optional

from .field_engine_physics import FieldEnginePhysics
from .field_state import FieldState


class TensionLoop:
    """
    TensionLoop v1
    ----------------
    Warstwa regulacyjna RAMORGA.

    Odpowiedzialności:
    - pobiera dane z backendu fizycznego,
    - aktualizuje FieldState,
    - wykonuje regulację napięcia (stabilizacja, wygładzanie),
    - zwraca wynik do FieldEngine.

    To jest pętla: physics → state → regulation → output.
    """

    def __init__(self) -> None:
        self._physics: Optional[FieldEnginePhysics] = None
        self._state: Optional[FieldState] = None

    # ------------------------------------------------------------------

    def attach(self, physics: FieldEnginePhysics, state: FieldState) -> None:
        """
        Podpinamy backend fizyczny i stan pola.
        """
        self._physics = physics
        self._state = state

    # ------------------------------------------------------------------

    def step(self) -> None:
        """
        Jeden pełny cykl pętli napięcia.
        """
        if self._physics is None or self._state is None:
            raise RuntimeError("TensionLoop not attached.")

        # 1) Pobierz pozycje z fizyki
        positions = self._physics.get_positions()

        # 2) Zaktualizuj stan pola
        self._state.update_from_positions(positions)

        # 3) Regulacja napięcia (v1: proste wygładzanie)
        self._apply_regulation()

    # ------------------------------------------------------------------

    def _apply_regulation(self) -> None:
        """
        Regulacja napięcia.
        v1: proste wygładzanie mapy napięć.
        """
        tension_map = self._state.get_tension_map()

        # proste wygładzanie globalne
        avg = sum(tension_map.values()) / max(len(tension_map), 1)

        # zapisujemy wynik jako "global tension level"
        self._global_tension = avg

    # ------------------------------------------------------------------

    def get_global_tension(self) -> float:
        """
        Zwraca globalny poziom napięcia pola.
        """
        return getattr(self, "_global_tension", 0.0)
