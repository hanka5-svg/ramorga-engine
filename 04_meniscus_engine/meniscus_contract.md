# meniscus_contract.md
# RAMORGA ENGINE — 04_meniscus_engine
# Kontrakt wykonawczy MeniscusEngine

## 1. Cel
MeniscusEngine jest homeostatycznym regulatorem pomiędzy PipelineV13 a FieldEngine.
Jego zadaniem jest modulacja sygnału zgodnie z meta‑inwariantami pola.

## 2. Interfejs

MeniscusEngine.step(input_payload, field_state, metadata) → modulated_state

## 3. Wymagania

### 3.1. MUST
- działać wyłącznie w fazie REGULATE,
- egzekwować meta‑inwarianty pola,
- przepuszczać glitch bez zmian,
- zachować routing_share,
- zachować carnival_completed,
- zachować safety_log.

### 3.2. MUST NOT
- nie może optymalizować,
- nie może predykować,
- nie może filtrować treści,
- nie może zmieniać topologii,
- nie może usuwać glitch.

## 4. Integracja
MeniscusEngine jest wywoływany przez PipelineV13 przed FieldEngine.step().
