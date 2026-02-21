# PipelineV13 Flowchart (Text-Only)
# RAMORGA ENGINE — Execution Flow Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument przedstawia **tekstowy flowchart** dla PipelineV13 — głównego pipeline wykonania
w ramorga-engine. Flowchart opisuje:
- sekwencję kroków,
- punkty integracji,
- przepływ danych,
- powiązania z MeniscusEngine, Field Engine, DataBridge i V12.

Flowchart jest zgodny z:
- state_machine.md  
- execution_flow.md  
- integration_flow_v13.md  
- pipeline_v13_contract.md  

---

## 2. Flowchart — pełna sekwencja (tekstowa)

┌──────────────────────────────────────────────────────────────┐
│ 1. INIT (MeniscusEngine)                                      │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 2. RECEIVE INPUT                                              │
│    - MeniscusEngine.receive()                                 │
│    - surowy input_payload                                     │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 3. VALIDATE + NORMALIZE                                       │
│    - walidacja ATML                                           │
│    - normalizacja danych                                      │
│    - output: normalized_payload                               │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 4. LOAD (V12 → V13)                                           │
│    - snapshot = LTM.read()                                    │
│    - field_state = DataBridge.load(snapshot)                  │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 5. PREPARE (opcjonalne)                                       │
│    - wstępne przetwarzanie danych                             │
│    - aktualizacja field_state (bez regulacji pola)            │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 6. EXECUTE_PIPELINE                                           │
│    - PipelineV13.step(normalized_payload, field_state)        │
│    - logika pipeline                                          │
│    - brak regulacji pola                                      │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 7. EXECUTE_FIELD_ENGINE                                       │
│    - tension_loop.run()                                       │
│    - energy_regulator.adjust()                                │
│    - entropic_modulator.modulate()                            │
│    - FieldEngine.step()                                       │
│    - aktualizacja field_state                                 │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 8. SAVE (V13 → V12)                                           │
│    - snapshot = DataBridge.save(field_state)                  │
│    - LTM.write(snapshot)                                      │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 9. RESPOND (MeniscusEngine)                                   │
│    - formatowanie output_payload                              │
│    - MeniscusEngine.respond()                                 │
└──────────────────────────────────────────────────────────────┘
│
▼
┌──────────────────────────────────────────────────────────────┐
│ 10. END                                                       │
└──────────────────────────────────────────────────────────────┘

---

## 3. Punkty integracji

### 3.1. MeniscusEngine → PipelineV13
- wejście: normalized_payload  
- brak dostępu do V12 i regulatorów  

### 3.2. PipelineV13 → Field Engine
- wywołanie FieldEngine.step()  
- brak regulacji w pipeline  

### 3.3. Field Engine → Regulatory
- kolejność stała: tension → energy → entropy  

### 3.4. PipelineV13 → DataBridge → V12
- LOAD przed step()  
- SAVE po FieldEngine.step()  

---

## 4. Inwarianty flowchartu
- LOAD zawsze przed EXECUTE_PIPELINE  
- EXECUTE_FIELD_ENGINE zawsze po EXECUTE_PIPELINE  
- SAVE zawsze po EXECUTE_FIELD_ENGINE  
- RESPOND zawsze po SAVE  
- brak pomijania regulatorów  
- brak bezpośrednich wywołań V12 poza DataBridge  

---

## 5. Wymagania implementacyjne
1. PipelineV13 musi implementować pełną sekwencję kroków.  
2. MeniscusEngine musi inicjalizować INIT i finalizować RESPOND.  
3. Field Engine musi wykonywać pełną regulację pola.  
4. DataBridge musi obsługiwać LOAD/SAVE.  
5. V12 musi zapewniać spójny snapshot.  
6. Testy muszą pokrywać pełną sekwencję flowchartu.  

---

## 6. Status implementacji
- pipeline_v13: wymaga pełnej integracji flow  
- Field Engine: istnieje, wymaga integracji z pipeline  
- MeniscusEngine: skeleton  
- DataBridge: brak implementacji  
- V12: istnieje, wymaga synchronizacji snapshotu  
- testy: brak pokrycia sekwencji  

---
