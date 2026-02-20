# snapshot_manager/test_snapshot_manager.py
# Test harness dla snapshot_manager — zgodny ze spec.md
# Brak implementacji snapshot_manager — testy opisowe, strukturalne.

import pytest
from .impl import SnapshotManager, Snapshot
from ..field_state.impl import FieldState


# ---------------------------------------------------------
# Pomocnicze dane testowe
# ---------------------------------------------------------

def sample_state():
    """Minimalny deterministyczny stan do testów."""
    return FieldState(
        energy_level=1.0,
        tension_map={"a": 1},
        entropy_signature={"e": 0},
        ritual_flags={"r": False},
    )


# ---------------------------------------------------------
# T1 — snapshot po inicjalizacji
# ---------------------------------------------------------

def test_snapshot_after_init():
    sm = SnapshotManager()
    state = sample_state()

    with pytest.raises(NotImplementedError):
        sm.save(state)


# ---------------------------------------------------------
# T2 — snapshot ≠ stan początkowy po modyfikacji
# ---------------------------------------------------------

def test_snapshot_differs_after_modification():
    sm = SnapshotManager()
    state = sample_state()

    # Wersja szkieletowa — brak implementacji, test oczekuje wyjątku
    with pytest.raises(NotImplementedError):
        sm.save(state)


# ---------------------------------------------------------
# T3 — restore przywraca stan bit‑po‑bicie
# ---------------------------------------------------------

def test_restore_roundtrip():
    sm = SnapshotManager()
    state = sample_state()

    # Wersja szkieletowa — brak implementacji, test oczekuje wyjątku
    with pytest.raises(NotImplementedError):
        sm.restore(Snapshot(data={}))
