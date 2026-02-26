# FIELD.RELATION.001 — Carnival Gate
# CI BLOCKER — merge blocked if violated

def test_carnival_state_exists():
    from runtime.field_state import field_state
    assert "carnival_completed" in field_state, "carnival_completed missing"
    assert "carnival_log" in field_state, "carnival_log missing"


def test_carnival_gate_hook_has_check():
    import runtime.carnival_gate_hook as c
    assert hasattr(c, "check"), "carnival_gate_hook missing check()"
