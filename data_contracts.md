# RAMORGA‑ENGINE — Data Contracts

Dokument definiuje kontrakty danych między modułami RAMORGA‑ENGINE.
Każdy moduł operuje wyłącznie na wybranych polach FieldState i zwraca
ściśle określone struktury. Kontrakty są niezmienne i deterministyczne.

---

# 1. FieldState — kontrakt bazowy

FieldState jest jedynym wspólnym medium danych.

## Struktura:

FieldState:
energy_level:float 
tension_map: Dict[str, Any] 
entropy_signature: Dict[str, Any] 
ritual_flags: Dict[str, bool]

## Wymagania:

- wszystkie pola muszą istnieć,
- brak wartości None,
- brak mutacji poza modułem, który jest właścicielem pola,
- clone() musi tworzyć głęboką kopię,
- merge() musi nadpisywać tylko wskazane pola.

---

# 2. tension_loop — kontrakt danych

## Wejście:

tension_map: Dict[str, Any]
params.tension: Dict[str, Any]

## Wyjście:

tension_map: Dict[str, Any] (zaktualizowany)

## Gwarancje:

- nie modyfikuje energy_level,
- nie modyfikuje entropy_signature,
- nie modyfikuje ritual_flags,
- zwraca nową mapę lub czystą mutację (deterministyczną).

---

# 3. energy_regulator — kontrakt danych

## Wejście:

energy_level: float
tension_map: Dict[str, Any]
params.energy: Dict[str, Any]

## Wyjście:

energy_level: float (zaktualizowany)

## Gwarancje:

- nie modyfikuje tension_map,
- nie modyfikuje entropy_signature,
- nie modyfikuje ritual_flags,
- energia musi pozostać w zakresie [E_min, E_max].

---

# 4. entropic_modulator — kontrakt danych

## Wejście:

entropy_signature: Dict[str, Any]
energy_level: float
params.entropy: Dict[str, Any]

## Wyjście:

entropy_signature: Dict[str, Any] (zaktualizowany)

## Gwarancje:

- nie modyfikuje tension_map,
- nie modyfikuje energy_level,
- nie modyfikuje ritual_flags,
- modulacja musi być deterministyczna.

---

# 5. ritual_detector — kontrakt danych

## Wejście:

state: FieldState (pełny)
event_input: Optional[Dict[str, Any]]
params.rituals: Dict[str, Any]

## Wyjście:

ritual_flags: Dict[str, bool]

## Gwarancje:

- nie modyfikuje tension_map,
- nie modyfikuje energy_level,
- nie modyfikuje entropy_signature,
- operuje tylko na odczycie stanu,
- wynik zależy wyłącznie od state + event_input.

---

# 6. snapshot_manager — kontrakt danych

## Wejście:

state: FieldState

## Wyjście:

Snapshot:
data: Dict[str, Any]

oraz:

restore(snapshot) → FieldState

## Gwarancje:

- snapshot musi być pełną serializacją stanu,
- restore musi odtwarzać stan bit‑po‑bicie,
- snapshot nie modyfikuje stanu,
- brak efektów ubocznych.

---

# 7. pipeline_v13 — kontrakt integracyjny

## Wejście:

mode: str
state: Optional[FieldState]
params: Dict[str, Any]
steps: int
snapshot: bool
event_input: Optional[Dict[str, Any]]

## Wyjście:

FieldState (zaktualizowany)
Optional[Snapshot]

## Gwarancje:

- wykonuje moduły w stałej kolejności,
- nie pomija żadnego modułu,
- snapshot jest opcjonalny,
- deterministyczność w test_mode,
- brak mutacji poza FieldState.

---

# 8. Zasady ogólne kontraktów

- **brak ukrytych pól** — wszystkie dane jawne,
- **brak efektów ubocznych** — moduły nie zapisują nic poza swoimi polami,
- **deterministyczność** — identyczne wejście → identyczne wyjście,
- **kompozycyjność** — każdy moduł może być testowany niezależnie,
- **serializowalność** — FieldState musi być w pełni serializowalny.

---

# 9. Podsumowanie

`data_contracts.md` definiuje niezmienne kontrakty danych między modułami
RAMORGA‑ENGINE. Dokument jest podstawą implementacji, testów i integracji.
