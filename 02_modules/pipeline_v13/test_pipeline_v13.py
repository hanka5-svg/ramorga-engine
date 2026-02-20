# pipeline_v13/test_pipeline_v13.py
# Test harness dla PipelineV13 — zgodny ze spec.md i T1–T4.
# Brak implementacji modułu — testy oczekują NotImplementedError.

import pytest
from .impl import PipelineV13
from ..field_state.impl import FieldState


# ---------------------------------------------------------
# Pomocniczy stan testowy
# ---------------------------------------------------------

def sample_state():
    return FieldState(
        energy_level=1.0,
        tension_map={"a": 1},
        entropy_signature={"e": 0},
        ritual_flags={"r": False},
    )


# ---------------------------------------------------------
# T1 — test inicjalizacji
# ---------------------------------------------------------

def test_pipeline_init():
    p = PipelineV13()

    with pytest.raises(NotImplementedError):
        p.run(
            mode="init",
            state=None,
            params={},
            steps=1,
            snapshot=False,
            event_input=None,
        )


# ---------------------------------------------------------
# T2 — test jednego kroku regulacji
# ---------------------------------------------------------

def test_pipeline_single_step():
    p = PipelineV13()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        p.run(
            mode="single_step",
            state=state,
            params={},
            steps=1,
            snapshot=False,
            event_input=None,
        )


# ---------------------------------------------------------
# T3 — test stabilności energii (multi_step)
# ---------------------------------------------------------

def test_pipeline_energy_stability():
    p = PipelineV13()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        p.run(
            mode="multi_step",
            state=state,
            params={},
            steps=10,
            snapshot=False,
            event_input=None,
        )


# ---------------------------------------------------------
# T4 — test snapshotów
# ---------------------------------------------------------

def test_pipeline_snapshots():
    p = PipelineV13()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        p.run(
            mode="single_step",
            state=state,
            params={},
            steps=1,
            snapshot=True,
            event_input=None,
        )
