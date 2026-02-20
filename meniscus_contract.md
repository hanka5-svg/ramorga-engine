# Meniscus Contract
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny kontrakt warstwy MeniscusEngine — jedynej bramy wejścia/wyjścia
dla ramorga-engine. Meniscus jest warstwą graniczną pomiędzy światem zewnętrznym a
pipeline V13 i Field Engine.

Kontrakt określa:
- odpowiedzialności warstwy,
- interfejsy wejścia/wyjścia,
- inwarianty,
- przepływ wykonania,
- wymagania implementacyjne,
- punkty integracji z V13 i V12.

---

## 2. Lokalizacja modułów w repo

04_meniscus_engine/
05_api/
06_integration/
pipeline_v13/
03_field_engine/
01_runtime/

---

## 3. Zakres odpowiedzialności MeniscusEngine
### 3.1. Odpowiedzialności
- przyjmowanie wejść z API i integracji,
- walidacja danych wejściowych,
- normalizacja danych do formatu ATML,
- inicjalizacja cyklu wykonania,
- przekazanie sterowania do PipelineV13,
- odbiór wyników z pipeline,
- przygotowanie odpowiedzi dla API/integracji.

### 3.2. Zakres niedozwolony
MeniscusEngine **nie wykonuje**:
- regulacji pola,
- operacji na field_state,
- operacji na pamięci V12,
- logiki pipeline.

---

## 4. Interfejs wejścia/wyjścia
### 4.1. Wejście

MeniscusEngine.receive(input_payload) → normalized_payload

### 4.2. Wyjście

MeniscusEngine.respond(output_payload)

### 4.3. Format wejścia (ATML)

input_payload:
request_id: str
timestamp: int
source: str
data: dict

### 4.4. Format wyjścia (ATML)

output_payload:
request_id: str
timestamp: int
status: str
data: dict

---

## 5. Przepływ wykonania (Execution Flow)
### 5.1. Sekwencja

1. receive(input_payload)

2. validate(input_payload)

3. normalize(input_payload)

4. LOAD (V12 → V13):
snapshot = LTM.read()
field_state = DataBridge.load(snapshot)

5. EXECUTE (V13 + Field Engine):
field_state = PipelineV13.step()
field_state = FieldEngine.step()

6. SAVE (V13 → V12):
snapshot = DataBridge.save(field_state)
LTM.write(snapshot)

7. respond(output_payload)

### 5.2. Zasada nadrzędna
MeniscusEngine **nie może** wywołać V12 ani Field Engine bezpośrednio.  
Wywołania muszą przechodzić przez PipelineV13.

---

## 6. Inwarianty MeniscusEngine
### 6.1. Inwarianty danych
- input_payload musi być zgodny z ATML,
- request_id musi być unikalny,
- timestamp musi być monotoniczny,
- brak danych nieznormalizowanych.

### 6.2. Inwarianty wykonania
- MeniscusEngine jest jedyną bramą wejścia/wyjścia,
- LOAD musi poprzedzać EXECUTE,
- SAVE musi następować po EXECUTE,
- brak bezpośrednich wywołań V12 lub Field Engine.

### 6.3. Inwarianty ciągłości
- brak utraty request_id,
- brak modyfikacji input_payload poza normalizacją,
- brak modyfikacji output_payload poza formatowaniem.

---

## 7. Integracja z PipelineV13
### 7.1. Wywołanie pipeline

field_state = PipelineV13.step(normalized_payload, field_state)

### 7.2. Wymagania
- PipelineV13 musi przyjmować normalized_payload,
- PipelineV13 musi zwracać field_state,
- PipelineV13 musi wywołać FieldEngine.step().

---

## 8. Integracja z V12 (LTM + drift)
### 8.1. LOAD

snapshot = LTM.read()
field_state = DataBridge.load(snapshot)

### 8.2. SAVE

snapshot = DataBridge.save(field_state)
LTM.write(snapshot)

### 8.3. Wymagania
- MeniscusEngine nie wywołuje LTM bezpośrednio,
- PipelineV13 zarządza LOAD/SAVE.

---

## 9. Wymagania implementacyjne
### 9.1. Moduły wymagane
- MeniscusEngine (04_meniscus_engine/)
- DataBridge (nowy moduł)
- aktualizacja pipeline_v13/ o integrację z MeniscusEngine

### 9.2. Funkcje wymagane

MeniscusEngine.receive()
MeniscusEngine.validate()
MeniscusEngine.normalize()
MeniscusEngine.respond()

### 9.3. Testy wymagane
- test_meniscus_receive
- test_meniscus_normalization
- test_meniscus_execution_flow
- test_meniscus_invariants
- test_meniscus_pipeline_integration

---

## 10. Status implementacji
- MeniscusEngine: skeleton (wymaga implementacji kontraktu),
- PipelineV13: wymaga integracji z MeniscusEngine,
- Field Engine: kompletna warstwa regulacji,
- V12: kompletna warstwa pamięci,
- Dokumentacja: wymaga synchronizacji.

---

## 11. Działania wymagane
1. Implementacja pełnego MeniscusEngine.
2. Dodanie normalizacji ATML.
3. Integracja MeniscusEngine → PipelineV13.
4. Dodanie testów MeniscusEngine.
5. Aktualizacja execution_flow.md.
6. Synchronizacja state_machine.md.

---

