# pipeline_v13/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- integrację modułów: `field_state`, `tension_loop`, `energy_regulator`,
  `ritual_detector`, `entropic_modulator`, `snapshot_manager`,
- wykonanie jednego kroku regulacji pola,
- obsługę trybów: init, single_step, multi_step, test_mode,
- przygotowanie danych dla testów (deterministyczność, snapshoty).

## Wejścia
- `FieldState` — stan początkowy lub null (dla init),
- parametry regulacyjne (np. wagi, progi, konfiguracje modułów),
- opcjonalnie: `EventInput` (dla `ritual_detector`),
- tryb pracy: `init | single_step | multi_step | test_mode`,
- liczba kroków (dla multi_step),
- flaga snapshotów: `true | false | "each" | "final"`.

## Wyjścia
- `FieldState` — stan zaktualizowany po wykonaniu kroku/kroków,
- `Snapshot` — serializacja stanu (jeśli snapshot_manager aktywny),
- flagi stabilności:
  - `TensionStabilityFlag`,
  - `EnergyStabilityFlag`,
  - opcjonalnie: `EntropyStabilityFlag`,
- metadane wykonania:
  - liczba wykonanych kroków,
  - aktywacje rytuałów.

## Zależności
- `field_state`
- `tension_loop`
- `energy_regulator`
- `entropic_modulator`
- `ritual_detector`
- `snapshot_manager`

## Kolejność wykonania (twarda)
1. `tension_loop`
2. `energy_regulator`
3. `entropic_modulator`
4. `ritual_detector`
5. `snapshot_manager` (opcjonalnie)

## Tryby pracy

### INIT
- walidacja parametrów,
- konstrukcja stanu przez `field_state.init`,
- opcjonalny snapshot,
- brak regulacji.

### SINGLE_STEP
- wykonanie pełnej sekwencji modułów,
- opcjonalny snapshot.

### MULTI_STEP
- powtarza SINGLE_STEP N razy,
- snapshot: `each | final | false`.

### TEST_MODE
- wymusza deterministyczność wszystkich modułów,
- brak losowości, brak zależności od czasu,
- snapshoty deterministyczne.

## Kontrakty modułów

### tension_loop
- wejście: `tension_map`,
- wyjście: zaktualizowany `tension_map`,
- deterministyczny w test_mode.

### energy_regulator
- wejście: `energy_level`, `tension_map`,
- wyjście: nowy `energy_level`,
- energia musi pozostać w zakresie `[E_min, E_max]`.

### entropic_modulator
- wejście: `entropy_signature`, `energy_level`,
- wyjście: zaktualizowany `entropy_signature`,
- brak chaotycznych oscylacji w test_mode.

### ritual_detector
- wejście: pełny stan + opcjonalny `EventInput`,
- wyjście: `ritual_flags`,
- zero fałszywych aktywacji w test_mode.

### snapshot_manager
- wejście: pełny stan,
- wyjście: snapshot,
- restore = identyczność bitowa.

## Powiązanie z testami
- `test_init.md` → poprawna inicjalizacja pipeline,
- `test_regulation_step.md` → poprawne wykonanie jednego kroku,
- `test_energy_stability.md` → stabilność energii w pipeline,
- `test_snapshot.md` → poprawna współpraca ze snapshot_manager.

