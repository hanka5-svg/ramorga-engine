# V13 Pre‑Release Plan — Final Integration & Verification Phase
# RAMORGA ENGINE — Pre‑Release Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje plan wejścia w etap **V13 Pre‑Release** — ostatnią fazę przed wydaniem stabilnej wersji V13.
Obejmuje:
- finalne integracje,
- finalne testy,
- stabilizację przepływów,
- synchronizację dokumentacji,
- kryteria wejścia w pre‑release,
- kryteria wyjścia (release readiness).

Plan jest kontynuacją:
- `v13_status_summary.md`
- `v13_next_steps.md`
- `v13_stabilization_tracker.md`

---

## 2. Zakres etapu Pre‑Release
Etap obejmuje:

1. **Finalną integrację V12 ↔ V13**  
2. **Stabilizację Field Engine i regulatorów**  
3. **Stabilizację snapshotu i driftu**  
4. **Pełne testy sekwencji i ciągłości**  
5. **Synchronizację dokumentacji**  
6. **Przygotowanie release tagu `v13.0.0-rc1`**

---

## 3. Priorytety Pre‑Release (HIGH)

### 3.1. DataBridge — finalizacja
- [ ] implementacja load/save  
- [ ] walidacja mapowania snapshot ↔ field_state  
- [ ] test_roundtrip_snapshot  
- [ ] test_load_mapping / test_save_mapping  

**Bez DataBridge nie ma pre‑release.**

---

### 3.2. Integracja Field Engine
- [ ] wywołanie FieldEngine.step() w pipeline_v13  
- [ ] walidacja kolejności regulatorów  
- [ ] test_regulator_chain  
- [ ] test_regulation_invariants  

**To jest serce V13.**

---

### 3.3. Wyłączenie regulatorów V12
- [ ] usunięcie legacy regulation  
- [ ] test_no_v12_regulation  

**Warunek Continuity Model.**

---

### 3.4. Stabilizacja snapshotu i driftu
- [ ] test_timestamp_monotonicity  
- [ ] test_drift_continuity  
- [ ] walidacja drift_bounds  

---

### 3.5. MeniscusEngine — finalizacja wejścia/wyjścia
- [ ] implementacja receive/normalize/respond  
- [ ] integracja z pipeline_v13  
- [ ] test_meniscus_entry_exit  

---

## 4. Testy wymagane do wejścia w Pre‑Release

### 4.1. Testy sekwencji (krytyczne)
- [ ] test_execution_sequence  
- [ ] test_load_execute_save  

### 4.2. Testy integracyjne
- [ ] pipeline_v13 ↔ field_engine  
- [ ] pipeline_v13 ↔ DataBridge ↔ V12  
- [ ] meniscus ↔ pipeline_v13  

### 4.3. Testy ciągłości
- [ ] test_roundtrip_snapshot  
- [ ] test_roundtrip_field_state  

### 4.4. Testy automatu stanów
- [ ] test_state_sequence  
- [ ] test_state_transitions  
- [ ] test_error_transitions  

---

## 5. Dokumentacja do synchronizacji

### 5.1. Dokumenty wymagające aktualizacji
- [ ] execution_flow.md  
- [ ] state_machine.md  
- [ ] v13_release_checklist.md  

### 5.2. Dokumenty wymagające potwierdzenia
- [ ] integration_flow_v13.md  
- [ ] pipeline_v13_contract.md  
- [ ] field_engine_contract.md  

---

## 6. Kryteria wejścia w etap Pre‑Release

### 6.1. Implementacja
- [ ] DataBridge działa  
- [ ] FieldEngine zintegrowany z pipeline_v13  
- [ ] regulatory V12 wyłączone  
- [ ] MeniscusEngine zintegrowany  

### 6.2. Testy
- [ ] 100% testów R1 (core regression) przechodzi  
- [ ] 80% testów R2–R4 przechodzi  
- [ ] test_execution_sequence przechodzi  
- [ ] test_roundtrip_snapshot przechodzi  

### 6.3. Dokumentacja
- [ ] execution_flow.md zsynchronizowany  
- [ ] state_machine.md zsynchronizowany  
- [ ] release_checklist zaktualizowany  

---

## 7. Kryteria wyjścia (Release Readiness)

### 7.1. Stabilność
- [ ] snapshot stabilny  
- [ ] drift stabilny  
- [ ] regulator chain stabilny  

### 7.2. Integracja
- [ ] pełna sekwencja INIT → END działa deterministycznie  
- [ ] brak naruszeń inwariantów  

### 7.3. Testy
- [ ] 100% testów R1–R3 przechodzi  
- [ ] 95% testów R4 przechodzi  

### 7.4. Dokumentacja
- [ ] wszystkie kontrakty aktualne  
- [ ] wszystkie specyfikacje aktualne  
- [ ] wszystkie przepływy aktualne  

---

## 8. Podsumowanie
Etap Pre‑Release jest ostatnią fazą przed wydaniem `v13.0.0-rc1`.  
Wymaga:
- finalnej integracji DataBridge i Field Engine,  
- pełnych testów sekwencji i ciągłości,  
- synchronizacji dokumentacji,  
- potwierdzenia stabilności regulatorów i snapshotu.

Po spełnieniu kryteriów V13 przechodzi do:
**V13 Release Candidate → v13.0.0.**

---
