# ritual_detector/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- wykrywanie aktywacji rytuałów,
- analizę stanu pola i opcjonalnych zdarzeń (`EventInput`),
- ustawianie `ritual_flags`.

## Wejścia
- pełny `FieldState`,
- opcjonalnie: `EventInput`.

## Wyjścia
- `ritual_flags`,
- metadane aktywacji.

## Zależności
- field_state,
- energy_regulator,
- tension_loop.

## Kontrakt wykonawczy
- zero fałszywych aktywacji w test_mode,
- deterministyczny,
- brak modyfikacji innych pól poza `ritual_flags`.

## Powiązanie z testami
- test_regulation_step.md — brak aktywacji przy stanie bazowym,
- test_energy_stability.md — brak fałszywych rytuałów.
