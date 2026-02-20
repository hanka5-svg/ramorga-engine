# Transition Architecture: PipelineV12 → PipelineV13
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalną architekturę przejścia pomiędzy PipelineV12 (runtime, pamięć, dryf)
a PipelineV13 (modularny pipeline pola).  
Zakres obejmuje:
- separację odpowiedzialności,
- kontrakty danych,
- kontrakty wykonania,
- kontrakty regulacji,
- ścieżkę integracji w repozytorium.

Dokument jest częścią warstwy wykonawczej RAMORGA ENGINE.

---

## 2. Zakres V12 (legacy runtime layer)
### 2.1. Lokalizacja w repo

01_runtime/

### 2.2. Odpowiedzialności
- long‑term memory (LTM),
- parameter drift handling,
- runtime state persistence,
- brak regulacji pola,
- brak integracji z Field Engine.

### 2.3. Interfejsy wymagane
- LTM.read(state_id) → state_snapshot
- LTM.write(state_snapshot)
- Drift.apply(parameters) → parameters'

---

## 3. Zakres V13 (primary execution pipeline)
### 3.1. Lokalizacja w repo

pipeline_v13/
03_field_engine/
tension_loop/
energy_regulator/
field_state/
src/ramorga_engine/entropic_modulator.py

### 3.2. Odpowiedzialności
- modularny pipeline wykonania,
- integracja z Field Engine,
- regulacja napięcia, energii, entropii,
- operacje na field_state,
- zgodność z state_machine.md i execution_flow.md.

### 3.3. Interfejsy wymagane
- PipelineV13.execute(input_payload) → output_payload
- FieldEngine.step(field_state) → field_state'
- Regulators:
  - tension_loop.run()
  - energy_regulator.adjust()
  - entropic_modulator.modulate()

---

## 4. Meniscus Engine (boundary layer)
### 4.1. Lokalizacja w repo

04_meniscus_engine/
05_api/
06_integration/

### 4.2. Odpowiedzialności
- jedyne wejście do systemu,
- normalizacja wejść,
- walidacja kontraktów danych,
- przekazanie sterowania do PipelineV13.

---

## 5. Model przejścia (Transition Architecture)
### 5.1. Architektura docelowa

[API/Integration]
↓
04_meniscus_engine/
↓
pipeline_v13/
↓
03_field_engine/
↓
01_runtime/ (LTM + drift)

### 5.2. Zasada ciągłości (Continuity Model)
- V13 jest jedynym pipeline wykonania.
- V12 jest wyłącznie warstwą pamięci i dryfu.
- Field Engine jest jedyną warstwą regulacji.
- Meniscus jest jedyną warstwą wejścia/wyjścia.

---

## 6. Kontrakty przejścia V12 ↔ V13
### 6.1. Kontrakt danych

V13.field_state  ↔  V12.LTM.snapshot

Mapowanie:
- field_state.core → snapshot.core
- field_state.parameters → snapshot.parameters
- field_state.regulation → ignorowane przez V12

### 6.2. Kontrakt wykonania
- PipelineV13 wywołuje V12 w dwóch punktach:
  - LOAD: przed inicjalizacją field_state
  - SAVE: po zakończeniu kroku regulacji

### 6.3. Kontrakt regulacji
- V12: regulatory = disabled
- V13: regulatory = tension_loop + energy_regulator + entropic_modulator

---

## 7. Wymagane zmiany w repo
### 7.1. Dokumentacja
Aktualizacja:

data_contracts.md
state_machine.md
execution_flow.md
module_map.md
dependency_graph.md

### 7.2. Kod
- izolacja V12 do funkcji LTM + drift,
- potwierdzenie, że pipeline_v13 nie wywołuje żadnych funkcji regulacyjnych z V12,
- integracja Field Engine jako jedynej warstwy regulacji.

---

## 8. Testy
### 8.1. Lokalizacja

07_tests/
test_plan.md
test_matrix.md

### 8.2. Wymagania
- testy T1–T4 muszą pokrywać:
  - LOAD (V12 → V13),
  - SAVE (V13 → V12),
  - pełny krok regulacji pola,
  - zgodność ze state_machine.md.

---

## 9. Status implementacji
- V12: kompletna warstwa runtime (01_runtime/)
- V13: pipeline + moduły regulacji (pipeline_v13/, 03_field_engine/, tension_loop/, energy_regulator/, field_state/)
- Meniscus: skeleton (04_meniscus_engine/)
- Dokumentacja: kompletna, wymaga synchronizacji z kodem

---

## 10. Wymagane działania (kolejność)
1. Ustalenie interfejsu LTM.read / LTM.write.
2. Dodanie mapowania field_state ↔ snapshot.
3. Aktualizacja execution_flow.md o LOAD/SAVE.
4. Weryfikacja state_machine.md pod kątem punktów przejścia.
5. Integracja Field Engine jako jedynej warstwy regulacji.
6. Aktualizacja test_matrix.md.
7. Dodanie testów T1–T4 dla przejść V12 ↔ V13.

---
