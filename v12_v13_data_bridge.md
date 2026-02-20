# V12 ↔ V13 Data Bridge
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny most danych pomiędzy:
- PipelineV12 (01_runtime/) — warstwa pamięci i dryfu,
- PipelineV13 (pipeline_v13/) — główny pipeline wykonania,
- Field Engine (03_field_engine/, tension_loop/, energy_regulator/, field_state/).

Most danych określa:
- struktury wymiany,
- kierunki przepływu,
- punkty synchronizacji,
- inwarianty spójności.

---

## 2. Lokalizacja modułów w repo
### 2.1. V12 — warstwa pamięci i dryfu

01_runtime/

### 2.2. V13 — pipeline modularny

pipeline_v13/

### 2.3. Field Engine — regulacja pola
03_field_engine/
tension_loop/
energy_regulator/
field_state/
src/ramorga_engine/entropic_modulator.py

---

## 3. Zakres mostu danych
Most obejmuje trzy obszary:

1. **Snapshot stanu**  
   - zapis/odczyt stanu pola i parametrów do/z V12.

2. **Parametry regulacji**  
   - przekazywane z V13 do V12 jako część snapshotu.

3. **Parametry dryfu**  
   - aktualizowane w V12 i zwracane do V13.

---

## 4. Struktura danych snapshotu (V12)
Snapshot przechowywany w V12 musi mieć strukturę zgodną z ATML i Continuity Model.

### 4.1. Format snapshotu

snapshot:
core:
timestamp: int
cycle_id: str
version: str
parameters:
model_parameters: dict
drift_parameters: dict
field:
state_vector: dict
regulation_state: dict

### 4.2. Wymagania
- snapshot musi być serializowalny,
- snapshot musi być odwracalny,
- snapshot musi zawierać pełny stan pola wymagany do rekonstrukcji field_state.

---

## 5. Struktura danych field_state (V13)
Field Engine operuje na strukturze:

field_state:
core:
cycle_id: str
timestamp: int
regulation:
tension: float
energy: float
entropy: float
parameters:
model_parameters: dict
drift_parameters: dict

---

## 6. Mapowanie snapshot ↔ field_state
### 6.1. Mapowanie V12 → V13 (LOAD)

field_state.core.timestamp        = snapshot.core.timestamp
field_state.core.cycle_id         = snapshot.core.cycle_id

field_state.parameters.model_parameters  = snapshot.parameters.model_parameters
field_state.parameters.drift_parameters  = snapshot.parameters.drift_parameters

field_state.regulation = snapshot.field.regulation_state

### 6.2. Mapowanie V13 → V12 (SAVE)

snapshot.core.timestamp           = field_state.core.timestamp
snapshot.core.cycle_id            = field_state.core.cycle_id

snapshot.parameters.model_parameters = field_state.parameters.model_parameters
snapshot.parameters.drift_parameters = field_state.parameters.drift_parameters

snapshot.field.state_vector       = field_state.regulation
snapshot.field.regulation_state   = field_state.regulation

---

## 7. Punkty synchronizacji
### 7.1. LOAD (przed wykonaniem pipeline V13)
Wywołanie:

snapshot = V12.LTM.read(state_id)
field_state = DataBridge.load(snapshot)

### 7.2. SAVE (po wykonaniu kroku regulacji)
Wywołanie:

snapshot = DataBridge.save(field_state)
V12.LTM.write(snapshot)

---

## 8. Inwarianty spójności
### 8.1. Inwarianty danych
- `cycle_id` musi być identyczny w snapshot i field_state.
- `timestamp` musi być monotoniczny.
- `model_parameters` muszą być zgodne z ATML.
- `drift_parameters` muszą być zgodne z Continuity Model.

### 8.2. Inwarianty wykonania
- LOAD musi poprzedzać każdy krok pipeline V13.
- SAVE musi następować po każdym kroku regulacji pola.
- Snapshot musi być kompletny — brak pól opcjonalnych.

---

## 9. Wymagania implementacyjne
### 9.1. Wymagane funkcje

DataBridge.load(snapshot) → field_state
DataBridge.save(field_state) → snapshot

### 9.2. Wymagane testy
- test_load_mapping
- test_save_mapping
- test_invariants
- test_roundtrip (snapshot → field_state → snapshot)

---

## 10. Status implementacji
- snapshot: istnieje w 01_runtime/
- field_state: istnieje w field_state/
- brak formalnego DataBridge — wymagane dodanie modułu

---

## 11. Działania wymagane
1. Utworzenie modułu DataBridge.
2. Implementacja load/save.
3. Aktualizacja execution_flow.md o LOAD/SAVE.
4. Dodanie testów roundtrip.
5. Synchronizacja z state_machine.md.

---


