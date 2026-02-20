# Error Model Contract
# RAMORGA ENGINE — Implementation Layer
# MBP HAI 2.0 + Patch | ATML | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje formalny model błędów (Error Model) dla ramorga-engine.
Model obejmuje:
- klasy błędów,
- propagację błędów,
- punkty detekcji,
- integrację z PipelineV13, MeniscusEngine, Field Engine i V12,
- inwarianty bezpieczeństwa i ciągłości,
- wymagania implementacyjne i testowe.

Celem jest zapewnienie spójnego, deterministycznego i audytowalnego zachowania
systemu w warunkach błędów.

---

## 2. Lokalizacja modułów w repo

error_model.md
pipeline_v13/
04_meniscus_engine/
03_field_engine/
01_runtime/
v12_v13_data_bridge.md
execution_bridge.md
regulation_bridge.md
state_machine.md

---

## 3. Klasy błędów
### 3.1. ERROR_INPUT
Błąd wejścia z MeniscusEngine:
- niepoprawny ATML,
- brak wymaganych pól,
- niepoprawny typ danych.

### 3.2. ERROR_LOAD
Błąd podczas odczytu snapshotu:
- brak snapshotu,
- uszkodzony snapshot,
- niespójność snapshotu z ATML.

### 3.3. ERROR_PIPELINE
Błąd logiki PipelineV13:
- niepoprawna aktualizacja field_state,
- brak wymaganych pól,
- naruszenie inwariantów.

### 3.4. ERROR_REGULATION
Błąd regulatorów:
- błąd tension_loop,
- błąd energy_regulator,
- błąd entropic_modulator,
- niespójność wartości regulacyjnych.

### 3.5. ERROR_SAVE
Błąd zapisu snapshotu:
- błąd serializacji,
- błąd zapisu do LTM,
- niespójność snapshotu po zapisie.

### 3.6. ERROR_SYSTEM
Błąd systemowy:
- wyjątek nieobsłużony,
- błąd środowiska wykonawczego.

---

## 4. Struktura błędu (ATML)

error:
type: str
code: str
message: str
details: dict
timestamp: int
state: str
request_id: str

---

## 5. Punkty detekcji błędów
### 5.1. MeniscusEngine
- walidacja ATML,
- normalizacja wejścia,
- generowanie ERROR_INPUT.

### 5.2. V12 (LTM + drift)
- odczyt snapshotu → ERROR_LOAD,
- zapis snapshotu → ERROR_SAVE.

### 5.3. PipelineV13
- logika pipeline → ERROR_PIPELINE,
- brak wymaganych pól → ERROR_PIPELINE.

### 5.4. Field Engine
- błąd regulatorów → ERROR_REGULATION,
- niespójność wartości regulacyjnych → ERROR_REGULATION.

---

## 6. Propagacja błędów
### 6.1. Zasada nadrzędna
Każdy błąd przechodzi do stanu ERROR w formalnym automacie stanów.

### 6.2. Propagacja

ANY_STATE → ERROR → RESPOND → END

### 6.3. Wymagania
- brak ukrywania błędów,
- brak pomijania błędów regulatorów,
- brak kontynuacji wykonania po ERROR.

---

## 7. Integracja z PipelineV13
### 7.1. PipelineV13 musi:
- przechwytywać błędy regulatorów,
- przechwytywać błędy snapshotu,
- przechwytywać błędy logiki pipeline,
- przechodzić do stanu ERROR.

### 7.2. PipelineV13 nie może:
- ignorować błędów,
- kontynuować wykonania po błędzie.

---

## 8. Integracja z MeniscusEngine
### 8.1. MeniscusEngine musi:
- generować ERROR_INPUT,
- formatować odpowiedź błędu,
- zwracać ATML-compliant error payload.

### 8.2. Format odpowiedzi błędu

output_payload:
request_id: str
timestamp: int
status: "error"
error: <error object>

---

## 9. Integracja z Field Engine
### 9.1. Field Engine musi:
- zgłaszać błędy regulatorów,
- zgłaszać niespójność wartości regulacyjnych,
- nie próbować naprawiać błędów.

---

## 10. Integracja z V12 (LTM + drift)
### 10.1. V12 musi:
- zgłaszać błędy odczytu snapshotu,
- zgłaszać błędy zapisu snapshotu,
- nie próbować naprawiać snapshotu.

---

## 11. Inwarianty Error Model
### 11.1. Inwarianty danych
- error.type ∈ {INPUT, LOAD, PIPELINE, REGULATION, SAVE, SYSTEM},
- error.timestamp musi być monotoniczny,
- error.state musi wskazywać stan, w którym wystąpił błąd.

### 11.2. Inwarianty wykonania
- ERROR musi prowadzić do RESPOND,
- RESPOND musi prowadzić do END,
- brak kontynuacji wykonania po ERROR.

### 11.3. Inwarianty ciągłości
- brak utraty request_id,
- brak utraty informacji o stanie,
- brak częściowych zapisów snapshotu po błędzie.

---

## 12. Wymagania implementacyjne
### 12.1. Moduły wymagane
- error_model.md
- pipeline_v13/
- 04_meniscus_engine/
- 03_field_engine/
- 01_runtime/

### 12.2. Funkcje wymagane

Error.raise(type, code, message, details)
Error.format_for_output()

### 12.3. Testy wymagane
- test_error_input
- test_error_load
- test_error_pipeline
- test_error_regulation
- test_error_save
- test_error_system
- test_error_propagation
- test_error_output_format

---

## 13. Status implementacji
- error_model.md: istnieje,
- brak formalnego kontraktu — niniejszy dokument go definiuje,
- pipeline_v13: wymaga integracji z Error Model,
- MeniscusEngine: wymaga implementacji obsługi błędów,
- Field Engine: wymaga propagacji błędów regulatorów,
- V12: wymaga propagacji błędów snapshotu.

---

## 14. Działania wymagane
1. Implementacja Error.raise() i Error.format_for_output().  
2. Integracja Error Model w pipeline_v13/.  
3. Dodanie obsługi błędów w MeniscusEngine.  
4. Dodanie propagacji błędów w Field Engine.  
5. Dodanie propagacji błędów w V12.  
6. Aktualizacja state_machine.md (stan ERROR).  
7. Dodanie testów błędów i propagacji.  

---
