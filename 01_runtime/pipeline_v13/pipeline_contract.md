# pipeline_contract.md
# RAMORGA ENGINE — PipelineV13 Contract

## 1. Rola
Deterministyczna trajektoria wykonawcza pola.

## 2. Interfejs
run(mode, state, params, steps, snapshot, event_input) → (FieldState, Optional[Snapshot])

## 3. MUST
- wykonywać moduły w kolejności:
  tension → energy → entropy → ritual → SAVE
- tworzyć nowy FieldState na każdym kroku
- zachować deterministyczność
- wywołać DataBridge w CONTINUE

## 4. MUST NOT
- nie wykonywać hooków runtime
- nie dotykać pamięci
- nie zmieniać glitch
- nie zmieniać topologii

## 5. Inwarianty
- FIELD.STATE.*
- FIELD.TOPOLOGY.001
- FIELD.GLITCH.001
