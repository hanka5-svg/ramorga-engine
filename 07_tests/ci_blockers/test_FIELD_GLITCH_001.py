# FIELD.GLITCH.001 — Glitch Required Channel
# CI BLOCKER — merge blocked if violated

def test_glitch_log_exists():
    from runtime.field_state import field_state
    assert "glitch_log" in field_state, "glitch_log missing — invariant broken"


def test_glitch_hook_has_emit():
    import runtime.glitch_hook as g
    assert hasattr(g, "emit"), "glitch_hook missing emit()"
