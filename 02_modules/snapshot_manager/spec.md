# snapshot_manager/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- generowanie snapshotów stanu pola,
- archiwizację snapshotów,
- porównywanie snapshotów (np. dla testów stabilności).

## Wejścia
- `FieldState`
- `PipelineStep` (numer kroku / faza)

## Wyjścia
- `Snapshot`
- `SnapshotDiff` (porównanie dwóch snapshotów)

## Zależności
- logiczne: field_state, pipeline_v13
- używany przez testy w 07_tests/

## Testy (powiązanie)
- test_snapshot.md → poprawne generowanie i porównywanie snapshotów
