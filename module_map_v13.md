# Module Map — PipelineV13 Architecture
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje mapę modułów (Module Map) dla PipelineV13 w ramorga-engine.
Celem jest przedstawienie:
- pełnej listy modułów,
- ich odpowiedzialności,
- powiązań między modułami,
- kierunków zależności,
- integracji z V12, Field Engine i MeniscusEngine.

Dokument jest źródłem prawdy dla implementacji i testów.

---

## 2. Zakres
Mapa obejmuje moduły znajdujące się w:

pipeline_v13/
03_field_engine/
tension_loop/
energy_regulator/
field_state/
src/ramorga_engine/entropic_modulator.py
04_meniscus_engine/
01_runtime/

---

## 3. Moduły PipelineV13
### 3.1. pipeline_v13/
**Rola:** główny pipeline wykonania.

**Podmoduły:**
- `pipeline_core.py` — logika główna step()
- `pipeline_utils.py` — funkcje pomocnicze
- `pipeline_errors.py` — obsługa błędów pipeline
- `pipeline_contract.md` — specyfikacja kontraktu

**Odpowiedzialności:**
- orkiestracja cyklu wykonania,
- integracja LOAD/EXECUTE/SAVE,
- wywołanie Field Engine,
- obsługa błędów.

---

## 4. Moduły Field Engine
### 4.1. 03_field_engine/
**Rola:** integracja regulatorów i aktualizacja field_state.

**Podmoduły:**
- `field_engine.py` — główna logika FieldEngine.step()
- `field_engine_utils.py` — funkcje pomocnicze

**Odpowiedzialności:**
- wykonanie pełnego kroku regulacji pola,
- integracja wyników regulatorów,
- aktualizacja field_state.

---

### 4.2. tension_loop/
**Rola:** regulacja napięcia pola.

**Podmoduły:**
- `tension_loop.py`
- `tension_loop_state.py`
- `test_tension_loop.py`

**Odpowiedzialności:**
- obliczanie i aktualizacja tension,
- zapewnienie stabilności napięcia.

---

### 4.3. energy_regulator/
**Rola:** regulacja energii pola.

**Podmoduły:**
- `energy_regulator.py`
- `test_energy_regulator.py`

**Odpowiedzialności:**
- obliczanie i aktualizacja energy,
- kompensacja energii w cyklu.

---

### 4.4. entropic_modulator
**Lokalizacja:**

src/ramorga_engine/entropic_modulator.py

**Rola:** regulacja entropii pola.

**Podmoduły:**
- `entropic_modulator.py`
- `test_entropic_modulator.py`

**Odpowiedzialności:**
- obliczanie i aktualizacja entropy,
- stabilizacja wariancji pola.

---

### 4.5. field_state/
**Rola:** struktura danych pola.

**Podmoduły:**
- `field_state.py`
- `field_state_contract.md`
- `test_field_state.py`

**Odpowiedzialności:**
- reprezentacja stanu pola,
- walidacja struktury,
- zgodność z ATML.

---

## 5. Moduły MeniscusEngine
### 5.1. 04_meniscus_engine/
**Rola:** jedyna brama wejścia/wyjścia.

**Podmoduły:**
- `meniscus_engine.py`
- `meniscus_normalization.py`
- `meniscus_contract.md`

**Odpowiedzialności:**
- odbiór input_payload,
- walidacja ATML,
- normalizacja,
- przekazanie sterowania do PipelineV13,
- formatowanie output_payload.

---

## 6. Moduły V12 (LTM + drift)
### 6.1. 01_runtime/
**Rola:** pamięć długoterminowa i dryf parametrów.

**Podmoduły:**
- `ltm.py`
- `drift.py`
- `runtime_utils.py`

**Odpowiedzialności:**
- odczyt snapshotu,
- zapis snapshotu,
- aktualizacja drift_parameters.

---

## 7. Moduły DataBridge
### 7.1. v12_v13_data_bridge.md (specyfikacja)
**Rola:** mapowanie snapshot ↔ field_state.

**Podmoduły (do implementacji):**
- `data_bridge.py`

**Odpowiedzialności:**
- load(snapshot) → field_state
- save(field_state) → snapshot

---

## 8. Kierunki zależności
### 8.1. Diagram zależności (tekstowy)

MeniscusEngine
↓
PipelineV13
↓
FieldEngine
↓     ↓     ↓
tension energy entropy
↓
field_state
↓
DataBridge
↓
V12 (LTM + drift)

### 8.2. Zasady
- zależności są jednokierunkowe,
- brak cykli,
- Field Engine nie zależy od V12,
- MeniscusEngine nie zależy od regulatorów.

---

## 9. Inwarianty Module Map
### 9.1. Inwarianty strukturalne
- każdy moduł ma jednoznaczną odpowiedzialność,
- brak duplikacji funkcji,
- brak ukrytych zależności.

### 9.2. Inwarianty wykonania
- PipelineV13 jest jedynym miejscem orkiestracji,
- Field Engine jest jedyną warstwą regulacji,
- V12 jest jedyną warstwą pamięci.

---

## 10. Wymagania implementacyjne
1. Dodanie brakujących modułów DataBridge.  
2. Ujednolicenie interfejsów regulatorów.  
3. Aktualizacja pipeline_v13 zgodnie z module_map.  
4. Synchronizacja module_map z dependency_graph.  
5. Dodanie testów integracyjnych modułów.  

---

## 11. Status implementacji
- większość modułów istnieje,  
- DataBridge wymaga implementacji,  
- MeniscusEngine wymaga pełnej integracji,  
- pipeline_v13 wymaga synchronizacji z kontraktami,  
- dokumentacja wymaga aktualizacji.  

---

