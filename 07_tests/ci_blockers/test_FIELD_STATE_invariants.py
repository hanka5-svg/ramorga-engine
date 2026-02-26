# test_FIELD_STATE_invariants.py
# CI BLOCKER — naruszenie inwariantu blokuje merge

import pytest
from field_state.field_state_manager import FieldStateManager, FieldStateError, FieldState


def test_energy_bounds():
    fsm = FieldStateManager()
    with pytest.raises(FieldStateError):
        fsm.validate(FieldState(-1, {}, {"energy_level": -1}, {}))

    with pytest.raises(FieldStateError):
        fsm.validate(FieldState(999, {}, {"energy_level": 999}, {}))


def test_tension_map_structure():
    fsm = FieldStateManager()
    with pytest.raises(FieldStateError):
        fsm.validate(FieldState(50, {"x": "bad"}, {"energy_level": 50}, {}))


def test_entropy_signature_contains_energy():
    fsm = FieldStateManager()
    with pytest.raises(FieldStateError):
        fsm.validate(FieldState(50, {}, {}, {}))


def test_ritual_flags_structure():
    fsm = FieldStateManager()
    with pytest.raises(FieldStateError):
        fsm.validate(FieldState(50, {}, {"energy_level": 50}, {"x": "bad"}))
