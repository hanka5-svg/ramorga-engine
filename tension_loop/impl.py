# tension_loop/impl.py
# Deterministyczna implementacja tension_loop zgodna z:
# - data_contracts.md
# - state_invariants.md
# - execution_flow.md

from __future__ import annotations
from typing import Any, Dict
from field_state.impl import FieldState, FieldStateManager, FieldStateError


class TensionLoopError(Exception):
    """Błąd modułu tension_loop."""
    pass


class TensionLoop:
    """
    Moduł tension_loop:
    - operuje WYŁĄCZNIE na tension_map,
    - nie dotyka energii, entropii ani rytuałów,
    - musi być deterministyczny,
    - brak efektów ubocznych.

    Minimalny model:
    - dla każdego klucza w tension_map zwiększamy wartość o 1,
      jeśli wartość jest liczbą,
    - jeśli wartość nie jest liczbą → pozostaje bez zmian.
    """

    def __init__(self, fsm: FieldStateManager) -> None:
        self.fsm = fsm

    def run(self, state: FieldState, params: Dict[str, Any]) -> FieldState:
        if state is None:
            raise TensionLoopError("state is required")

        self.fsm.validate(state)

        tension_map = dict(state.tension_map)

        # deterministyczna aktualizacja
        updated = {}
        for k, v in tension_map.items():
            if isinstance(v, (int, float)):
                updated[k] = v + 1
            else:
                updated[k] = v

        new_state = FieldState(
            energy_level=state.energy_level,
            tension_map=updated,
            entropy_signature=dict(state.entropy_signature),
            ritual_flags=dict(state.ritual_flags),
        )

        self.fsm.validate(new_state)
        return new_state
