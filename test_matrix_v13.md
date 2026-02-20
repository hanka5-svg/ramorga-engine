# Test Matrix — V13 Architecture
# RAMORGA ENGINE — Quality & Verification Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje macierz testów (Test Matrix) dla architektury V13 w ramorga-engine.
Macierz łączy:
- moduły,
- kontrakty,
- typy testów (T1–T4),
- wymagane przypadki testowe,
- status pokrycia.

Celem jest zapewnienie pełnej, mierzalnej i audytowalnej weryfikacji systemu.

---

## 2. Kategorie testów
### T1 — Unit Tests
Testy jednostkowe modułów.

### T2 — Integration Tests
Testy integracji między modułami.

### T3 — Execution Flow Tests
Testy sekwencji wykonania.

### T4 — State Machine Compliance
Testy zgodności z automatem stanów.

---

## 3. Macierz testów (Test Matrix)

| Moduł / Kontrakt | T1 Unit | T2 Integracja | T3 Flow | T4 State Machine | Status |
|------------------|---------|---------------|---------|------------------|--------|
| **pipeline_v13/** | test_pipeline_utils, test_pipeline_errors | test_pipeline_field_engine_integration | test_pipeline_sequence | test_state_sequence | BRAK |
| **03_field_engine/** | test_field_engine_core | test_field_engine_regulators | test_field_engine_flow | test_state_transitions | BRAK |
| **tension_loop/** | test_tension_loop | test_regulator_chain | — | — | CZĘŚCIOWE |
| **energy_regulator/** | test_energy_regulator | test_regulator_chain | — | — | ISTNIEJE |
| **entropic_modulator.py** | test_entropic_modulator | test_regulator_chain | — | — | ISTNIEJE |
| **field_state/** | test_field_state | — | test_field_state_flow | — | ISTNIEJE |
| **04_meniscus_engine/** | test_meniscus_normalization | test_meniscus_pipeline_integration | test_meniscus_flow | test_state_init | BRAK |
| **01_runtime/ (LTM + drift)** | test_ltm_read_write, test_drift_update | test_ltm_pipeline_integration | test_load_save_flow | — | CZĘŚCIOWE |
| **DataBridge** | test_load_mapping, test_save_mapping | test_data_bridge_pipeline | test_roundtrip | — | BRAK |
| **execution_bridge.md** | — | test_load_execute_save | test_execution_sequence | test_state_sequence | BRAK |
| **regulation_bridge.md** | — | test_regulation_sequence | test_regulation_flow | — | BRAK |
| **error_model_contract.md** | test_error_format | test_error_propagation | test_error_flow | test_error_transitions | BRAK |
| **state_machine_alignment.md** | — | — | test_state_machine_flow | test_state_machine_compliance | BRAK |
| **coverage_alignment.md** | — | — | — | — | META |

---

## 4. Minimalny zestaw testów wymagany
