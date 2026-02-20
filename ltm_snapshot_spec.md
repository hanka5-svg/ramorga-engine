# LTM Snapshot Specification (V12 Memory Layer)
# RAMORGA ENGINE — Data Specification Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalną specyfikację snapshotu LTM (Long-Term Memory) w warstwie V12.
Snapshot jest jedyną trwałą reprezentacją stanu systemu pomiędzy cyklami wykonania V13.

Specyfikacja obejmuje:
- strukturę snapshotu,
- typy danych,
- zasady serializacji,
- zasady odwracalności,
- inwarianty ciągłości,
- integrację z DataBridge i field_state.

---

## 2. Lokalizacja modułów w repo

01_runtime/
v12_v13_data_bridge.md
ltm_drift_contract.md
field_state/
pipeline_v13/

---

## 3. Rola snapshotu
Snapshot pełni funkcję:
- trwałego zapisu stanu pola,
- trwałego zapisu parametrów modelu i dryfu,
- punktu startowego dla kolejnego cyklu wykonania,
- źródła danych dla DataBridge.load().

Snapshot **nie** zawiera:
- logiki wykonania,
- danych wejściowych,
- danych regulatorów poza stanem pola.

---

## 4. Struktura snapshotu (ATML-compliant)

### 4.1. Format główny

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

---

## 5. Specyfikacja pól

### 5.1. core
| Pole | Typ | Opis |
|------|-----|------|
| timestamp | int | znacznik czasu snapshotu; monotoniczny |
| cycle_id | str | identyfikator cyklu wykonania |
| version | str | wersja snapshotu (np. "v12.3") |

### 5.2. parameters
| Pole | Typ | Opis |
|------|-----|------|
| model_parameters | dict | parametry modelu wymagane przez V13 |
| drift_parameters | dict | parametry dryfu aktualizowane przez V12 |

### 5.3. field
| Pole | Typ | Opis |
|------|-----|------|
| state_vector | dict | pełny stan pola wymagany do rekonstrukcji field_state |
| regulation_state | dict | wartości regulacyjne (tension, energy, entropy) |

---

## 6. Zasady serializacji
### 6.1. Wymagania
- snapshot musi być serializowalny do JSON,
- snapshot musi być odwracalny (roundtrip),
- snapshot musi być kompletny (brak pól opcjonalnych),
- snapshot musi być zgodny z ATML.

### 6.2. Niedozwolone
- wartości null,
- wartości NaN,
- typy niestandardowe (np. obiekty klas).

---

## 7. Zasady odwracalności (Roundtrip)
### 7.1. Definicja
Roundtrip oznacza:

snapshot → DataBridge.load() → field_state → DataBridge.save() → snapshot'
gdzie:

snapshot == snapshot'

### 7.2. Wymagania
- brak utraty danych,
- brak zmian kolejności pól,
- brak zmian typów danych.

---

## 8. Integracja z DataBridge
### 8.1. LOAD

field_state = DataBridge.load(snapshot)

### 8.2. SAVE

snapshot = DataBridge.save(field_state)

### 8.3. Wymagania
- mapowanie musi być jednoznaczne,
- snapshot musi zawierać wszystkie dane wymagane do rekonstrukcji field_state,
- field_state nie może zawierać danych spoza snapshotu.

---

## 9. Integracja z field_state
### 9.1. Mapowanie snapshot → field_state

field_state.core.timestamp        = snapshot.core.timestamp
field_state.core.cycle_id         = snapshot.core.cycle_id
field_state.parameters.model_parameters = snapshot.parameters.model_parameters
field_state.parameters.drift_parameters = snapshot.parameters.drift_parameters
field_state.regulation            = snapshot.field.regulation_state

### 9.2. Mapowanie field_state → snapshot

snapshot.core.timestamp           = field_state.core.timestamp
snapshot.core.cycle_id            = field_state.core.cycle_id
snapshot.parameters.model_parameters = field_state.parameters.model_parameters
snapshot.parameters.drift_parameters = field_state.parameters.drift_parameters
snapshot.field.state_vector       = field_state.regulation
snapshot.field.regulation_state   = field_state.regulation

---

## 10. Inwarianty snapshotu
### 10.1. Inwarianty danych
- timestamp musi być monotoniczny,
- cycle_id musi być unikalny w obrębie cyklu,
- brak wartości null,
- brak brakujących pól.

### 10.2. Inwarianty wykonania
- snapshot musi być zapisany po każdym cyklu,
- snapshot musi być odczytany przed każdym cyklem,
- snapshot musi być spójny z field_state.

### 10.3. Inwarianty ciągłości
- brak utraty parametrów,
- brak nadpisywania regulacji pola przez drift,
- brak częściowych zapisów.

---

## 11. Wymagania implementacyjne
1. Implementacja pełnej serializacji snapshotu.  
2. Implementacja DataBridge.load/save zgodnie ze specyfikacją.  
3. Dodanie testów roundtrip.  
4. Dodanie testów integralności snapshotu.  
5. Aktualizacja execution_flow.md i state_machine_alignment.md.  

---

## 12. Status implementacji
- snapshot: istnieje w 01_runtime/, wymaga formalizacji,
- DataBridge: brak implementacji,
- field_state: istnieje,
- pipeline_v13: wymaga integracji LOAD/SAVE,
- dokumentacja: wymaga synchronizacji.

---
