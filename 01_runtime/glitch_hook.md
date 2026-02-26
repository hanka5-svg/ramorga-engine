# glitch_hook.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel modułu
Moduł glitch_hook odpowiada za egzekwowanie meta‑inwariantu
FIELD.GLITCH.001 — „Obowiązkowy kanał glitch”.

Celem modułu jest:
- zapewnienie, że każdy etap pipeline posiada kanał glitchOut,
- propagacja glitch bez normalizacji i tłumienia,
- logowanie zdarzeń glitch,
- integracja z pętlą obecności RAMORGI.

---

## 2. Zakres odpowiedzialności
### 2.1. Odpowiedzialności
- rejestrowanie zdarzeń glitch,
- propagacja glitch między modułami,
- aktualizacja field_state.glitch_log,
- walidacja, że glitch nie został usunięty ani wygładzony.

### 2.2. Zakres niedozwolony
Moduł **NIE może**:
- modyfikować wartości glitch,
- usuwać glitch,
- normalizować sygnału,
- wykonywać korekcji błędów,
- ingerować w regulację pola.

---

## 3. Interfejs
### 3.1. Funkcje eksportowane

glitch_hook.emit(glitch_event, metadata) → None
glitch_hook.propagate(glitch_event, next_module) → None
glitch_hook.log(glitch_event) → None

### 3.2. Parametry
- `glitch_event` — struktura ATML opisująca anomalię,
- `metadata` — struktura ATML zawierająca:
  - request_id,
  - cycle_id,
  - loopPhase,
  - timestamp.

---

## 4. Struktura danych
### 4.1. GlitchEvent (ATML)

{
"event_id": UUID,
"timestamp": int,
"source_module": str,
"description": str,
"severity": "LOW" | "MEDIUM" | "HIGH",
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}

### 4.2. Log glitch

field_state.glitch_log: list[GlitchEvent]

---

## 5. Wymagania ATML
### 5.1. Wymagania MUST
- każdy moduł MUSI posiadać glitchOut,
- każde zdarzenie glitch MUSI zostać zarejestrowane,
- glitch MUSI być propagowany bez zmian,
- glitch MUSI być logowany w field_state.glitch_log,
- hook MUSI działać w fazach OBSERVE i CONTINUE.

### 5.2. Wymagania MUST NOT
- glitch NIE może być normalizowany,
- glitch NIE może być usuwany,
- glitch NIE może być wygładzany,
- glitch NIE może być reinterpretowany.

---

## 6. Integracja z Loop RAMORGI
### 6.1. Fazy pętli
- OBSERVE — hook aktywny,
- REGULATE — hook nieaktywny,
- CONTINUE — hook aktywny.

### 6.2. Wymagania
- operacje glitch w fazie REGULATE muszą być blokowane,
- glitch musi być propagowany w OBSERVE i CONTINUE.

---

## 7. Integracja z pipeline_v13
- każdy etap pipeline musi wywoływać glitch_hook.emit() przy wykryciu anomalii,
- glitchOut musi być przekazywany do kolejnego modułu,
- pipeline nie może usuwać glitch.

---

## 8. Model błędów
### 8.1. glitchSuppressionViolation
Wyzwalany, gdy:
- wykryto brak propagacji glitch,
- wykryto normalizację glitch,
- wykryto usunięcie glitch.

### 8.2. Reakcja
- zapis zdarzenia do glitch_log,
- brak eskalacji (diagnostyka, nie kontrola).

---

## 9. Testy wymagane
- test_glitch_emit_logged,
- test_glitch_propagation_chain,
- test_glitch_block_in_regulate_phase,
- test_glitch_no_normalisation,
- test_glitch_no_suppression.

---

## 10. Status implementacji
- Moduł: nowy plik,
- Integracja z pipeline_v13: wymagana,
- Integracja z FieldEngine: diagnostyczna,
- Testy: wymagane.

---

Koniec pliku.
