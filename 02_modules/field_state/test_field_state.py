# field_state/test_field_state.py
# Test harness dla field_state — zgodny ze spec.md
# Brak implementacji modułu — testy oczekują NotImplementedError.

import pytest
from .impl import FieldState, FieldStateManager


# ---------------------------------------------------------
# T1 — poprawna inicjalizacja stanu
# ---------------------------------------------------------

def test_init_creates_valid_state():
    fsm = FieldStateManager()

    with pytest.raises(NotImplementedError):
        fsm.init(params={})


# ---------------------------------------------------------
# T2 — walidacja poprawnego stanu
# ---------------------------------------------------------

def test_validate_valid_state():
    fsm = FieldStateManager()

    state = FieldState(
        energy_level=1.0,
        tension_map={"a": 1},
        entropy_signature={"e": 0},
        ritual_flags={"r": False},
    )

    with pytest.raises(NotImplementedError):
        fsm.validate(state)


# ---------------------------------------------------------
# T3 — clone tworzy kopię stanu
# ---------------------------------------------------------

def test_clone_creates_deep_copy():
    fsm = FieldStateManager()

    state = FieldState(
        energy_level=1.0,
        tension_map={"a": 1},
        entropy_signature={"e": 0},
        ritual_flags={"r": False},
    )

    with pytest.raises(NotImplementedError):
        fsm.clone(state)


# ---------------------------------------------------------
# T4 — merge nadpisuje pola
# ---------------------------------------------------------

def test_merge_overrides_fields():
    fsm = FieldStateManager()

    state = FieldState(
        energy_level=1.0,
        tension_map={"a": 1},
        entropy_signature={"e": 0},
        ritual_flags={"r": False},
    )

    override = {"energy_level": 2.0}

    with pytest.raises(NotImplementedError):
        fsm.merge(state, override)
