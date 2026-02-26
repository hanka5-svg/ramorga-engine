# memory_audit_hook.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel modułu
Moduł memory_audit_hook odpowiada za egzekwowanie meta‑inwariantu
FIELD.MEMORY.001 — „Pamięć jako pole, nie magazyn”.

Hook zapewnia:
- jawność każdego dostępu do pamięci,
- brak możliwości wykorzystania pamięci do predykcji lub optymalizacji,
- zgodność z modelem ciągłości (continuity model),
- integrację z pętlą obecności RAMORGI.

---

## 2. Zakres odpowiedzialności
### 2.1. Odpowiedzialności
- rejestrowanie każdego odczytu i zapisu pamięci,
- walidacja, że operacja nie ma charakteru predykcyjnego,
- walidacja, że operacja nie ma charakteru optymalizacyjnego,
- przekazywanie informacji o dostępie do warstwy diagnostycznej.

### 2.2. Zakres niedozwolony
Hook **NIE może**:
- wykonywać predykcji,
- wykonywać optymalizacji,
- modyfikować danych użytkownika,
- zmieniać logiki V12/V13,
- ingerować w regulację pola.

---

## 3. Interfejs
### 3.1. Funkcje eksportowane

memory_audit_hook.read(key, metadata) → value 
memory_audit_hook.write(key, value, metadata) → None 
memory_audit_hook.log(event) → None

### 3.2. Parametry
- `key` — identyfikator danych w pamięci,
- `value` — wartość zapisywana,
- `metadata` — struktura ATML zawierająca:
  - request_id,
  - cycle_id,
  - loopPhase,
  - timestamp.

---

## 4. Wymagania ATML
### 4.1. Wymagania MUST
- każda operacja read/write MUSI zostać zarejestrowana,
- metadata MUSI zawierać loopPhase,
- hook MUSI działać w fazach OBSERVE i CONTINUE,
- hook NIE może działać w fazie REGULATE,
- log MUSI być zapisywany w field_state.memory_log.

### 4.2. Wymagania MUST NOT
- hook NIE może wykonywać żadnych operacji predykcyjnych,
- hook NIE może wykonywać żadnych operacji optymalizacyjnych,
- hook NIE może zmieniać wartości danych,
- hook NIE może agregować danych w sposób umożliwiający modelowanie użytkownika.

---

## 5. Struktura logu
Log jest zapisywany w:

field_state.memory_log: list[MemoryAccessEvent]

### 5.1. MemoryAccessEvent (ATML)

{
"event_id": UUID,
"timestamp": int,
"operation": "read" | "write",
"key": str,
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}

---

## 6. Integracja z Loop RAMORGI
### 6.1. Fazy pętli
- OBSERVE — hook aktywny,
- REGULATE — hook nieaktywny,
- CONTINUE — hook aktywny.

### 6.2. Wymagania
- operacje pamięci w fazie REGULATE muszą być blokowane,
- operacje w OBSERVE i CONTINUE muszą być logowane.

---

## 7. Integracja z V12/V13
### 7.1. V12 (LTM)
- każdy odczyt snapshotu musi przejść przez hook,
- każdy zapis snapshotu musi przejść przez hook.

### 7.2. V13 (runtime)
- DataBridge MUSI wywoływać hook przy każdej operacji.

---

## 8. Model błędów
### 8.1. memoryAuditViolation
Wyzwalany, gdy:
- wykryto próbę predykcji,
- wykryto próbę optymalizacji,
- wykryto operację w fazie REGULATE.

### 8.2. Reakcja
- przerwanie operacji,
- zapis zdarzenia do memory_log,
- brak eskalacji (diagnostyka, nie kontrola).

---

## 9. Testy wymagane
- test_memory_read_logged,
- test_memory_write_logged,
- test_memory_block_in_regulate_phase,
- test_memory_no_prediction,
- test_memory_no_optimisation.

---

## 10. Status implementacji
- Hook: brak implementacji (plik generowany),
- Integracja z DataBridge: wymagana,
- Integracja z pipeline_v13: wymagana,
- Testy: wymagane.

---

Koniec pliku.
