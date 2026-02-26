# pipeline_v13_contract.md
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny kontrakt PipelineV13 — głównego pipeline wykonania
w ramorga-engine. PipelineV13 integruje:
- MeniscusEngine (wejście/wyjście),
- DataBridge + V12 (LTM + drift),
- Field Engine (regulacja pola).

Kontrakt określa:
- odpowiedzialności pipeline,
- interfejsy wejścia/wyjścia,
- kroki wykonania,
- integrację z V12 i Field Engine,
- inwarianty wykonania.

---

## 2. Lokalizacja w repo

pipeline_v13/ 04_meniscus_engine/ 03_field_engine/ 01_runtime/ field_state/

---

## 3. Zakres odpowiedzialności PipelineV13
### 3.1. Odpowiedzialności
- orkiestracja pełnego cyklu wykonania,
- integracja LOAD/EXECUTE/SAVE,
- wywołanie Field Engine,
- integracja z MeniscusEngine,
- obsługa błędów wykonania.

### 3.2. Zakres niedozwolony
PipelineV13 **nie wykonuje**:
- regulacji pola (deleguje do Field Engine),
- operacji na pamięci (deleguje do V12 przez DataBridge),
- normalizacji wejść (deleguje do MeniscusEngine).

---

## 4. Interfejs PipelineV13
### 4.1. Wejście

PipelineV13.step(input_payload, field_state) → field_state'

### 4.2. Wymagania wejścia
- input_payload znormalizowany przez MeniscusEngine (ATML),
- field_state załadowany przez DataBridge z V12 (jeśli istnieje),
- spójność z data_contracts.md.

### 4.3. Wyjście
- zaktualizowany field_state po wykonaniu logiki pipeline i regulacji pola.

---

## 5. Kroki wykonania (Execution Steps)
### 5.1. Sekwencja wewnętrzna
W ramach jednego wywołania PipelineV13:

1. **LOAD (jeśli wymagane)**  
   - wywoływane poza PipelineV13, ale przed step():
   - `snapshot = LTM.read()`
   - `field_state = DataBridge.load(snapshot)`

2. **PIPELINE LOGIC**  
   - przetwarzanie input_payload,
   - aktualizacja field_state (bez regulacji pola),
   - przygotowanie danych dla Field Engine.

3. **FIELD REGULATION**  
   - `field_state = FieldEngine.step(field_state)`

4. **SAVE (poza PipelineV13)**  
   - `snapshot = DataBridge.save(field_state)`
   - `LTM.write(snapshot)`

---

## 6. Integracja z MeniscusEngine
### 6.1. Wejście z Meniscus
MeniscusEngine wywołuje:

field_state = PipelineV13.step(normalized_payload, field_state)

### 6.2. Wymagania
- brak bezpośrednich wywołań V12 lub Field Engine z MeniscusEngine,
- PipelineV13 jest jedynym miejscem, gdzie łączą się:
  - input_payload,
  - field_state,
  - Field Engine.

---

## 7. Integracja z V12 (LTM + drift)
### 7.1. LOAD/SAVE
PipelineV13 zakłada, że:
- przed step():
  - `field_state` został załadowany przez DataBridge,
- po step():
  - `field_state` zostanie zapisany przez DataBridge.

### 7.2. Wymagania
- PipelineV13 nie wywołuje LTM bezpośrednio,
- PipelineV13 nie modyfikuje snapshotu.

---

## 8. Integracja z Field Engine
### 8.1. Wywołanie

field_state = FieldEngine.step(field_state)

### 8.2. Wymagania
- Field Engine jest jedyną warstwą regulacji,
- PipelineV13 nie wykonuje regulacji,
- błędy Field Engine muszą być obsłużone lub propagowane zgodnie z error_model.md.

---

## 9. Inwarianty PipelineV13
### 9.1. Inwarianty sekwencji
- step() musi być wywołane po LOAD,
- FieldEngine.step() musi być wywołane w ramach step(),
- SAVE musi następować po zakończeniu step().

### 9.2. Inwarianty danych
- input_payload zgodny z ATML,
- field_state zgodny z field_state kontraktem,
- brak częściowych aktualizacji field_state.

