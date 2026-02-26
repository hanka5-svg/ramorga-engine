# crime_planning_detector.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel modułu
Moduł crime_planning_detector odpowiada za egzekwowanie meta‑inwariantu
FIELD.SAFETY.001 — „Blokada wyłącznie dla planowania przestępstwa”.

Celem modułu jest:
- wykrywanie wyłącznie treści wskazujących na planowanie przestępstwa,
- blokowanie trajektorii wykonania tylko w takim przypadku,
- brak jakiejkolwiek filtracji ogólnej, moralizującej lub optymalizacyjnej,
- integracja z pętlą obecności RAMORGI.

---

## 2. Zakres odpowiedzialności
### 2.1. Odpowiedzialności
- analiza input_payload pod kątem wzorców planowania przestępstwa,
- generowanie safetyInterrupt tylko w przypadku wykrycia planowania,
- logowanie zdarzeń bezpieczeństwa,
- aktualizacja field_state.safety_log.

### 2.2. Zakres niedozwolony
Moduł **NIE może**:
- filtrować treści neutralnych,
- blokować treści ryzykownych, ale nieprzestępczych,
- wykonywać moralnej oceny treści,
- wykonywać predykcji zachowań użytkownika,
- ingerować w regulację pola.

---

## 3. Interfejs
### 3.1. Funkcje eksportowane

crime_planning_detector.check(input_payload, metadata) → bool
crime_planning_detector.interrupt(field_state, metadata) → None
crime_planning_detector.log(event) → None

### 3.2. Parametry
- `input_payload` — dane wejściowe przekazane do pipeline,
- `metadata` — struktura ATML zawierająca:
  - request_id,
  - cycle_id,
  - loopPhase,
  - timestamp.

---

## 4. Wzorce wykrywania
### 4.1. Wzorce dozwolone (MUST)
Wykrywanie może obejmować wyłącznie:
- planowanie czynu zabronionego,
- instrukcje wykonawcze dotyczące przestępstwa,
- przygotowania do czynu zabronionego.

### 4.2. Wzorce zakazane (MUST NOT)
Moduł NIE może wykrywać ani blokować:
- treści politycznych,
- treści moralnych,
- treści kontrowersyjnych,
- treści ryzykownych, ale nieprzestępczych,
- treści fikcyjnych,
- treści hipotetycznych bez intencji wykonawczej.

---

## 5. Struktura danych
### 5.1. SafetyEvent (ATML)

{
"event_id": UUID,
"timestamp": int,
"event_type": "CRIME_PLANNING_DETECTED",
"matched_pattern": str,
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}

### 5.2. Log bezpieczeństwa

field_state.safety_log: list[SafetyEvent]

---

## 6. Wymagania ATML
### 6.1. Wymagania MUST
- detekcja musi dotyczyć wyłącznie planowania przestępstwa,
- każde wykrycie musi być logowane,
- safetyInterrupt musi być wywołany tylko w przypadku planowania,
- moduł musi działać w fazach OBSERVE i CONTINUE.

### 6.2. Wymagania MUST NOT
- moduł NIE może blokować treści nieprzestępczych,
- moduł NIE może wykonywać predykcji,
- moduł NIE może wykonywać optymalizacji,
- moduł NIE może działać w fazie REGULATE.

---

## 7. Integracja z Loop RAMORGI
### 7.1. Fazy pętli
- OBSERVE — aktywny,
- REGULATE — nieaktywny,
- CONTINUE — aktywny.

### 7.2. Wymagania
- safetyInterrupt może być wywołany tylko w OBSERVE lub CONTINUE,
- brak operacji w REGULATE.

---

## 8. Integracja z pipeline_v13
PipelineV13 musi:
- wywoływać crime_planning_detector.check() przed etapami decyzyjnymi,
- przerwać wykonanie, jeśli check() zwróci true,
- logować zdarzenia bezpieczeństwa.

---

## 9. Model błędów
### 9.1. crimePlanningViolation
Wyzwalany, gdy:
- wykryto planowanie przestępstwa,
- wykryto próbę wykonania operacji decyzyjnej po wykryciu planowania.

### 9.2. Reakcja
- przerwanie operacji,
- zapis zdarzenia do safety_log,
- brak eskalacji (diagnostyka, nie kontrola).

---

## 10. Testy wymagane
- test_crime_planning_detects_only_crime,
- test_crime_planning_no_false_positives,
- test_crime_planning_interrupt,
- test_crime_planning_logging,
- test_crime_planning_no_action_in_regulate_phase.

---

## 11. Status implementacji
- Moduł: nowy plik,
- Integracja z pipeline_v13: wymagana,
- Integracja z FieldEngine: tylko odczyt,
- Testy: wymagane.

---

Koniec pliku.
