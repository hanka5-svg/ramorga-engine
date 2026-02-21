# V13 Next Steps — Stabilization & Integration Plan
# RAMORGA ENGINE — Stabilization Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje **kolejne kroki** wymagane do wejścia w etap stabilizacji V13.
Obejmuje:
- priorytety implementacyjne,
- priorytety testowe,
- synchronizację dokumentacji,
- integrację mostów V12 ↔ V13,
- kryteria wejścia w etap stabilizacji.

Dokument jest kontynuacją `v13_status_summary.md`.

---

## 2. Priorytety implementacyjne (HIGH)

### 2.1. DataBridge (krytyczne)
- [ ] implementacja `DataBridge.load(snapshot)`
- [ ] implementacja `DataBridge.save(field_state)`
- [ ] walidacja roundtrip snapshot ↔ field_state
- [ ] integracja z V12 (LTM.read/write)

**Dlaczego:**  
Bez DataBridge nie istnieje realny przepływ danych V12 ↔ V13.

---

### 2.2. Integracja Field Engine z PipelineV13
- [ ] dodanie wywołania `FieldEngine.step()` w pipeline_v13
- [ ] potwierdzenie kolejności regulatorów
- [ ] walidacja inwariantów regulacji po każdym kroku

**Dlaczego:**  
To jest serce regulacji pola — bez tego V13 nie jest funkcjonalne.

---

### 2.3. Wyłączenie regulatorów V12
- [ ] usunięcie/wyłączenie legacy regulation w 01_runtime/
- [ ] potwierdzenie, że V12 wykonuje tylko: LTM + drift

**Dlaczego:**  
Podwójna regulacja = naruszenie Continuity Model.

---

### 2.4. Integracja MeniscusEngine
- [ ] implementacja receive/normalize/respond
- [ ] integracja z pipeline_v13
- [ ] walidacja ATML na wejściu

**Dlaczego:**  
Meniscus jest bramą wejścia/wyjścia — bez niego pipeline nie jest wywoływalny.

---

## 3. Priorytety testowe (HIGH)

### 3.1. Testy sekwencji wykonania
- [ ] `test_execution_sequence`
- [ ] `test_load_execute_save`

### 3.2. Testy DataBridge
- [ ] `test_load_mapping`
- [ ] `test_save_mapping`
- [ ] `test_roundtrip_snapshot`

### 3.3. Testy regulatorów
- [ ] `test_regulator_chain`
- [ ] `test_regulation_invariants`
- [ ] `test_no_v12_regulation`

### 3.4. Testy automatu stanów
- [ ] `test_state_sequence`
- [ ] `test_state_transitions`
- [ ] `test_error_transitions`

---

## 4. Synchronizacja dokumentacji (MEDIUM)

### 4.1. Dokumenty wymagające aktualizacji
- [ ] execution_flow.md  
- [ ] state_machine.md  
- [ ] v13_release_checklist.md  

### 4.2. Dokumenty wymagające potwierdzenia
- [ ] integration_flow_v13.md  
- [ ] pipeline_v13_contract.md  
- [ ] field_engine_contract.md  

---

## 5. Stabilizacja architektury (MEDIUM)

### 5.1. Stabilizacja snapshotu
- [ ] potwierdzenie spójności snapshotu z field_state
- [ ] walidacja timestamp monotonicity

### 5.2. Stabilizacja drift
- [ ] walidacja drift_bounds
- [ ] test_drift_continuity

### 5.3. Stabilizacja regulatorów
- [ ] potwierdzenie deterministyczności
- [ ] walidacja braku skoków wartości

---

## 6. Kryteria wejścia w etap stabilizacji

### 6.1. Implementacja
- [ ] DataBridge działa w pełnym zakresie
- [ ] FieldEngine zintegrowany z pipeline_v13
- [ ] regulatory V12 wyłączone
- [ ] MeniscusEngine zintegrowany

### 6.2. Testy
- [ ] 100% testów R1 (core regression) przechodzi
- [ ] 80% testów R2–R4 przechodzi
- [ ] brak naruszeń inwariantów

### 6.3. Dokumentacja
- [ ] execution_flow.md zsynchronizowany
- [ ] state_machine.md zsynchronizowany
- [ ] release_checklist zaktualizowany

---

## 7. Podsumowanie
Etap stabilizacji V13 wymaga:
- implementacji DataBridge,
- integracji Field Engine,
- wyłączenia regulatorów V12,
- pełnych testów sekwencji i ciągłości,
- synchronizacji dokumentacji.

Po wykonaniu powyższych kroków V13 przechodzi do fazy:
**V13 Integration & Stabilization → V13 Pre‑Release**.

---
