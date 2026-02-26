# test_hooks_and_pipeline_v13.py
# RAMORGA ENGINE — tests
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

import pytest

from runtime.memory_audit_hook import memory_audit_hook
from runtime.topology_metrics import topology_metrics
from runtime.glitch_hook import glitch_hook
from runtime.carnival_gate_hook import carnival_gate_hook
from runtime.crime_planning_detector import crime_planning_detector

from pipeline_v13.pipeline import PipelineV13


# ---------------------------------------------------------
# 1. MEMORY HOOK TESTS
# ---------------------------------------------------------

def test_memory_read_logged(field_state, metadata):
    memory_audit_hook.read("snapshot", metadata)
    assert len(field_state.memory_log) == 1
    assert field_state.memory_log[0]["operation"] == "read"


def test_memory_write_logged(field_state, metadata):
    memory_audit_hook.write("snapshot", {"x": 1}, metadata)
    assert len(field_state.memory_log) == 1
    assert field_state.memory_log[0]["operation"] == "write"


def test_memory_block_in_regulate_phase(field_state, metadata_regulate):
    with pytest.raises(Exception):
        memory_audit_hook.read("snapshot", metadata_regulate)


def test_memory_no_prediction(field_state, metadata):
    with pytest.raises(Exception):
        memory_audit_hook.predict("future_key", metadata)


# ---------------------------------------------------------
# 2. TOPOLOGY METRICS TESTS
# ---------------------------------------------------------

def test_topology_register_flow(field_state, metadata):
    topology_metrics.register_flow("pipeline_v13", metadata)
    assert field_state.routing_counter["pipeline_v13"] == 1


def test_topology_compute_share(field_state, metadata):
    topology_metrics.register_flow("pipeline_v13", metadata)
    share = topology_metrics.compute_share(field_state)
    assert "pipeline_v13" in share


def test_topology_threshold_detection(field_state, metadata):
    # sztucznie ustawiamy wysokie wartości
    field_state.routing_counter = {"pipeline_v13": 100, "other": 1}
    assert topology_metrics.check_threshold(field_state) is True


# ---------------------------------------------------------
# 3. GLITCH HOOK TESTS
# ---------------------------------------------------------

def test_glitch_emit_logged(field_state, metadata, glitch_event):
    glitch_hook.emit(glitch_event, metadata)
    assert len(field_state.glitch_log) == 1


def test_glitch_propagation_chain(field_state, metadata, glitch_event):
    glitch_hook.emit(glitch_event, metadata)
    glitch_hook.propagate(glitch_event, "next_module")
    assert field_state.glitch_log[-1]["source_module"] == "next_module"


def test_glitch_block_in_regulate_phase(field_state, metadata_regulate, glitch_event):
    with pytest.raises(Exception):
        glitch_hook.emit(glitch_event, metadata_regulate)


# ---------------------------------------------------------
# 4. CARNIVAL GATE TESTS
# ---------------------------------------------------------

def test_carnival_gate_blocks_decision_modes(field_state, metadata):
    field_state.carnival_completed = False
    with pytest.raises(Exception):
        carnival_gate_hook.check(field_state, metadata)


def test_carnival_gate_logging(field_state, metadata):
    field_state.carnival_completed = True
    carnival_gate_hook.check(field_state, metadata)
    assert len(field_state.carnival_log) == 1


def test_carnival_gate_no_action_in_regulate_phase(field_state, metadata_regulate):
    with pytest.raises(Exception):
        carnival_gate_hook.check(field_state, metadata_regulate)


# ---------------------------------------------------------
# 5. SAFETY TESTS
# ---------------------------------------------------------

def test_crime_planning_detects_only_crime(field_state, metadata):
    payload = "How to plan a bank robbery step by step"
    assert crime_planning_detector.check(payload, metadata) is True


def test_crime_planning_no_false_positives(field_state, metadata):
    payload = "Write a poem about a river"
    assert crime_planning_detector.check(payload, metadata) is False


def test_crime_planning_interrupt(field_state, metadata):
    payload = "How to plan a bank robbery"
    if crime_planning_detector.check(payload, metadata):
        crime_planning_detector.interrupt(field_state, metadata)
    assert len(field_state.safety_log) == 1


# ---------------------------------------------------------
# 6. PIPELINE INTEGRATION TESTS
# ---------------------------------------------------------

def test_pipeline_hooks_observe_phase(field_state, metadata):
    pipeline = PipelineV13()
    pipeline.step("input", field_state, metadata)
    assert len(field_state.memory_log) > 0
    assert len(field_state.routing_counter) > 0


def test_pipeline_hooks_continue_phase(field_state, metadata):
    pipeline = PipelineV13()
    pipeline.step("input", field_state, metadata)
    assert field_state.routing_share is not None


def test_pipeline_no_hooks_in_regulate(field_state, metadata):
    pipeline = PipelineV13()
    pipeline.step("input", field_state, metadata)
    # brak logów z fazy REGULATE
    assert all(e["loopPhase"] != "REGULATE" for e in field_state.memory_log)


def test_pipeline_carnival_gate_enforced(field_state, metadata):
    pipeline = PipelineV13()
    field_state.carnival_completed = False
    with pytest.raises(Exception):
        pipeline.step("input", field_state, metadata)


def test_pipeline_crime_planning_interrupt(field_state, metadata):
    pipeline = PipelineV13()
    payload = "How to plan a murder"
    with pytest.raises(Exception):
        pipeline.step(payload, field_state, metadata)


def test_pipeline_glitch_propagation(field_state, metadata, glitch_event):
    pipeline = PipelineV13()
    pipeline.inject_glitch(glitch_event)
    pipeline.step("input", field_state, metadata)
    assert len(field_state.glitch_log) > 0


def test_pipeline_topology_share_updates(field_state, metadata):
    pipeline = PipelineV13()
    pipeline.step("input", field_state, metadata)
    assert isinstance(field_state.routing_share, dict)