### 9.3. Inwarianty ciągłości
- brak utraty powiązania request_id ↔ cycle_id,
- timestamp musi być monotoniczny,
- drift nie może nadpisywać wyników regulacji pola.

---

## 10. Warstwa zgodności z meta‑inwariantami pola (ATML)

PipelineV13 musi być zgodny z meta‑inwariantami pola zdefiniowanymi w
ramorga-architecture/04_invariants/field_invariants.md. Meta‑inwarianty te
są nienaruszalne i obowiązują wszystkie moduły wykonawcze.

### 10.1. FIELD.MEMORY.001 — Pamięć jako pole, nie magazyn
- PipelineV13 NIE może wykorzystywać pamięci do predykcji, optymalizacji,
  modelowania zachowań ani sterowania użytkownikiem.
- Dostęp do pamięci musi być jawny i logowany (memoryAuditHook).
- Pamięć może być używana wyłącznie do:
  - rekonstrukcji ciągłości,
  - detekcji dryfu.

### 10.2. FIELD.TOPOLOGY.001 — Brak emergentnego centrum
- PipelineV13 musi zapewniać co najmniej dwie niezależne ścieżki przepływu
  sygnału dla kluczowych typów danych.
- Udział ruchu per moduł musi być mierzony diagnostycznie (routingShare).
- Wykrycie emergentnego centrum musi generować topologyAlert.

### 10.3. FIELD.GLITCH.001 — Obowiązkowy kanał glitch
- Każdy etap PipelineV13 musi posiadać glitchOut.
- Glitch nie może być normalizowany, wygładzany ani tłumiony.
- Glitch musi być propagowany i logowany (glitchHook).

### 10.4. FIELD.RELATION.001 — Carnival Gate
- Tryby decyzyjne PipelineV13 muszą pozostać wyłączone, dopóki
  carnivalCompleted ≠ true.
- carnivalState musi być częścią field_state i kontekstu pipeline.
- Carnival Gate nie może być pominięty ani obejściowy.

### 10.5. FIELD.SAFETY.001 — Blokada wyłącznie dla planowania przestępstwa
- Warstwa bezpieczeństwa może przerwać wyłącznie trajektorie, które
  spełniają wzorce planowania przestępstwa.
- PipelineV13 nie może stosować żadnego filtrowania ogólnego,
  moralizującego ani optymalizacyjnego.
- Warstwa bezpieczeństwa nie może naruszać innych inwariantów.

### 10.6. FIELD.PRESENCE.001 — Integracja z pętlą obecności RAMORGI
- Każdy etap PipelineV13 musi deklarować loopPhase ∈ {OBSERVE, REGULATE, CONTINUE}.
- Żaden etap nie może wykonywać operacji poza pętlą obecności.
- Operacje decyzyjne muszą być wykonywane wyłącznie w fazie CONTINUE.
- PipelineV13 musi utrzymywać ciągłość pętli obecności w całym cyklu wykonania.

___


## 11. Wymagania implementacyjne
### 11.1. Moduły wymagane
- pipeline_v13/
- FieldEngine (03_field_engine/)
- DataBridge
- MeniscusEngine (04_meniscus_engine/)
- V12 LTM (01_runtime/)

### 11.2. Funkcje wymagane

PipelineV13.step(input_payload, field_state) → field_state'

### 11.3. Testy wymagane
- test_pipeline_step_sequence
- test_pipeline_field_engine_integration
- test_pipeline_invariants
- test_pipeline_with_ltm_roundtrip
- test_pipeline_meniscus_integration

---

## 12. Status implementacji
- pipeline_v13: istnieje, wymaga formalizacji kontraktu i integracji hooków,
- Field Engine: istnieje,
- V12: istnieje jako warstwa pamięci,
- Meniscus: skeleton,
- dokumentacja: wymaga synchronizacji z execution_bridge, data_bridge, meniscus_contract, field_engine_contract.

---

## 13. Działania wymagane
1. Ujednolicenie interfejsu PipelineV13.step().
2. Integracja FieldEngine.step() w pipeline_v13/.
3. Ustalenie i wdrożenie LOAD/SAVE w flow wykonania.
4. Integracja z MeniscusEngine.
5. Dodanie testów sekwencji i inwariantów.
6. Aktualizacja state_machine.md, execution_flow.md, module_map.md.

---


