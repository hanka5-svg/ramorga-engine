# Coverage Alignment — V13 Architecture
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalne powiązanie pomiędzy:
- istniejącymi testami w repo,
- planem testów (test_plan.md),
- macierzą pokrycia (test_matrix.md),
- kontraktami V13 (pipeline, field engine, meniscus, data bridge, regulation bridge),
- automatem stanów (state_machine.md),
- przepływem wykonania (execution_flow.md).

Celem jest zapewnienie pełnego, mierzalnego i audytowalnego pokrycia testowego
dla architektury V13.

---

## 2. Zakres
Dokument obejmuje moduły:

pipeline_v13/
03_field_engine/
tension_loop/
energy_regulator/
field_state/
src/ramorga_engine/entropic_modulator.py
04_meniscus_engine/
01_runtime/
data_bridge (planowany)

oraz dokumenty:

test_plan.md
test_matrix.md
state_machine.md
execution_flow.md
*_contract.md
*_bridge.md

---

## 3. Kategorie pokrycia
### 3.1. T1 — Unit Tests
Testy jednostkowe dla:
- regulatorów,
- field_state,
- DataBridge,
- LTM + drift,
- pipeline utils.

### 3.2. T2 — Integration Tests
Testy integracyjne dla:
- PipelineV13 ↔ Field Engine,
- Field Engine ↔ regulatory,
- PipelineV13 ↔ DataBridge ↔ V12,
- MeniscusEngine ↔ PipelineV13.

### 3.3. T3 — Execution Flow Tests
Testy sekwencji:
- INIT → LOAD → EXECUTE_PIPELINE → EXECUTE_FIELD_ENGINE → SAVE → RESPOND → END.

### 3.4. T4 — State Machine Compliance
Testy zgodności z automatem stanów:
- poprawne przejścia,
- błędne przejścia,
- stan ERROR,
- inwarianty stanów.

---

## 4. Mapa pokrycia (Coverage Map)
### 4.1. Moduły pokryte testami (stan obecny)

energy_regulator/ (test_energy_regulator.py)
field_state/ (test_field_state.py)
entropic_modulator/ (test_entropic_modulator.py)

### 4.2. Moduły bez pokrycia (wymagane)

pipeline_v13/
03_field_engine/
tension_loop/
04_meniscus_engine/
01_runtime/ (LTM + drift)
data_bridge/

---

## 5. Powiązanie testów z kontraktami
### 5.1. Kontrakty wymagające pokrycia
- pipeline_v13_contract.md
- field_engine_contract.md
- meniscus_contract.md
- regulation_bridge.md
- execution_bridge.md
- v12_v13_data_bridge.md
- ltm_drift_contract.md
- error_model_contract.md
- state_machine_alignment.md

### 5.2. Wymagane testy dla każdego kontraktu
| Kontrakt | Wymagane testy |
|----------|----------------|
| pipeline_v13_contract | test_pipeline_step_sequence, test_pipeline_invariants |
| field_engine_contract | test_field_engine_sequence, test_regulator_integration |
| meniscus_contract | test_meniscus_normalization, test_meniscus_execution_flow |
| regulation_bridge | test_regulation_sequence, test_no_v12_regulation |
| execution_bridge | test_load_execute_save, test_execution_invariants |
| v12_v13_data_bridge | test_load_mapping, test_save_mapping, test_roundtrip |
| ltm_drift_contract | test_ltm_read_write, test_drift_update |
| error_model_contract | test_error_propagation, test_error_output_format |
| state_machine_alignment | test_state_sequence, test_state_transitions |

---

## 6. Powiązanie testów z automatem stanów
### 6.1. Stany wymagające pokrycia

INIT
LOAD
PREPARE
EXECUTE_PIPELINE
EXECUTE_FIELD_ENGINE
SAVE
RESPOND
END
ERROR

### 6.2. Wymagane testy
- test_state_sequence
- test_state_invariants
- test_state_transitions
- test_error_transitions

---

## 7. Powiązanie testów z execution_flow.md
### 7.1. Wymagane testy
- test_execution_sequence
- test_load_execute_save
- test_meniscus_pipeline_integration
- test_pipeline_field_engine_integration
- test_ltm_pipeline_integration

---

## 8. Inwarianty pokrycia
### 8.1. Inwarianty strukturalne
- każdy kontrakt musi mieć co najmniej jeden test T1–T4,
- każdy stan automatu musi mieć test przejścia,
- każdy moduł musi mieć test jednostkowy.

### 8.2. Inwarianty wykonania
- testy muszą pokrywać pełną sekwencję wykonania,
- testy muszą wykrywać naruszenia inwariantów,
- testy muszą wykrywać błędne przejścia.

### 8.3. Inwarianty ciągłości
- brak „martwych modułów” bez testów,
- brak „martwych stanów” bez testów,
- brak „martwych kontraktów” bez testów.

---

## 9. Wymagania implementacyjne
1. Utworzenie brakujących testów T1–T4.  
2. Dodanie testów DataBridge.  
3. Dodanie testów MeniscusEngine.  
4. Dodanie testów PipelineV13.  
5. Dodanie testów Field Engine.  
6. Aktualizacja test_matrix.md.  
7. Aktualizacja coverage_map.md.  

---

## 10. Status implementacji
- testy regulatorów: istnieją,  
- testy field_state: istnieją,  
- testy entropic_modulator: istnieją,  
- testy pipeline_v13: brak,  
- testy Field Engine: brak,  
- testy MeniscusEngine: brak,  
- testy DataBridge: brak,  
- testy V12: częściowe,  
- testy stanów: brak,  
- testy przepływu: brak.

---
