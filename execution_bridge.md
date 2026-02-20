# Execution Bridge: PipelineV12 ↔ PipelineV13
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny most wykonania pomiędzy:
- PipelineV12 (01_runtime/) — warstwa pamięci i dryfu,
- PipelineV13 (pipeline_v13/) — główny pipeline wykonania,
- Field Engine (03_field_engine/) — warstwa regulacji pola.

Most wykonania określa:
- kolejność kroków,
- punkty wywołań,
- zasady synchronizacji,
- wymagane interfejsy,
- inwarianty wykonania.

---

## 2. Lokalizacja modułów w repo
### 2.1. V12 — runtime

01_runtime/

### 2.2. V13 — pipeline modularny

pipeline_v13/

### 2.3. Field Engine

03_field_engine/
tension_loop/
energy_regulator/
field_state/
src/ramorga_engine/entropic_modulator.py

### 2.4. Meniscus Engine (wejście/wyjście)

04_meniscus_engine/
05_api/
06_integration/

---

## 3. Model wykonania (Execution Model)
### 3.1. Architektura docelowa

[API/Integration]
↓
04_meniscus_engine/
↓
pipeline_v13/
↓
03_field_engine/
↓
01_runtime/ (LTM + drift)

### 3.2. Zasada nadrzędna
PipelineV13 jest **jedynym** pipeline wykonania.  
PipelineV12 jest **wyłącznie** warstwą pamięci i dryfu.

---

## 4. Punkty wywołań (Execution Hooks)
### 4.1. HOOK 1 — LOAD (V12 → V13)
Wywoływany przed każdym krokiem pipeline V13.

snapshot = V12.LTM.read(state_id)
field_state = DataBridge.load(snapshot)

### 4.2. HOOK 2 — EXECUTE (V13 → Field Engine)
Główna faza wykonania.

field_state = PipelineV13.step(input_payload, field_state)
field_state = FieldEngine.step(field_state)

### 4.3. HOOK 3 — SAVE (V13 → V12)
Wywoływany po zakończeniu kroku regulacji.

snapshot = DataBridge.save(field_state)
V12.LTM.write(snapshot)

---

## 5. Kolejność kroków wykonania
### 5.1. Sekwencja pełnego cyklu

1. MeniscusEngine.receive(input_payload)

2. LOAD:
snapshot = V12.LTM.read()
field_state = DataBridge.load(snapshot)

3. EXECUTE:
field_state = PipelineV13.step()
field_state = FieldEngine.step()

4. SAVE:
snapshot = DataBridge.save(field_state)
V12.LTM.write(snapshot)

5. MeniscusEngine.respond(output_payload)

---

## 6. Interfejsy wymagane
### 6.1. V12 (01_runtime/)

LTM.read(state_id) → snapshot
LTM.write(snapshot)
Drift.apply(parameters) → parameters'

### 6.2. V13 (pipeline_v13/)

PipelineV13.step(input_payload, field_state) → field_state'

### 6.3. Field Engine (03_field_engine/)

FieldEngine.step(field_state) → field_state'

### 6.4. DataBridge

DataBridge.load(snapshot) → field_state
DataBridge.save(field_state) → snapshot

### 6.5. Meniscus Engine

MeniscusEngine.receive(input_payload)
MeniscusEngine.respond(output_payload)

---

## 7. Inwarianty wykonania
### 7.1. Inwarianty sekwencji
- LOAD musi poprzedzać EXECUTE.
- SAVE musi następować po EXECUTE.
- MeniscusEngine jest jedyną warstwą wejścia/wyjścia.

### 7.2. Inwarianty danych
- field_state musi być spójny z snapshotem.
- snapshot musi być kompletny przed SAVE.
- brak częściowych zapisów.

### 7.3. Inwarianty regulacji
- V12 nie wykonuje żadnej regulacji.
- Field Engine jest jedyną warstwą regulacji.

---

## 8. Wymagania implementacyjne
### 8.1. Wymagane moduły
- DataBridge (nowy moduł)
- aktualizacja pipeline_v13/ o HOOK LOAD/SAVE
- aktualizacja execution_flow.md

### 8.2. Wymagane testy
- test_execution_sequence
- test_load_execute_save
- test_invariants_execution
- test_meniscus_entry_exit

---

## 9. Status implementacji
- V12: kompletna warstwa runtime
- V13: pipeline modularny — wymaga integracji HOOK LOAD/SAVE
- Field Engine: kompletna warstwa regulacji
- Meniscus: skeleton — wymaga integracji z pipeline V13
- Dokumentacja: wymaga synchronizacji

---

## 10. Działania wymagane
1. Dodanie HOOK LOAD/SAVE do pipeline_v13/.
2. Implementacja DataBridge.load/save.
3. Aktualizacja execution_flow.md.
4. Integracja MeniscusEngine → PipelineV13.
5. Dodanie testów sekwencji wykonania.
6. Synchronizacja state_machine.md z Execution Bridge.

---
