import pytest
from pipeline_v12 import (
    StableCore,
    AdaptiveLayer,
    DriftCheckpoint,
    LongTermMemory
)

# --- Stable Core -------------------------------------------------------------

def test_stable_core_invariants_immutable():
    core = StableCore()
    before = core.invariants.copy()
    core.enforce()
    after = core.invariants
    assert before == after


def test_stable_core_rejects_invalid_update():
    core = StableCore()
    with pytest.raises(ValueError):
        core.update_invariant("forbidden_change")


# --- Adaptive Layer ----------------------------------------------------------

def test_adaptive_layer_updates_allowed():
    layer = AdaptiveLayer()
    layer.update("signal", {"value": 1})
    assert "signal" in layer.state


def test_adaptive_layer_respects_invariants():
    layer = AdaptiveLayer()
    layer.bind_invariants({"fixed": True})
    with pytest.raises(RuntimeError):
        layer.update("fixed", False)


# --- Drift Checkpoints -------------------------------------------------------

def test_checkpoint_detects_no_drift():
    cp = DriftCheckpoint()
    assert cp.detect({}, {}) == "none"


def test_checkpoint_detects_directional_drift():
    cp = DriftCheckpoint()
    old = {"x": 1}
    new = {"x": 5}
    assert cp.detect(old, new) == "directional"


def test_checkpoint_detects_critical_drift():
    cp = DriftCheckpoint()
    old = {"x": 1}
    new = {"x": 999}
    assert cp.detect(old, new) == "critical"


# --- Long-Term Memory --------------------------------------------------------

def test_memory_persists_entries():
    mem = LongTermMemory()
    mem.store("id1", {"a": 1})
    assert mem.retrieve("id1") == {"a": 1}


def test_memory_consolidation_prefers_stable():
    mem = LongTermMemory()
    mem.store("core", {"stable": True}, stable=True)
    mem.consolidate("core", {"stable": False})
    assert mem.retrieve("core") == {"stable": True}


def test_memory_reconstruction_uses_checkpoints():
    mem = LongTermMemory()
    mem.store("id", {"v": 1})
    cp = DriftCheckpoint()
    reconstructed = mem.reconstruct(checkpoint=cp)
    assert reconstructed is not None


# --- Integration: Core + Adaptive + Drift + Memory ---------------------------

def test_integration_adaptation_checked_by_core_and_checkpoint():
    core = StableCore()
    layer = AdaptiveLayer()
    cp = DriftCheckpoint()

    # bind invariants from core
    layer.bind_invariants(core.invariants)

    # safe update
    layer.update("x", 1)
    assert layer.state["x"] == 1

    # simulate drift
    old = {"x": 1}
    new = {"x": 50}
    drift = cp.detect(old, new)
    assert drift in ("directional", "critical")


def test_integration_memory_consolidation_after_drift():
    mem = LongTermMemory()
    cp = DriftCheckpoint()

    mem.store("signal", {"v": 1})
    old = {"v": 1}
    new = {"v": 200}

    drift = cp.detect(old, new)
    assert drift == "critical"

    # critical drift → memory should not overwrite stable entry
    mem.store("signal", {"v": 1}, stable=True)
    mem.consolidate("signal", new)
    assert mem.retrieve("signal") == {"v": 1}


def test_integration_full_pipeline_roundtrip():
    core = StableCore()
    layer = AdaptiveLayer()
    mem = LongTermMemory()
    cp = DriftCheckpoint()

    layer.bind_invariants(core.invariants)

    # update layer
    layer.update("a", 10)
    assert layer.state["a"] == 10

    # store to memory
    mem.store("a", {"v": 10})

    # simulate drift
    drift = cp.detect({"v": 10}, {"v": 999})
    assert drift == "critical"

    # reconstruct after drift
    reconstructed = mem.reconstruct(checkpoint=cp)
    assert reconstructed is not None
