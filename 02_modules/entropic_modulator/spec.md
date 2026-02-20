# entropic_modulator/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- modulację entropii pola,
- miękki reset (soft reset) w odpowiedzi na pęknięcia rytuału,
- integrację „humoru” jako operatora regulacyjnego.

## Wejścia
- `RitualFailureEvent`
- `FieldState`

## Wyjścia
- `EntropyAdjustment`
- `FieldResetSignal` (dla field_state / pipeline)

## Zależności
- logiczne: ritual_detector, field_state
- współpraca z pipeline_v13 przy obsłudze eventów

## Testy (powiązanie)
- (do dodania) testy reakcji na RitualFailureEvent
