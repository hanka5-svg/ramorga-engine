# field_state/test_field_state.py
# Testy FieldStateManager zgodne z invariants + data_contracts.

import pytest
from field_state.impl import FieldState, FieldStateManager, FieldStateError


# ---------------------------------------------------------------------------
# T1 — INIT
# ---------------------------------------------------------------------------

def test_init_creates_valid_state():
    fsm = FieldStateManager()
    state = fsm.init()

    assert isinstance(state, FieldState)
    assert isinstance(state.energy_level, float)
    assert isinstance(state.tension_map, dict)
    assert isinstance(state.entropy_signature, dict)
    assert isinstance(state.ritual_flags, dict)

    # energia w zakresie
    assert 0.0 <= state.energy_level <= 100.0


def test_init_respects_energy_bounds():
    fsm = FieldStateManager()

    state = fsm.init({"energy_level": 999})
    assert state.energy_level == 100.0  # clamp

    state = fsm.init({"energy_level": -50})
    assert state.energy_level == 0.0  # clamp


# ---------------------------------------------------------------------------
# T2 — VALIDATE
# ---------------------------------------------------------------------------

def test_validate_rejects_none_state():
    fsm = FieldStateManager()
    with pytest.raises(FieldStateError):
        fsm.validate(None)


def test_validate_rejects_nan_energy():
    fsm = FieldStateManager()
    bad = FieldState(
        energy_level=float("nan"),
        tension_map={},
        entropy_signature={},
        ritual_flags={}
    )
    with pytest.raises(FieldStateError):
        fsm.validate(bad)


def test_validate_rejects_non_bool_ritual_flags():
    fsm = FieldStateManager()
    bad = FieldState(
        energy_level=10.0,
        tension_map={},
        entropy_signature={},
        ritual_flags={"x": "not_bool"}
    )
    with pytest.raises(FieldStateError):
        fsm.validate(bad)


# ---------------------------------------------------------------------------
# T3 — CLONE
# ---------------------------------------------------------------------------

def test_clone_creates_deep_copy():
    fsm = FieldStateManager()

    state = FieldState(
        energy_level=10.0,
        tension_map={"a": [1, 2]},
        entropy_signature={"e": {"x": 1}},
        ritual_flags={"r": False},
    )

    clone = fsm.clone(state)

    assert clone is not state
    assert clone.tension_map is not state.tension_map
    assert clone.entropy_signature is not state.entropy_signature
    assert clone.ritual_flags is not state.ritual_flags

    # wartości identyczne
    assert clone.tension_map == state.tension_map
    assert clone.entropy_signature == state.entropy_signature
    assert clone.ritual_flags == state.ritual_flags


# ---------------------------------------------------------------------------
# T4 — MERGE
# ---------------------------------------------------------------------------

def test_merge_overrides_energy_level():
    fsm = FieldStateManager()

    state = fsm.init({"energy_level": 10})
    merged = fsm.merge(state, {"energy_level": 20})

    assert merged.energy_level == 20
    assert merged is not state


def test_merge_rejects_unknown_keys():
    fsm = FieldStateManager()
    state = fsm.init()

    with pytest.raises(FieldStateError):
        fsm.merge(state, {"unknown": 123})


def test_merge_validates_after_merge():
    fsm = FieldStateManager()
    state = fsm.init()

    # ustawiamy energię poza zakresem → powinno rzucić błąd
    with pytest.raises(FieldStateError):
        fsm.merge(state, {"energy_level": -999})
