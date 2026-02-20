# energy_regulator/test_energy_regulator.py
# Test harness dla energy_regulator — zgodny ze spec.md
# Brak implementacji modułu — testy oczekują NotImplementedError.

import pytest
from .impl import EnergyRegulator
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
# T1 — regulacja energii przy stanie bazowym
# ---------------------------------------------------------

def test_energy_regulation_base_state():
    er = EnergyRegulator()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        er.run(
            energy_level=state.energy_level,
            tension_map=state.tension_map,
            params={}
        )


# ---------------------------------------------------------
# T2 — regulacja przy wysokim napięciu
# ---------------------------------------------------------

def test_energy_regulation_high_tension():
    er = EnergyRegulator()
    state = sample_state()
    state.tension_map = {"a": 10}

    with pytest.raises(NotImplementedError):
        er.run(
            energy_level=state.energy_level,
            tension_map=state.tension_map,
            params={}
        )


# ---------------------------------------------------------
# T3 — regulacja przy niskiej energii
# ---------------------------------------------------------

def test_energy_regulation_low_energy():
    er = EnergyRegulator()
    state = sample_state()
    state.energy_level = 0.1

    with pytest.raises(NotImplementedError):
        er.run(
            energy_level=state.energy_level,
            tension_map=state.tension_map,
            params={}
        )


# ---------------------------------------------------------
# T4 — deterministyczność w test_mode
# ---------------------------------------------------------

def test_enforce_determinism():
    er = EnergyRegulator()

    with pytest.raises(NotImplementedError):
        er.enforce_determinism()
