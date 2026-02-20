# ritual_detector/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- wykrywanie pęknięć rytuału (rupture events),
- ocenę integralności rytuału (warstwa Goffmana),
- klasyfikację eventów rytualnych.

## Wejścia
- `FieldState`
- `EventInput` (zdarzenia z otoczenia, np. sekwencje zachowań)

## Wyjścia
- `RitualStatus` (np. OK / DEGRADED / BROKEN)
- `RitualFailureEvent` (sygnał dla entropic_modulator)

## Zależności
- logiczne: entropic_modulator, field_state
- brak implementacji (analiza teoretyczna + testy scenariuszy)

## Testy (powiązanie)
- (do dodania) testy scenariuszy pęknięcia rytuału
