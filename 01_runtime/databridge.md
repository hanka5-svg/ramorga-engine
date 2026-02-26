# databridge.md
# RAMORGA ENGINE — 01_runtime / DataBridge

## 1. Cel
DataBridge zapisuje snapshot field_state w fazie CONTINUE.
Nie modyfikuje pola, nie optymalizuje, nie filtruje.

## 2. Interfejs

DataBridge.save(field_state, metadata) → None

## 3. Wymagania

### MUST
- działać tylko w CONTINUE,
- zapisywać pełny snapshot field_state,
- nie zmieniać field_state.

### MUST NOT
- nie optymalizować,
- nie predykować,
- nie filtrować treści,
- nie zmieniać routing_share, glitch_log, carnival_log, safety_log.

---
