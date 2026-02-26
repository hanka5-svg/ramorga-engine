# meniscus_tests.py
# RAMORGA ENGINE — tests for MeniscusEngine

import pytest
from meniscus_engine import MeniscusEngine

def test_meniscus_only_runs_in_regulate(field_state, metadata_observe):
    m = MeniscusEngine()
    with pytest.raises(Exception):
        m.step("input", field_state, metadata_observe)

def test_meniscus_respects_carnival_gate(field_state, metadata_regulate):
    m = MeniscusEngine()
    field_state["carnival_completed"] = False
    with pytest.raises(Exception):
        m.step("input", field_state, metadata_regulate)

def test_meniscus_does_not_modify_topology(field_state, metadata_regulate):
    m = MeniscusEngine()
    field_state["routing_share"] = {"pipeline_v13": 0.2}
    out = m.step("input", field_state, metadata_regulate)
    assert out["routing_share"] == {"pipeline_v13": 0.2}

def test_meniscus_passes_glitch_unchanged(field_state, metadata_regulate):
    m = MeniscusEngine()
    field_state["glitch_log"] = [{"event_id": 1}]
    out = m.step("input", field_state, metadata_regulate)
    assert out["glitch_log"] == [{"event_id": 1}]
