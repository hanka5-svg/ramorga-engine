# Regression Suite — V13 Architecture
# RAMORGA ENGINE — Quality & Stability Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje pełny zestaw testów regresyjnych (Regression Suite) dla architektury V13.
Celem regresji jest:
- wykrywanie regresji funkcjonalnych,
- utrzymanie stabilności systemu,
- zapewnienie zgodności z kontraktami V13,
- potwierdzenie ciągłości działania po zmianach w kodzie.

Regression Suite jest wykonywany po:
- każdej zmianie w pipeline_v13/,
- każdej zmianie w Field Engine lub regulatorach,
- każdej zmianie w DataBridge,
- każdej zmianie w LTM + drift,
- każdej zmianie w MeniscusEngine,
- każdej zmianie w state_machine.md lub execution_flow.md.

---

## 2. Zakres regresji
Regression Suite obejmuje moduły:

pipeline_v13/
03_field_engine/
tension_loop/
energy_regulator/
src/ramorga_engine/entropic_modulator.py
field_state/
04_meniscus_engine/
01_runtime/ (LTM + drift)
data_bridge/

oraz dokumenty:

*_contract.md
*_bridge.md
state_machine.md
execution_flow.md
test_matrix_v13.md

---

## 3. Struktura Regression Suite
Regression Suite składa się z czterech warstw:

### 3.1. R1 — Core Regression
Testy krytyczne, które muszą przejść zawsze:
- test_pipeline_step_sequence  
- test_field_engine_sequence  
- test_regulator_chain  
- test_load_execute_save  
- test_state_sequence  
- test_error_transitions  

### 3.2. R2 — Contract Regression
Testy zgodności z kontraktami:
- pipeline_v13_contract  
- field_engine_contract  
- meniscus_contract  
- regulation_bridge  
- execution_bridge  
- ltm_drift_contract  
- error_model_contract  
- data_bridge_contract  

### 3.3. R3 — Integration Regression
Testy integracyjne:
- test_meniscus_pipeline_integration  
- test_pipeline_field_engine_integration  
- test_ltm_pipeline_integration  
- test_data_bridge_pipeline  
- test_regulator_integration  

### 3.4. R4 — Continuity Regression
Testy ciągłości:
- test_roundtrip_snapshot  
- test_roundtrip_field_state  
- test_timestamp_monotonicity  
- test_drift_continuity  
- test_no_v12_regulation  

---

## 4. Macierz regresji (Regression Matrix)

| Warstwa | Test | Moduły | Status |
|--------|------|--------|--------|
| R1 | test_pipeline_step_sequence | pipeline_v13 | BRAK |
| R1 | test_field_engine_sequence | field_engine | BRAK |
| R1 | test_regulator_chain | tension/energy/entropy | CZĘŚCIOWE |
| R1 | test_load_execute_save | pipeline_v13 + V12 | BRAK |
| R1 | test_state_sequence | pipeline_v13 | BRAK |
| R1 | test_error_transitions | error_model | BRAK |
| R2 | test_pipeline_invariants | pipeline_v13 | BRAK |
| R2 | test_field_engine_invariants | field_engine | BRAK |
| R2 | test_meniscus_normalization | meniscus | BRAK |
| R2 | test_data_bridge_contract | data_bridge | BRAK |
| R2 | test_ltm_drift_contract | V12 | CZĘŚCIOWE |
| R3 | test_meniscus_pipeline_integration | meniscus + pipeline | BRAK |
| R3 | test_pipeline_field_engine_integration | pipeline + field_engine | BRAK |
| R3 | test_ltm_pipeline_integration | pipeline + V12 | BRAK |
| R3 | test_regulator_integration | field_engine + regulators | BRAK |
| R4 | test_roundtrip_snapshot | V12 + DataBridge | BRAK |
| R4 | test_roundtrip_field_state | field_state + DataBridge | BRAK |
| R4 | test_timestamp_monotonicity | V12 | BRAK |
| R4 | test_drift_continuity | drift | CZĘŚCIOWE |
| R4 | test_no_v12_regulation | V12 | BRAK |

---

## 5. Kryteria przejścia (Pass Criteria)
### 5.1. Kryteria minimalne
- wszystkie testy R1 muszą przejść,
- brak błędów krytycznych w R2,
- brak regresji w R3.

### 5.2. Kryteria pełne
- wszystkie testy R1–R4 przechodzą,
- brak ostrzeżeń dotyczących ciągłości,
- brak naruszeń kontraktów.

---

## 6. Inwarianty Regression Suite
### 6.1. Inwarianty strukturalne
- każdy moduł musi mieć co najmniej jeden test regresyjny,
- każdy kontrakt musi być pokryty testem regresyjnym.

### 6.2. Inwarianty wykonania
- regresja musi wykrywać naruszenia sekwencji,
- regresja musi wykrywać naruszenia inwariantów,
- regresja musi wykrywać błędne przejścia stanów.

### 6.3. Inwarianty ciągłości
- brak utraty snapshotów,
- brak utraty parametrów,
- brak pomijania regulatorów.

---

## 7. Wymagania implementacyjne
1. Utworzenie brakujących testów R1–R4.  
2. Dodanie testów DataBridge.  
3. Dodanie testów MeniscusEngine.  
4. Dodanie testów PipelineV13.  
5. Dodanie testów Field Engine.  
6. Aktualizacja test_matrix_v13.md i coverage_alignment.md.  

---

## 8. Status implementacji
- testy regulatorów: częściowe,  
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
