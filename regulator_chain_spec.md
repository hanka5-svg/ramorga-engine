# Regulator Chain Specification — V13 Regulation Layer
# RAMORGA ENGINE — Regulation Architecture
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje specyfikację łańcucha regulatorów (Regulator Chain) używanego przez
Field Engine w architekturze V13.  
Łańcuch regulatorów jest odpowiedzialny za:
- regulację napięcia pola (tension),
- regulację energii pola (energy),
- regulację entropii pola (entropy),
- zachowanie ciągłości i stabilności pola zgodnie z Continuity Model.

Specyfikacja obejmuje:
- kolejność regulatorów,
- interfejsy,
- wymagania wejścia/wyjścia,
- inwarianty,
- integrację z Field Engine i field_state.

---

## 2. Lokalizacja modułów w repo

03_field_engine/
tension_loop/
energy_regulator/
src/ramorga_engine/entropic_modulator.py
field_state/
pipeline_v13/
regulation_bridge.md
field_engine_contract.md

---

## 3. Architektura łańcucha regulatorów

### 3.1. Kolejność wykonania (stała)

1. tension_loop.run(field_state)

2. energy_regulator.adjust(field_state)

3. entropic_modulator.modulate(field_state)


### 3.2. Zasada nadrzędna
Łańcuch regulatorów jest wykonywany **wyłącznie** przez FieldEngine.step().

PipelineV13 **nie** może:
- wywoływać regulatorów,
- modyfikować wartości regulacyjnych,
- zmieniać kolejności regulatorów.

---

## 4. Interfejsy regulatorów

### 4.1. tension_loop

tension_loop.run(field_state) → field_state'
**Wejście:** field_state  
**Wyjście:** zaktualizowane regulation.tension

### 4.2. energy_regulator

energy_regulator.adjust(field_state) → field_state'
**Wejście:** field_state (po tension_loop)  
**Wyjście:** zaktualizowane regulation.energy

### 4.3. entropic_modulator

entropic_modulator.modulate(field_state) → field_state'
**Wejście:** field_state (po energy_regulator)  
**Wyjście:** zaktualizowane regulation.entropy

---

## 5. Wymagania wejścia/wyjścia

### 5.1. Wymagania wejścia
- field_state musi być zgodny z ATML,
- regulation.tension/energy/entropy muszą istnieć,
- brak wartości null,
- brak NaN.

### 5.2. Wymagania wyjścia
- każdy regulator musi zwrócić pełny field_state,
- wartości regulacyjne muszą być liczbami rzeczywistymi,
- brak skoków wartości naruszających Continuity Model.

---

## 6. Inwarianty łańcucha regulatorów

### 6.1. Inwarianty kolejności
- kolejność regulatorów jest niezmienna,
- brak równoległego wykonania,
- brak pomijania regulatorów.

### 6.2. Inwarianty danych
- regulation.tension ∈ ℝ  
- regulation.energy ∈ ℝ  
- regulation.entropy ∈ ℝ  
- brak null / NaN  
- brak zmian w polach spoza regulation.*

### 6.3. Inwarianty wykonania
- każdy regulator musi działać deterministycznie w ramach cyklu,
- regulator nie może modyfikować snapshotu,
- regulator nie może modyfikować drift_parameters.

### 6.4. Inwarianty ciągłości
- brak skoków wartości między cyklami,
- brak naruszeń stabilności pola,
- brak nadpisywania wyników poprzednich regulatorów.

---

## 7. Integracja z Field Engine

### 7.1. Wywołanie

FieldEngine.step(field_state):
tension_loop.run()
energy_regulator.adjust()
entropic_modulator.modulate()

### 7.2. Wymagania
- Field Engine musi wykonać pełny łańcuch,
- Field Engine nie może zmieniać kolejności regulatorów,
- Field Engine musi walidować inwarianty po każdym regulatorze.

---

## 8. Integracja z field_state

### 8.1. Mapowanie
Regulatory aktualizują wyłącznie:

field_state.regulation.tension
field_state.regulation.energy
field_state.regulation.entropy

### 8.2. Niedozwolone
- modyfikacja field_state.core,
- modyfikacja field_state.parameters,
- modyfikacja drift_parameters.

---

## 9. Wymagania testowe

### 9.1. Testy jednostkowe (T1)
- test_tension_loop  
- test_energy_regulator  
- test_entropic_modulator  

### 9.2. Testy integracyjne (T2)
- test_regulator_chain  
- test_field_engine_regulators  

### 9.3. Testy przepływu (T3)
- test_field_engine_sequence  

### 9.4. Testy inwariantów (T4)
- test_regulation_invariants  

---

## 10. Status implementacji
- tension_loop: istnieje, wymaga testów,
- energy_regulator: istnieje, testy częściowe,
- entropic_modulator: istnieje, testy istnieją,
- Field Engine: istnieje, wymaga integracji,
- pipeline_v13: wymaga integracji z Field Engine,
- DataBridge: brak implementacji.

---
