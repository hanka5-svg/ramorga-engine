# tension_loop/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- obliczanie napięcia pola,
- regulację napięcia w czasie,
- wykrywanie oscylacji napięcia.

## Wejścia
- `FieldState`
- parametry regulacyjne (np. wagi, progi stabilności)

## Wyjścia
- `TensionDelta`
- `TensionStabilityFlag` (np. STABLE / UNSTABLE / OSCILLATING)

## Zależności
- logiczne: field_state, energy_regulator
- brak implementacji (stub na etapie teorii + testów)

## Testy (powiązanie)
- test_regulation_step.md → poprawne wyliczenie TensionDelta
- test_energy_stability.md → wpływ napięcia na stabilność energii
