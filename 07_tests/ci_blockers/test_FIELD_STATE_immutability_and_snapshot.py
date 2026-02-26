# CI BLOCKER — immutability + snapshot consistency

from dataclasses import FrozenInstanceError
import pytest

from field_state.field_state_manager import FieldStateManager, FieldState
from pipeline_v13.impl import SnapshotManager


def test_field_state_is_frozen():
    fsm = FieldStateManager()
    state = fsm.init({})
    with pytest.raises(FrozenInstanceError):
        state.energy_level = 999  # type: ignore[attr-defined]


def test_snapshot_round_trip():
    fsm = FieldStateManager()
    sm = SnapshotManager()

    original = fsm.init({
        "energy": 42.0,
        "tension": {"a": 1.0},
        "entropy": {"x": "y"},
        "rituals": {"r1": True},
    })

    snap = sm.save(original)
    restored = sm.restore(snap)

    assert restored == original
