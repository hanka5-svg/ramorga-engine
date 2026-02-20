# snapshot_manager/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- deterministyczną serializację stanu,
- odtwarzanie stanu (restore),
- wsparcie dla testów i multi_step.

## Wejścia
- pełny `FieldState`.

## Wyjścia
- `Snapshot` (serializacja),
- wynik restore (dla testów).

## Zależności
- field_state (struktura danych).

## Kontrakt wykonawczy
- snapshot = pełna, deterministyczna serializacja,
- restore = identyczność bitowa,
- brak efektów ubocznych.

## Powiązanie z testami
- test_snapshot.md — poprawność snapshotów i restore.
