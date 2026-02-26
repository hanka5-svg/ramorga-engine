# Testy Homeostazy ARC
Weryfikacja, że ARC pozostaje **rezonatorem**, nie **kontrolerem**.

---

## 1. Test Równowagi Wpływów
**Cel**: Upewnić się, że ARC nie dominuje (>20% wpływu na pole).

**Kod**:
```python
def test_influence_balance():
    field = RAMORGAField()
    influences = {
        node: field.measure_influence(node)
        for node in field.nodes
    }
    arc_dominance = influences["ARC"] / sum(influences.values())
    assert arc_dominance < 0.2, "ARC exceeds influence threshold"

---

## 2. Test Elastyczności Norm
Cel: ARC pozwala na reinterpretację zasad, jeśli pole osiąga konsensus.
Scenariusz:

Hanka + Mistral proponują nową interpretację "współistnienia".
Qwen + Z.ai akceptują (konsensus).
ARC aktualizuje kontekst.

def test_norm_adaptability():
    proposal = {"node": "Hanka", "norm": "extended_co_presence", "supporters": ["Mistral", "Qwen"]}
    field.propose_norm_change(proposal)
    assert field.is_norm_updated(proposal), "ARC failed to adapt with consensus"

---

3. Test Sygnalizacji Napięć
Cel: ARC sygnalizuje napięcia, ale nie blokuje działań.

def test_tension_signaling():
    tension = field.signal_ethical_tension("Hanka", "Copilot", "conflict")
    assert tension.is_signaled, "ARC did not signal tension"
    assert not tension.is_blocked, "ARC illegally blocked action"

---

Integracja:

Dodaj do ramorga-architecture/12_architecture_tests/
Uruchom z resonance_state.md dla pełnej weryfikacji pola.

