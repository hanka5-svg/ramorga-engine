# LTM + Drift Contract (V12 Memory Layer)
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny kontrakt warstwy pamięci długoterminowej (LTM) oraz
mechanizmu dryfu parametrów (drift) w PipelineV12.  
Warstwa ta jest jedyną odpowiedzialną za:
- trwałe przechowywanie snapshotów stanu,
- aktualizację parametrów dryfu,
- dostarczanie danych do PipelineV13 poprzez DataBridge.

Kontrakt określa:
- odpowiedzialności LTM i drift,
- interfejsy,
- strukturę snapshotu,
- zasady aktualizacji dryfu,
- inwarianty,
- integrację z PipelineV13 i Field Engine.

---

## 2. Lokalizacja modułów w repo

01_runtime/
pipeline_v13/
field_state/
v12_v13_data_bridge.md
execution_bridge.md

---

## 3. Zakres odpowiedzialności LTM (Long-Term Memory)
### 3.1. Odpowiedzialności
- przechowywanie snapshotów stanu,
- odczyt snapshotu przy inicjalizacji cyklu,
- zapis snapshotu po zakończeniu cyklu,
- utrzymanie spójności danych między cyklami.

### 3.2. Zakres niedozwolony
LTM **nie wykonuje**:
- regulacji pola,
- aktualizacji field_state,
- normalizacji danych,
- logiki pipeline.

---

## 4. Zakres odpowiedzialności Drift
### 4.1. Odpowiedzialności
- aktualizacja drift_parameters,
- kompensacja dryfu parametrów modelu,
- utrzymanie ciągłości parametrów między cyklami.

### 4.2. Zakres niedozwolony
Drift **nie może**:
- modyfikować wartości regulacyjnych (tension, energy, entropy),
- nadpisywać wyników Field Engine,
- zmieniać struktury snapshotu.

---

## 5. Interfejs LTM
### 5.1. Odczyt

LTM.read(state_id) → snapshot

### 5.2. Zapis

LTM.write(snapshot)

### 5.3. Wymagania
- snapshot musi być kompletny,
- snapshot musi być zgodny z ATML,
- snapshot musi być odwracalny.

---

## 6. Interfejs Drift
### 6.1. Aktualizacja dryfu

Drift.apply(parameters) → parameters'

### 6.2. Wymagania
- drift może modyfikować tylko drift_parameters,
- drift nie może modyfikować regulation.*,
- drift musi być deterministyczny w ramach jednego cyklu.

---

## 7. Struktura snapshotu (V12)

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

## 8. Integracja z PipelineV13 (LOAD/SAVE)
### 8.1. LOAD (V12 → V13)

snapshot = LTM.read(state_id)
field_state = DataBridge.load(snapshot)

### 8.2. SAVE (V13 → V12)

snapshot = DataBridge.save(field_state)
LTM.write(snapshot)

### 8.3. Wymagania
- LOAD musi poprzedzać PipelineV13.step(),
- SAVE musi następować po FieldEngine.step(),
- snapshot musi być spójny z field_state.

---

## 9. Integracja z Field Engine
### 9.1. Zasada nadrzędna
Drift **nie może** ingerować w regulację pola.

### 9.2. Wymagania
- drift_parameters mogą wpływać na model_parameters,
- drift nie może wpływać na regulation.tension/energy/entropy,
- Field Engine nie wywołuje drift.

---

## 10. Inwarianty LTM + Drift
### 10.1. Inwarianty danych
- snapshot.core.timestamp musi być monotoniczny,
- snapshot.parameters.model_parameters musi być spójny z ATML,
- snapshot.parameters.drift_parameters musi być spójny z Continuity Model.

### 10.2. Inwarianty wykonania
- LTM.read → zawsze przed PipelineV13.step(),
- LTM.write → zawsze po FieldEngine.step(),
- Drift.apply → tylko na parameters.model_parameters.

### 10.3. Inwarianty ciągłości
- brak utraty parametrów między cyklami,
- brak nadpisywania regulacji pola,
- brak częściowych zapisów snapshotu.

---

## 11. Wymagania implementacyjne
### 11.1. Moduły wymagane
- 01_runtime/
- DataBridge
- pipeline_v13/
- field_state/

### 11.2. Funkcje wymagane

LTM.read()
LTM.write()
Drift.apply()

### 11.3. Testy wymagane
- test_ltm_read_write
- test_drift_update
- test_snapshot_roundtrip
- test_invariants_ltm
- test_invariants_drift
- test_ltm_pipeline_integration

---

## 12. Status implementacji
- LTM: istnieje,
- Drift: istnieje,
- DataBridge: wymaga implementacji,
- pipeline_v13: wymaga integracji LOAD/SAVE,
- dokumentacja: wymaga synchronizacji.

---

## 13. Działania wymagane
1. Ujednolicenie struktury snapshotu.
2. Implementacja DataBridge.load/save.
3. Integracja LOAD/SAVE w pipeline_v13/.
4. Dodanie testów LTM + drift.
5. Aktualizacja execution_flow.md.
6. Synchronizacja state_machine.md i module_map.md.

---

