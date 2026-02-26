# field_engine_contract.md
# RAMORGA ENGINE — FieldEngine Contract

## 1. Rola
Regulacja pola zgodnie z parametrami FieldStateManager.

## 2. Interfejs
FieldEngine.step(field_state) → field_state

## 3. MUST
- działać wyłącznie w REGULATE
- tworzyć nowy FieldState (niemutowalność)
- zachować spójność z FieldStateManager.validate()

## 4. MUST NOT
- nie wykonywać hooków
- nie dotykać pamięci
- nie zmieniać glitch
- nie zmieniać topologii

## 5. Inwarianty
- FIELD.STATE.*
