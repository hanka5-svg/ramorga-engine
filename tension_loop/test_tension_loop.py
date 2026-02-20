# tension_loop/test_tension_loop.py
# Testy modułu tension_loop zgodne z test_matrix.md i coverage_map.md

import pytest

from field_state.impl import FieldState, FieldStateManager, FieldStateError
from tension_loop.impl import TensionLoop, TensionLoopError


# ---------------------------------------------------------------------------
# T2 — aktualizacja napięć
# ---------------------------------------------------------------------------

def test_tension_loop_updates_numeric_values():
    fsm = FieldStateManager()
    tl = TensionLoop(fsm)

    state = FieldState(
        energy_level=10.0,
        tension_map={"a": 1, "b": 2.5, "c": "x"},
        entropy_signature={},
        ritual_flags={},
    )

    new_state = tl.run(state, params={})

    assert new_state.tension_map["a"] == 2
    assert new_state.tension_map["b"] == 3.5
    assert new_state.tension_map["c"] == "x"  # nienumeryczne bez zmian


def test_tension_loop_does_not_modify_other_fields():
    fsm = FieldStateManager()
    tl = TensionLoop(fsm)

    state = FieldState(
        energy_level=10.0,
        tension_map={"a": 1},
        entropy_signature={"e": 5},
        ritual_flags={"r": False},
    )

    new_state = tl.run(state, params={})

    assert new_state.energy_level == 10.0
    assert new_state.entropy_signature == {"e": 5}
    assert new_state.ritual_flags == {"r": False}


# ---------------------------------------------------------------------------
# T2 — deterministyczność
# ---------------------------------------------------------------------------

def test_tension_loop_is_deterministic():
    fsm = FieldStateManager()
    tl = TensionLoop(fsm)

    state = FieldState(
        energy_level=10.0,
        tension_map={"x": 5},
        entropy_signature={},
        ritual_flags={},
    )

    s1 = tl.run(state, params={})
    s2 = tl.run(state, params={})

    assert s1.tension_map == s2.tension_map


# ---------------------------------------------------------------------------
# ERROR CASES
# ---------------------------------------------------------------------------

def test_tension_loop_rejects_none_state():
    fsm = FieldStateManager()
    tl = TensionLoop(fsm)

    with pytest.raises(TensionLoopError):
        tl.run(None, params={})
