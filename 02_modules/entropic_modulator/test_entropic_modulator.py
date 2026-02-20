# entropic_modulator/test_entropic_modulator.py
# Test harness dla entropic_modulator — zgodny ze spec.md
# Brak implementacji modułu — testy oczekują NotImplementedError.

import pytest
from .impl import EntropicModulator
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
# T1 — modulacja entropii przy stanie bazowym
# ---------------------------------------------------------

def test_entropy_modulation_base_state():
    em = EntropicModulator()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        em.run(
            entropy_signature=state.entropy_signature,
            energy_level=state.energy_level,
            params={}
        )


# ---------------------------------------------------------
# T2 — deterministyczność w test_mode
# ---------------------------------------------------------

def test_enforce_determinism():
    em = EntropicModulator()

    with pytest.raises(NotImplementedError):
        em.enforce_determinism()


# ---------------------------------------------------------
# T3 — modulacja przy niskiej energii (szkielet)
# ---------------------------------------------------------

def test_entropy_modulation_low_energy():
    em = EntropicModulator()
    state = sample_state()
    state.energy_level = 0.1

    with pytest.raises(NotImplementedError):
        em.run(
            entropy_signature=state.entropy_signature,
            energy_level=state.energy_level,
            params={}
        )
