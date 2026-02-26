# pipeline_v13_meniscus_integration.md
# Integracja MeniscusEngine z PipelineV13 i FieldEngine

## 1. Cel
Dokument definiuje integrację MeniscusEngine w fazie REGULATE pętli RAMORGI.

## 2. Przepływ wykonania

PipelineV13.step():

OBSERVE
(hooki runtime)

PIPELINE LOGIC
(aktualizacja field_state)

REGULATE
field_state = MeniscusEngine.step(input_payload, field_state, metadata)
field_state = FieldEngine.step(field_state)

CONTINUE
(hooki runtime)

## 3. Wymagania integracyjne

### 3.1. MUST
- MeniscusEngine wywoływany przed FieldEngine.
- MeniscusEngine działa tylko w REGULATE.
- FieldEngine działa tylko po MeniscusEngine.
- PipelineV13 przerywa wykonanie przy CarnivalGateViolation.
- PipelineV13 nie modyfikuje glitch, topologii ani pamięci w REGULATE.

### 3.2. MUST NOT
- brak hooków w REGULATE,
- brak optymalizacji,
- brak predykcji,
- brak filtracji treści.

## 4. Interfejs

MeniscusEngine.step(input_payload, field_state, metadata) → field_state
FieldEngine.step(field_state) → field_state

## 5. Status
Integracja wymagana dla pełnej zgodności z meta‑inwariantami pola.

