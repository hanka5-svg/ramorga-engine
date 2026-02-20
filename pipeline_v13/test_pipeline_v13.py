# pipeline_v13/test_pipeline_v13.py
# Testy integracyjne PipelineV13 zgodne z T1–T4.

import pytest

from field_state.impl import FieldStateManager, FieldStateError
from pipeline_v13.impl import PipelineV13, PipelineError


# ---------------------------------------------------------------------------
# T1 — INIT
# ---------------------------------------------------------------------------

def test_init_creates_valid_state():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, snapshot = pipeline.run(mode="init", params={}, snapshot=False)

    assert state is not None
    assert snapshot is None
    fsm.validate(state)


def test_init_with_snapshot():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, snapshot = pipeline.run(mode="init", params={}, snapshot=True)

    assert state is not None
    assert snapshot is not None
    assert isinstance(snapshot, dict)


# ---------------------------------------------------------------------------
# T2 — SINGLE STEP
# ---------------------------------------------------------------------------

def test_single_step_updates_state():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, _ = pipeline.run(mode="init", params={})
    initial_energy = state.energy_level

    new_state, snapshot = pipeline.run(
        mode="single_step",
        state=state,
        params={},
        snapshot=False,
    )

    assert new_state is not state
    assert new_state.energy_level != initial_energy
    assert snapshot is None

    fsm.validate(new_state)


def test_single_step_with_snapshot():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, _ = pipeline.run(mode="init", params={})

    new_state, snapshot = pipeline.run(
        mode="single_step",
        state=state,
        params={},
        snapshot=True,
    )

    assert new_state is not None
    assert snapshot is not None
    fsm.validate(new_state)


# ---------------------------------------------------------------------------
# T3 — MULTI STEP (stabilność)
# ---------------------------------------------------------------------------

def test_multi_step_runs_multiple_iterations():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, _ = pipeline.run(mode="init", params={})

    new_state, snapshot = pipeline.run(
        mode="multi_step",
        state=state,
        params={},
        steps=5,
        snapshot=False,
    )

    assert new_state is not None
    assert snapshot is None
    fsm.validate(new_state)


def test_multi_step_energy_stays_in_bounds():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, _ = pipeline.run(mode="init", params={})

    new_state, _ = pipeline.run(
        mode="multi_step",
        state=state,
        params={},
        steps=20,
        snapshot=False,
    )

    assert 0.0 <= new_state.energy_level <= 100.0
    fsm.validate(new_state)


# ---------------------------------------------------------------------------
# T4 — SNAPSHOTS
# ---------------------------------------------------------------------------

def test_snapshot_after_multi_step():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, _ = pipeline.run(mode="init", params={})

    new_state, snapshot = pipeline.run(
        mode="multi_step",
        state=state,
        params={},
        steps=3,
        snapshot=True,
    )

    assert new_state is not None
    assert snapshot is not None
    assert isinstance(snapshot, dict)


def test_snapshot_restore_roundtrip():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, snapshot = pipeline.run(mode="init", params={}, snapshot=True)

    restored = pipeline.snapshot_manager.restore(snapshot)

    assert restored == state
    fsm.validate(restored)


# ---------------------------------------------------------------------------
# ERROR CASES
# ---------------------------------------------------------------------------

def test_error_on_invalid_mode():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    with pytest.raises(PipelineError):
        pipeline.run(mode="unknown", params={})


def test_error_on_missing_state_in_single_step():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    with pytest.raises(PipelineError):
        pipeline.run(mode="single_step", state=None, params={})


def test_error_on_zero_steps_in_multi_step():
    fsm = FieldStateManager()
    pipeline = PipelineV13(fsm=fsm)

    state, _ = pipeline.run(mode="init", params={})

    with pytest.raises(PipelineError):
        pipeline.run(mode="multi_step", state=state, params={}, steps=0)
