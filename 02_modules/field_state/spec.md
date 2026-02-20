# field_state/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- definicję struktury stanu pola (`FieldState`),
- inicjalizację stanu,
- walidację integralności stanu,
- operacje pomocnicze (np. merge, clone).

## Wejścia
- parametry inicjalizacyjne (baseline energii, mapa napięć, sygnatura entropii),
- opcjonalne wartości nadpisujące (dla testów).

## Wyjścia
- poprawnie skonstruowany `FieldState`,
- błędy walidacji przy niepoprawnych danych.

## Zależności
- brak zależności od innych modułów.

## Kontrakt wykonawczy
- `init(params)` tworzy kompletny stan,
- `validate(state)` zwraca błąd lub true,
- brak efektów ubocznych,
- deterministyczny w każdym trybie.

## Powiązanie z testami
- test_init.md — poprawna inicjalizacja,
- test_regulation_step.md — poprawność wejścia do pipeline.
