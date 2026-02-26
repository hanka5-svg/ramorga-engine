# field_state_manager_contract.md
# RAMORGA ENGINE — FieldStateManager Contract

## 1. Rola
Tworzenie i walidacja FieldState zgodnie z meta‑inwariantami pola.

## 2. Interfejs
init(params) → FieldState  
validate(state) → None  

## 3. MUST
- tworzyć stan zgodny z inwariantami
- egzekwować wszystkie FIELD.STATE.*
- zachować deterministyczność

## 4. MUST NOT
- nie generować losowości
- nie optymalizować
- nie filtrować treści

## 5. Inwarianty
- FIELD.STATE.ENERGY.001  
- FIELD.STATE.TENSION.001  
- FIELD.STATE.ENTROPY.001  
- FIELD.STATE.RITUAL.001  
- FIELD.STATE.IMMUTABILITY.001  
