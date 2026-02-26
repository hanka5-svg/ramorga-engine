# meniscus_contract.md
# RAMORGA ENGINE — MeniscusEngine Contract

## 1. Rola
Homeostatyczny regulator pomiędzy pipeline_v13 a FieldEngine.

## 2. Interfejs
MeniscusEngine.step(input_payload, field_state, metadata) → field_state

## 3. MUST
- działać wyłącznie w REGULATE
- egzekwować Carnival Gate
- przepuszczać glitch bez zmian
- zachować routing_share
- zwracać niemodyfikowany field_state

## 4. MUST NOT
- nie optymalizować
- nie predykować
- nie filtrować treści
- nie zmieniać topologii
- nie dotykać pamięci

## 5. Inwarianty
- FIELD.GLITCH.001
- FIELD.TOPOLOGY.001
- FIELD.RELATION.001
