# Regulation Bridge: V12 → V13
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny most regulacji pomiędzy:
- PipelineV12 (01_runtime/) — warstwa pamięci i dryfu,
- PipelineV13 (pipeline_v13/) — główny pipeline wykonania,
- Field Engine (03_field_engine/) — warstwa regulacji pola.

Most regulacji określa:
- które moduły odpowiadają za regulację,
- jak wyłączane są regulatory V12,
- jak V13 deleguje regulację do Field Engine,
- jakie interfejsy i inwarianty muszą być zachowane.

---

## 2. Lokalizacja modułów regulacji w repo
### 2.1. Regulatory V12 (do wyłączenia)

01_runtime/ # internal drift + legacy regulation (must be disabled)

### 2.2. Regulatory V13 (docelowe)

tension_loop/
energy_regulator/
src/ramorga_engine/entropic_modulator.py
field_state/
03_field_engine/


### 2.3. Pipeline wykonania

pipeline_v13/

---

## 3. Zasada nadrzędna regulacji
### 3.1. Jedyny regulator pola
**Field Engine jest jedyną warstwą regulacji pola.**

### 3.2. Rola V12
- V12 **nie wykonuje regulacji**.
- V12 wykonuje wyłącznie:
  - long‑term memory,
  - parameter drift,
  - snapshot persistence.

### 3.3. Rola V13
- V13 deleguje regulację do Field Engine.
- V13 nie posiada własnych regulatorów.

---

## 4. Architektura regulacji (docelowa)

pipeline_v13/
↓
03_field_engine/
↓
tension_loop/
energy_regulator/
entropic_modulator/
↓
field_state/

---

## 5. Interfejsy regulacji
### 5.1. Field Engine

FieldEngine.step(field_state) → field_state'

### 5.2. Tension Loop

tension_loop.run(field_state) → field_state'

### 5.3. Energy Regulator

energy_regulator.adjust(field_state) → field_state'

### 5.4. Entropic Modulator

entropic_modulator.modulate(field_state) → field_state'

### 5.5. PipelineV13

PipelineV13.step(input_payload, field_state) → field_state'

---

## 6. Wyłączenie regulatorów V12
### 6.1. Zakres wyłączenia
W katalogu:

01_runtime/
należy wyłączyć:
- wszelkie funkcje regulacyjne,
- wszelkie modyfikacje field_state,
- wszelkie operacje na napięciu, energii, entropii.

### 6.2. Pozostawione funkcje
- LTM.read
- LTM.write
- Drift.apply

---

## 7. Kolejność regulacji (Execution Order)
### 7.1. Sekwencja

1. PipelineV13.step()
2. tension_loop.run()
3. energy_regulator.adjust()
4. entropic_modulator.modulate()
5. FieldEngine.step()   # integracja wyników

### 7.2. Inwarianty
- Regulacja musi być deterministyczna w ramach jednego cyklu.
- Kolejność regulatorów jest stała.
- FieldEngine.step() jest ostatnim krokiem regulacji.

---

## 8. Punkty integracji z pipeline V13
### 8.1. Integracja w pipeline_v13/
PipelineV13 musi wywołać:

 field_state = FieldEngine.step(field_state)
 po wykonaniu własnej logiki.

### 8.2. Integracja w Field Engine
Field Engine musi wywołać regulatory w kolejności:

tension_loop → energy_regulator → entropic_modulator

---

## 9. Inwarianty regulacji
### 9.1. Inwarianty danych
- field_state.regulation.tension ∈ ℝ
- field_state.regulation.energy ∈ ℝ
- field_state.regulation.entropy ∈ ℝ

### 9.2. Inwarianty wykonania
- regulatory V12 = disabled
- regulatory V13 = enabled
- Field Engine = jedyna warstwa regulacji

### 9.3. Inwarianty ciągłości (Continuity Model)
- brak skoków wartości regulacyjnych między cyklami,
- dryf parametrów nie może nadpisywać regulacji pola.

---

## 10. Wymagania implementacyjne
### 10.1. Wymagane zmiany
- wyłączenie regulatorów V12,
- dodanie wywołań FieldEngine.step() w pipeline_v13/,
- potwierdzenie kolejności regulatorów w Field Engine,
- aktualizacja execution_flow.md.

### 10.2. Wymagane testy
- test_regulation_sequence
- test_regulation_invariants
- test_no_v12_regulation
- test_field_engine_integration

---

## 11. Status implementacji
- regulatory V13: istnieją,
- Field Engine: istnieje,
- regulatory V12: wymagają wyłączenia,
- pipeline_v13: wymaga integracji z Field Engine,
- dokumentacja: wymaga synchronizacji.

---

## 12. Działania wymagane
1. Wyłączyć regulatory V12.
2. Dodać wywołanie FieldEngine.step() do pipeline_v13/.
3. Ustalić kolejność regulatorów w Field Engine.
4. Zaktualizować execution_flow.md.
5. Dodać testy regulacji.
6. Zsynchronizować state_machine.md.

---
