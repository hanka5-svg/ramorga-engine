# pipeline_v13/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- integrację modułów: field_state, tension_loop, energy_regulator,
  ritual_detector, entropic_modulator, snapshot_manager,
- wykonanie jednego kroku regulacji pola,
- przygotowanie danych dla testów.

## Wejścia
- `FieldState` (stan początkowy)
- parametry regulacyjne (np. wagi, progi)
- opcjonalnie: `EventInput` (dla ritual_detector)

## Wyjścia
- `FieldState` (stan zaktualizowany)
- `Snapshot` (dla snapshot_manager)
- flagi stabilności (np. TensionStabilityFlag, EnergyStabilityFlag)

## Zależności
- field_state
- tension_loop
- energy_regulator
- ritual_detector
- entropic_modulator
- snapshot_manager

## Testy (powiązanie)
- test_init.md → poprawna inicjalizacja pipeline
- test_regulation_step.md → poprawne wykonanie jednego kroku
- test_energy_stability.md → stabilność energii w pipeline
- test_snapshot.md → poprawna współpraca ze snapshot_manager
