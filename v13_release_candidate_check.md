# V13 Release Candidate Check — RC1 Gate
# RAMORGA ENGINE — Release Candidate Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje **formalną checklistę wejścia w etap Release Candidate (RC1)** dla architektury V13.
Jest to brama jakościowa (RC‑gate), która musi zostać w pełni spełniona przed oznaczeniem tagu:

**v13.0.0‑rc1**

Checklistę stosuje się po zakończeniu:
- stabilizacji (wg `v13_stabilization_tracker.md`),
- integracji (wg `v13_next_steps.md`),
- synchronizacji dokumentacji (wg `v13_status_summary.md`).

---

## 2. Kryteria RC1 — Implementacja (MUST PASS)

### 2.1. DataBridge
| Zadanie | Status |
|---------|--------|
| DataBridge.load działa | ☐ |
| DataBridge.save działa | ☐ |
| Mapowanie snapshot ↔ field_state kompletne | ☐ |
| Roundtrip snapshot stabilny | ☐ |

### 2.2. Field Engine
| Zadanie | Status |
|---------|--------|
| FieldEngine.step() zintegrowany z pipeline_v13 | ☐ |
| Kolejność regulatorów potwierdzona | ☐ |
| Brak skoków wartości (Continuity Model) | ☐ |

### 2.3. MeniscusEngine
| Zadanie | Status |
|---------|--------|
| receive/normalize/respond kompletne | ☐ |
| Integracja z pipeline_v13 | ☐ |

### 2.4. V12
| Zadanie | Status |
|---------|--------|
| regulatory V12 wyłączone | ☐ |
| drift działa zgodnie z drift_parameter_spec.md | ☐ |
| snapshot zgodny z ltm_snapshot_spec.md | ☐ |

---

## 3. Kryteria RC1 — Testy (MUST PASS)

### 3.1. Testy sekwencji
| Test | Status |
|------|--------|
| test_execution_sequence | ☐ |
| test_load_execute_save | ☐ |

### 3.2. Testy DataBridge
| Test | Status |
|------|--------|
| test_load_mapping | ☐ |
| test_save_mapping | ☐ |
| test_roundtrip_snapshot | ☐ |

### 3.3. Testy regulatorów
| Test | Status |
|------|--------|
| test_regulator_chain | ☐ |
| test_regulation_invariants | ☐ |
| test_no_v12_regulation | ☐ |

### 3.4. Testy automatu stanów
| Test | Status |
|------|--------|
| test_state_sequence | ☐ |
| test_state_transitions | ☐ |
| test_error_transitions | ☐ |

### 3.5. Testy ciągłości
| Test | Status |
|------|--------|
| test_roundtrip_field_state | ☐ |
| test_timestamp_monotonicity | ☐ |
| test_drift_continuity | ☐ |

---

## 4. Kryteria RC1 — Dokumentacja (MUST PASS)

### 4.1. Dokumenty wymagające synchronizacji
| Dokument | Status |
|----------|--------|
| execution_flow.md | ☐ |
| state_machine.md | ☐ |
| v13_release_checklist.md | ☐ |

### 4.2. Dokumenty wymagające potwierdzenia
| Dokument | Status |
|----------|--------|
| pipeline_v13_contract.md | ☐ |
| field_engine_contract.md | ☐ |
| integration_flow_v13.md | ☐ |
| v12_v13_data_bridge.md | ☐ |
| execution_bridge.md | ☐ |
| regulation_bridge.md | ☐ |

---

## 5. Kryteria RC1 — Stabilność (MUST PASS)

### 5.1. Snapshot
| Kryterium | Status |
|-----------|--------|
| brak utraty parametrów | ☐ |
| brak niespójności timestampów | ☐ |
| brak błędów serializacji | ☐ |

### 5.2. Drift
| Kryterium | Status |
|-----------|--------|
| drift_rate stabilny | ☐ |
| drift_bounds respektowane | ☐ |
| brak skoków wartości | ☐ |

### 5.3. Regulator Chain
| Kryterium | Status |
|-----------
