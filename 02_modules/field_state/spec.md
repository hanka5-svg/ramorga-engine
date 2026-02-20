# field_state/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- reprezentację stanu pola (FieldState),
- aktualizację stanu po kroku pipeline,
- udostępnianie stanu innym modułom.

## Wejścia
- `TensionDelta` (z tension_loop)
- `EnergyAdjustment` (z energy_regulator)
- sygnały regulacyjne z pipeline_v13

## Wyjścia
- `FieldState` (aktualny)
- `FieldStatePrev` (poprzedni, opcjonalnie)
- dane do snapshot_manager

## Zależności
- logiczne: tension_loop, energy_regulator, snapshot_manager
- brak zależności implementacyjnych (etap: teoria + testy)

## Testy (powiązanie)
- test_init.md → poprawna inicjalizacja FieldState
- test_regulation_step.md → poprawna aktualizacja po jednym kroku
- test_snapshot.md → poprawna współpraca ze snapshot_manager
