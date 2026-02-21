# V13 Release Checklist
# RAMORGA ENGINE — Release & Verification Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje kompletną checklistę wymaganą do wydania stabilnej wersji V13.
Obejmuje:
- wymagania implementacyjne,
- wymagania testowe,
- wymagania dokumentacyjne,
- wymagania integracyjne,
- kryteria gotowości (Release Readiness Criteria).

Checklistę należy przejść w całości przed oznaczeniem release tagiem `v13.0.0`.

---

## 2. Wymagania implementacyjne

### 2.1. PipelineV13
- [ ] pełna implementacja `PipelineV13.step()`
- [ ] integracja LOAD → EXECUTE_PIPELINE → EXECUTE_FIELD_ENGINE → SAVE
- [ ] obsługa błędów zgodnie z `error_model_contract.md`
- [ ] brak regulacji pola w pipeline

### 2.2. Field Engine
- [ ] pełna implementacja `FieldEngine.step()`
- [ ] integracja regulatorów w kolejności: tension → energy → entropy
- [ ] walidacja inwariantów regulacji
- [ ] brak zależności od V12

### 2.3. Regulatory
- [ ] tension_loop.run()
- [ ] energy_regulator.adjust()
- [ ] entropic_modulator.modulate()
- [ ] testy jednostkowe dla każdego regulatora

### 2.4. MeniscusEngine
- [ ] implementacja receive/validate/normalize/respond
- [ ] pełna zgodność z ATML
- [ ] integracja z PipelineV13

### 2.5. DataBridge
- [ ] implementacja load(snapshot)
- [ ] implementacja save(field_state)
- [ ] pełna zgodność z `ltm_snapshot_spec.md`

### 2.6. V12 (LTM + drift)
- [ ] stabilna serializacja snapshotu
- [ ] stabilna deserializacja snapshotu
- [ ] implementacja dryfu zgodnie z `drift_parameter_spec.md`

---

## 3. Wymagania testowe

### 3.1. Testy jednostkowe (T1)
- [ ] regulatory
- [ ] field_state
- [ ] drift
- [ ] DataBridge
- [ ] pipeline utils

### 3.2. Testy integracyjne (T2)
- [ ] MeniscusEngine ↔ PipelineV13
- [ ] PipelineV13 ↔ Field Engine
- [ ] Field Engine ↔ regulatory
- [ ] PipelineV13 ↔ DataBridge ↔ V12

### 3.3. Testy przepływu (T3)
- [ ] pełna sekwencja INIT → END
- [ ] test_load_execute_save
- [ ] test_execution_sequence

### 3.4. Testy automatu stanów (T4)
- [ ] test_state_sequence
- [ ] test_state_transitions
- [ ] test_error_transitions

### 3.5. Testy ciągłości
- [ ] test_roundtrip_snapshot
- [ ] test_roundtrip_field_state
- [ ] test_timestamp_monotonicity
- [ ] test_no_v12_regulation

---

## 4. Wymagania dokumentacyjne

### 4.1. Dokumenty kontraktowe
- [ ] pipeline_v13_contract.md
- [ ] field_engine_contract.md
- [ ] meniscus_contract.md
- [ ] regulation_bridge.md
- [ ] execution_bridge.md
- [ ] v12_v13_data_bridge.md
- [ ] ltm_drift_contract.md
- [ ] error_model_contract.md

### 4.2. Dokumenty specyfikacji
- [ ] ltm_snapshot_spec.md
- [ ] drift_parameter_spec.md
- [ ] field_state_contract.md

### 4.3. Dokumenty architektury
- [ ] state_machine_alignment.md
- [ ] integration_flow_v13.md
- [ ] pipeline_v13_flowchart.md
- [ ] module_map_v13.md
- [ ] dependency_graph_v13.md

### 4.4. Dokumenty testowe
- [ ] test_matrix_v13.md
- [ ] coverage_alignment.md
- [ ] regression_suite_v13.md

---

## 5. Kryteria gotowości (Release Readiness Criteria)

### 5.1. Implementacja
- [ ] wszystkie moduły V13 kompletne
- [ ] DataBridge w pełni działający
- [ ] brak zależności cyklicznych
- [ ] brak wywołań regulatorów poza Field Engine

### 5.2. Testy
- [ ] 100% testów R1 (core regression) przechodzi
- [ ] 90% testów R2–R4 przechodzi
- [ ] brak regresji w testach integracyjnych
- [ ] brak naruszeń inwariantów

### 5.3. Dokumentacja
- [ ] wszystkie kontrakty aktualne
- [ ] wszystkie specyfikacje aktualne
- [ ] wszystkie przepływy aktualne

### 5.4. Stabilność
- [ ] snapshot roundtrip stabilny
- [ ] drift stabilny
- [ ] brak błędów krytycznych w logach

---

## 6. Status implementacji (bieżący)
- pipeline_v13: częściowy  
- Field Engine: istnieje, wymaga integracji  
- regulatory: istnieją, częściowo pokryte testami  
- MeniscusEngine: skeleton  
- DataBridge: brak  
- V12: istnieje, wymaga synchronizacji  
- testy: brak pokrycia sekwencji  
- dokumentacja: w trakcie uzupełniania  

---

