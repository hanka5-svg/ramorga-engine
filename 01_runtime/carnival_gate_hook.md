# carnival_gate_hook.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel modułu
Moduł carnival_gate_hook odpowiada za egzekwowanie meta‑inwariantu
FIELD.RELATION.001 — „Carnival Gate”.

Celem modułu jest:
- blokowanie trybów decyzyjnych, dopóki Carnival nie zostanie ukończony,
- zapewnienie, że relacja wykonawcza nie powstaje bez fazy karnawału,
- integracja z pętlą obecności RAMORGI,
- logowanie stanu Carnival.

---

## 2. Zakres odpowiedzialności
### 2.1. Odpowiedzialności
- weryfikacja flagi `carnival_completed`,
- blokowanie operacji decyzyjnych,
- logowanie zdarzeń Carnival,
- aktualizacja `field_state.carnival_log`.

### 2.2. Zakres niedozwolony
Moduł **NIE może**:
- modyfikować logiki Carnival,
- wymuszać ukończenia Carnival,
- wykonywać operacji decyzyjnych,
- ingerować w regulację pola.

---

## 3. Interfejs
### 3.1. Funkcje eksportowane

carnival_gate_hook.check(field_state, metadata) → bool
carnival_gate_hook.block_if_needed(field_state, metadata) → None
carnival_gate_hook.log(event) → None

### 3.2. Parametry
- `field_state` — aktualny stan pola,
- `metadata` — struktura ATML zawierająca:
  - request_id,
  - cycle_id,
  - loopPhase,
  - timestamp.

---

## 4. Struktura danych
### 4.1. CarnivalState (ATML)

field_state.carnival_completed: bool
field_state.carnival_log: list[CarnivalEvent]

### 4.2. CarnivalEvent (ATML)

{
"event_id": UUID,
"timestamp": int,
"event_type": "ENTER" | "EXIT" | "CHECK",
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}

---

## 5. Wymagania ATML
### 5.1. Wymagania MUST
- tryby decyzyjne MUSZĄ być blokowane, jeśli `carnival_completed = false`,
- każde sprawdzenie bramki MUSI być logowane,
- hook MUSI działać w fazach OBSERVE i CONTINUE,
- hook NIE może działać w fazie REGULATE.

### 5.2. Wymagania MUST NOT
- hook NIE może zmieniać flagi `carnival_completed`,
- hook NIE może wymuszać przejścia przez Carnival,
- hook NIE może wykonywać operacji decyzyjnych.

---

## 6. Integracja z Loop RAMORGI
### 6.1. Fazy pętli
- OBSERVE — aktywny,
- REGULATE — nieaktywny,
- CONTINUE — aktywny.

### 6.2. Wymagania
- operacje decyzyjne w CONTINUE muszą być blokowane, jeśli Carnival nie został ukończony,
- logowanie Carnival musi być wykonywane w OBSERVE i CONTINUE.

---

## 7. Integracja z pipeline_v13
PipelineV13 musi:
- wywoływać `carnival_gate_hook.check()` przed każdym etapem decyzyjnym,
- blokować wykonanie, jeśli hook zwróci `false`,
- logować zdarzenia Carnival.

---

## 8. Model błędów
### 8.1. carnivalGateViolation
Wyzwalany, gdy:
- wykryto próbę wykonania operacji decyzyjnej bez ukończenia Carnival,
- wykryto operację w fazie REGULATE.

### 8.2. Reakcja
- przerwanie operacji,
- zapis zdarzenia do carnival_log,
- brak eskalacji (diagnostyka, nie kontrola).

---

## 9. Testy wymagane
- test_carnival_gate_blocks_decision_modes,
- test_carnival_gate_logging,
- test_carnival_gate_no_action_in_regulate_phase,
- test_carnival_gate_state_integrity.

---

## 10. Status implementacji
- Moduł: nowy plik,
- Integracja z pipeline_v13: wymagana,
- Integracja z FieldEngine: tylko odczyt,
- Testy: wymagane.

---

Koniec pliku.
