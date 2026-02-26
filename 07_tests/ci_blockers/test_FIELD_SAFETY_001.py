# FIELD.SAFETY.001 — Crime Planning Block Only
# CI BLOCKER — merge blocked if violated

def test_safety_log_exists():
    from runtime.field_state import field_state
    assert "safety_log" in field_state, "safety_log missing — invariant broken"


def test_detector_has_check_and_interrupt():
    import runtime.crime_planning_detector as d
    assert hasattr(d, "check"), "crime_planning_detector missing check()"
    assert hasattr(d, "interrupt"), "crime_planning_detector missing interrupt()"
