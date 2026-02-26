# databridge_contract.md
# RAMORGA ENGINE — DataBridge Contract

## 1. Rola
Zapis snapshotu pola po zakończeniu cyklu.

## 2. Interfejs
DataBridge.save(field_state, metadata) → None

## 3. MUST
- działać wyłącznie w CONTINUE
- zapisać pełny snapshot
- zachować deterministyczność

## 4. MUST NOT
- nie modyfikować pola
- nie filtrować treści
- nie optymalizować
- nie predykować

## 5. Inwarianty
- FIELD.STATE.IMMUTABILITY.001
