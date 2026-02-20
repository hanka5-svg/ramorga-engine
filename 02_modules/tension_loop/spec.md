# tension_loop/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- aktualizację `tension_map`,
- modelowanie lokalnych i globalnych napięć,
- przygotowanie danych dla regulatora energii.

## Wejścia
- `tension_map`,
- parametry regulacyjne (progi, wagi).

## Wyjścia
- zaktualizowany `tension_map`,
- opcjonalne flagi stabilności napięcia.

## Zależności
- field_state (struktura danych).

## Kontrakt wykonawczy
- brak modyfikacji innych pól stanu,
- deterministyczny w test_mode,
- brak losowości,
- brak efektów ubocznych.

## Powiązanie z testami
- test_regulation_step.md — poprawna aktualizacja napięć,
- test_energy_stability.md — wpływ napięć na energię.
