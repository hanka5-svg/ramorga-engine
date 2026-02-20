# ritual_detector/test_ritual_detector.py
# Test harness dla ritual_detector — zgodny ze spec.md
# Brak implementacji modułu — testy oczekują NotImplementedError.

import pytest
from .impl import RitualDetector
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
# T1 — brak aktywacji rytuałów przy stanie bazowym
# ---------------------------------------------------------

def test_no_activation_on_base_state():
    rd = RitualDetector()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        rd.run(state, event_input=None, params={})


# ---------------------------------------------------------
# T2 — deterministyczność w test_mode
# ---------------------------------------------------------

def test_enforce_determinism():
    rd = RitualDetector()

    with pytest.raises(NotImplementedError):
        rd.enforce_determinism()


# ---------------------------------------------------------
# T3 — obsługa EventInput (szkielet)
# ---------------------------------------------------------

def test_event_input_handling():
    rd = RitualDetector()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        rd.run(state, event_input={"type": "dummy"}, params={})
