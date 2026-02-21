# Drift Parameter Specification (V12 Drift Layer)
# RAMORGA ENGINE — Data Specification Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalną specyfikację parametrów dryfu (drift_parameters) w warstwie V12.
Drift jest mechanizmem odpowiedzialnym za:
- długoterminową adaptację parametrów modelu,
- kompensację zmian wynikających z kolejnych cykli wykonania,
- utrzymanie ciągłości parametrów między cyklami V13.

Specyfikacja obejmuje:
- strukturę drift_parameters,
- typy danych,
- zasady aktualizacji,
- inwarianty ciągłości,
- integrację z snapshotem i DataBridge.

---

## 2. Lokalizacja modułów w repo

01_runtime/drift.py
01_runtime/ltm.py
ltm_snapshot_spec.md
ltm_drift_contract.md
v12_v13_data_bridge.md 
field_state/ 
pipeline_v13/

---

## 3. Rola drift_parameters
Drift pełni funkcję:
- adaptacji parametrów modelu w czasie,
- kompensacji dryfu numerycznego,
- stabilizacji długoterminowej,
- utrzymania zgodności z Continuity Model.

Drift **nie** może:
- modyfikować wartości regulacyjnych (tension, energy, entropy),
- ingerować w state_vector,
- nadpisywać wyników Field Engine.

---

## 4. Struktura drift_parameters

### 4.1. Format główny

drift_parameters:
drift_step: int
drift_vector: dict
drift_rate: float
drift_bounds: dict
metadata:
last_update_timestamp: int
last_cycle_id: str

---

## 5. Specyfikacja pól

### 5.1. drift_step
**Typ:** int  
**Opis:** licznik kroków dryfu; zwiększany o 1 przy każdym cyklu.

### 5.2. drift_vector
**Typ:** dict  
**Opis:** wektor parametrów podlegających dryfowi; klucze zależne od modelu.

### 5.3. drift_rate
**Typ:** float  
**Opis:** współczynnik określający tempo dryfu; wartość ∈ (0, 1].

### 5.4. drift_bounds
**Typ:** dict  
**Opis:** ograniczenia wartości dryfu; format:

drift_bounds:
param_name:
min: float
max: float

### 5.5. metadata
**Typ:** dict  
**Opis:** dane pomocnicze:
- last_update_timestamp — monotoniczny,
- last_cycle_id — identyfikator cyklu, w którym wykonano dryf.

---

## 6. Zasady aktualizacji dryfu

### 6.1. Ogólna formuła
Dla każdego parametru `p`:

p' = p + drift_rate * drift_vector[p]

### 6.2. Ograniczenia
Po aktualizacji:

p' = clamp(p', drift_bounds[p].min, drift_bounds[p].max)

### 6.3. Aktualizacja metadanych

drift_step += 1
last_update_timestamp = current_timestamp
last_cycle_id = current_cycle_id

---

## 7. Integracja z snapshotem

### 7.1. Zapis

snapshot.parameters.drift_parameters = drift_parameters

### 7.2. Odczyt

drift_parameters = snapshot.parameters.drift_parameters

### 7.3. Wymagania
- drift_parameters muszą być kompletne,
- brak wartości null,
- brak brakujących pól.

---

## 8. Integracja z DataBridge

### 8.1. LOAD

field_state.parameters.drift_parameters = snapshot.parameters.drift_parameters

### 8.2. SAVE

snapshot.parameters.drift_parameters = field_state.parameters.drift_parameters

### 8.3. Wymagania
- mapowanie musi być jednoznaczne,
- brak transformacji danych poza serializacją.

---

## 9. Integracja z Continuity Model
### 9.1. Wymagania
- drift musi być monotoniczny w czasie,
- drift nie może powodować skoków wartości,
- drift nie może naruszać stabilności regulatorów.

### 9.2. Niedozwolone
- dryfowanie wartości regulacyjnych,
- dryfowanie timestampów,
- dryfowanie cycle_id.

---

## 10. Inwarianty dryfu

### 10.1. Inwarianty danych
- drift_rate ∈ (0, 1],
- drift_step ≥ 0,
- drift_bounds.min ≤ drift_bounds.max,
- brak wartości null.

### 10.2. Inwarianty wykonania
- Drift.apply() może być wywołane tylko w V12,
- drift nie może być wywoływany w V13,
- drift musi być deterministyczny w ramach cyklu.

### 10.3. Inwarianty ciągłości
- brak utraty parametrów,
- brak nadpisywania regulacji pola,
- brak częściowych aktualizacji.

---

## 11. Wymagania implementacyjne
1. Implementacja pełnej aktualizacji dryfu w drift.py.  
2. Dodanie walidacji drift_bounds.  
3. Dodanie testów dryfu (T1–T4).  
4. Integracja z snapshotem i DataBridge.  
5. Aktualizacja ltm_drift_contract.md i ltm_snapshot_spec.md.  

---

## 12. Status implementacji
- drift.py: istnieje, wymaga formalizacji,
- snapshot: istnieje, wymaga synchronizacji,
- DataBridge: brak implementacji,
- testy dryfu: częściowe,
- dokumentacja: wymaga aktualizacji.

---
