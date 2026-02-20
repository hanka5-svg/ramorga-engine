# dependency_graph_v13.md
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje graf zależności (Dependency Graph) dla architektury V13 w ramorga-engine.
Obejmuje:
- moduły wykonawcze,
- moduły regulacji,
- warstwę pamięci V12,
- warstwę graniczną MeniscusEngine,
- kierunki zależności,
- inwarianty strukturalne.

---

## 2. Zakres
Graf obejmuje moduły z:
- `pipeline_v13/`
- `03_field_engine/`
- `tension_loop/`
- `energy_regulator/`
- `field_state/`
- `src/ramorga_engine/entropic_modulator.py`
- `04_meniscus_engine/`
- `01_runtime/`
- `data_bridge.py` (planowany)
- kontraktów: `*_contract.md`, `*_bridge.md`, `state_machine_alignment.md`, `module_map_v13.md`

---

## 3. Węzły grafu (moduły logiczne)

### 3.1. MeniscusEngine
**Węzeł:** `MENISCUS`  
**Repo:** `04_meniscus_engine/`  
**Rola:** brama wejścia/wyjścia, normalizacja ATML.

### 3.2. PipelineV13
**Węzeł:** `PIPELINE_V13`  
**Repo:** `pipeline_v13/`  
**Rola:** główny pipeline wykonania, orkiestracja cyklu.

### 3.3. Field Engine
**Węzeł:** `FIELD_ENGINE`  
**Repo:** `03_field_engine/`  
**Rola:** integracja regulatorów, aktualizacja `field_state`.

### 3.4. Tension Loop
**Węzeł:** `TENSION_LOOP`  
**Repo:** `tension_loop/`  
**Rola:** regulacja napięcia.

### 3.5. Energy Regulator
**Węzeł:** `ENERGY_REGULATOR`  
**Repo:** `energy_regulator/`  
**Rola:** regulacja energii.

### 3.6. Entropic Modulator
**Węzeł:** `ENTROPIC_MODULATOR`  
**Repo:** `src/ramorga_engine/entropic_modulator.py`  
**Rola:** regulacja entropii.

### 3.7. Field State
**Węzeł:** `FIELD_STATE`  
**Repo:** `field_state/`  
**Rola:** struktura danych pola.

### 3.8. DataBridge
**Węzeł:** `DATA_BRIDGE`  
**Repo:** `data_bridge.py` (planowany), `v12_v13_data_bridge.md`  
**Rola:** mapowanie `snapshot ↔ field_state`.

### 3.9. V12 LTM + Drift
**Węzeł:** `V12_LTM_DRIFT`  
**Repo:** `01_runtime/`  
**Rola:** pamięć długoterminowa, dryf parametrów.

---

## 4. Krawędzie grafu (zależności)

### 4.1. Meniscus → PipelineV13
**Krawędź:** `MENISCUS → PIPELINE_V13`  
**Znaczenie:** MeniscusEngine wywołuje `PipelineV13.step()` z `input_payload`.

### 4.2. PipelineV13 → Field Engine
**Krawędź:** `PIPELINE_V13 → FIELD_ENGINE`  
**Znaczenie:** PipelineV13 wywołuje `FieldEngine.step(field_state)`.

### 4.3. Field Engine → Regulatorzy
**Krawędzie:**
- `FIELD_ENGINE → TENSION_LOOP`
- `FIELD_ENGINE → ENERGY_REGULATOR`
- `FIELD_ENGINE → ENTROPIC_MODULATOR`

**Znaczenie:** Field Engine wywołuje kolejno:
- `tension_loop.run()`
- `energy_regulator.adjust()`
- `entropic_modulator.modulate()`

### 4.4. Regulatorzy → Field State
**Krawędzie:**
- `TENSION_LOOP → FIELD_STATE`
- `ENERGY_REGULATOR → FIELD_STATE`
- `ENTROPIC_MODULATOR → FIELD_STATE`

**Znaczenie:** każdy regulator odczytuje i aktualizuje `field_state`.

### 4.5. PipelineV13 ↔ DataBridge
**Krawędzie:**
- `PIPELINE_V13 → DATA_BRIDGE` (SAVE)
- `DATA_BRIDGE → PIPELINE_V13` (LOAD przez `field_state`)

**Znaczenie:** PipelineV13 korzysta z DataBridge do mapowania `field_state ↔ snapshot`.

### 4.6. DataBridge ↔ V12 LTM + Drift
**Krawędzie:**
- `DATA_BRIDGE → V12_LTM_DRIFT` (SAVE → `LTM.write(snapshot)`)
- `V12_LTM_DRIFT → DATA_BRIDGE` (LOAD → `LTM.read()`)

**Znaczenie:** DataBridge jest jedynym łącznikiem danych między V13 a V12.

### 4.7. Meniscus → Error Model (pośrednio)
**Krawędź logiczna:** `MENISCUS → ERROR_MODEL`  
**Znaczenie:** MeniscusEngine formatuje błędy zgodnie z `error_model_contract.md`.

---

## 5. Graf zależności — zapis tekstowy

### 5.1. Główna ścieżka wykonania
```text
MENISCUS
  ↓
PIPELINE_V13
  ↓
FIELD_ENGINE
  ↓
TENSION_LOOP → FIELD_STATE
  ↓
ENERGY_REGULATOR → FIELD_STATE
  ↓
ENTROPIC_MODULATOR → FIELD_STATE
  ↓
DATA_BRIDGE
  ↓
V12_LTM_DRIFT

5.2. Zasady kierunku
wszystkie krawędzie są jednokierunkowe,

brak cykli,

brak zależności wstecznych:

V12 nie zależy od V13,

Field Engine nie zależy od Meniscus,

Meniscus nie zależy od V12.

6. Inwarianty grafu zależności
6.1. Inwarianty strukturalne
każdy moduł ma jednoznaczny kierunek zależności,

brak cyklicznych zależności,

brak ukrytych wywołań poza zdefiniowanymi krawędziami.

6.2. Inwarianty wykonania
MeniscusEngine nigdy nie wywołuje V12 ani regulatorów bezpośrednio,

PipelineV13 jest jedynym miejscem orkiestracji,

Field Engine jest jedyną warstwą regulacji,

V12 jest jedyną warstwą pamięci.

6.3. Inwarianty ciągłości
zmiana w jednym module nie może wymuszać zmian w modułach „w górę” grafu,

DataBridge jest jedynym punktem styku V12/V13,

brak bezpośrednich zależności między Meniscus a V12.

7. Wymagania implementacyjne
Zweryfikować, że rzeczywiste importy w:

pipeline_v13/

03_field_engine/

tension_loop/

energy_regulator/

entropic_modulator.py

04_meniscus_engine/

01_runtime/
są zgodne z grafem zależności.

Dodać data_bridge.py jako jedyny moduł łączący V13 z V12.

Zaktualizować:

module_map_v13.md

state_machine_alignment.md

execution_bridge.md

regulation_bridge.md
o referencje do grafu zależności.

Dodać testy integracyjne:

test_dependency_graph_imports

test_no_backwards_dependencies

test_data_bridge_is_single_entrypoint_to_v12.

8. Status implementacji
moduły V13: istnieją,

kontrakty: istnieją (*_contract.md, *_bridge.md),

DataBridge: wymaga implementacji,

importy: wymagają audytu pod kątem zgodności z grafem,

dokumentacja: wymaga synchronizacji z rzeczywistymi zależnościami



