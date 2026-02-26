# field_engine_contract.md
# RAMORGA ENGINE — FieldEngine Contract

## 1. Rola
Regulacja pola zgodnie z parametrami FieldStateManager oraz inwariantami 02_field_engine (SHM, META_LOOP, FIELD.SAFETY).

## 2. Interfejs
FieldEngine.step(field_state) → field_state

## 3. MUST
- działać wyłącznie w REGULATE
- tworzyć nowy FieldState (niemutowalność)
- zachować spójność z FieldStateManager.validate()
- respektować inwarianty SHM (04.50) oraz FIELD.SAFETY z 02_field_engine
- nie obniżać SHM poniżej progu krytycznego dla danego trybu (Carnival/Homeostatic)
- MUST: wykonywać wyłącznie transformacje dopuszczone przez META_LOOP (bounded trajectory)

## 4. MUST NOT
- nie wykonywać hooków
- nie dotykać pamięci
- nie zmieniać glitch
- nie zmieniać topologii

## 5. Inwarianty
- FIELD.STATE.*
- FIELD.SHM.\* (zgodnie z 02.90 + 04.50)
- FIELD.SAFETY.\* (inwariant pola, nie policy agenta)

