# tension_loop/test_tension_loop.py
# Test harness dla tension_loop — zgodny ze spec.md
# Brak implementacji modułu — testy oczekują NotImplementedError.

import pytest
from .impl import TensionLoop


# ---------------------------------------------------------
# Pomocnicze dane testowe
# ---------------------------------------------------------

def sample_tension_map():
    return {"a": 1, "b": 2}


# ---------------------------------------------------------
# T1 — aktualizacja napięć przy stanie bazowym
# ---------------------------------------------------------

def test_tension_update_base_state():
    tl = TensionLoop()
    tension_map = sample_tension_map()

    with pytest.raises(NotImplementedError):
        tl.run(tension_map=tension_map, params={})


# ---------------------------------------------------------
# T2 — aktualizacja przy wysokim napięciu
# ---------------------------------------------------------

def test_tension_update_high_tension():
    tl = TensionLoop()
    tension_map = {"a": 10, "b": 20}

    with pytest.raises(NotImplementedError):
        tl.run(tension_map=tension_map, params={})


# ---------------------------------------------------------
# T3 — deterministyczność w test_mode
# ---------------------------------------------------------

def test_enforce_determinism():
    tl = TensionLoop()

    with pytest.raises(NotImplementedError):
        tl.enforce_determinism()
