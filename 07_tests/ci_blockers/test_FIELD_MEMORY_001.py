# FIELD.MEMORY.001 — Memory as Field, not Store
# CI BLOCKER — merge blocked if violated

def test_no_prediction_interfaces():
    import runtime.memory_audit_hook as m
    assert not hasattr(m, "predict"), "Prediction interface detected — violation of FIELD.MEMORY.001"


def test_no_optimisation_interfaces():
    import runtime.memory_audit_hook as m
    forbidden = ["optimize", "improve", "score", "rank"]
    for f in forbidden:
        assert not hasattr(m, f), f"Forbidden optimisation interface '{f}' detected"
