# Session Profile: RAMORGA ↔ Copilot

## 1. Inicjalizacja sesji

RAMORGA tworzy:
- FIELD_STATE
- MENISCUS_STATE
- SESSION_CONTEXT

## 2. Format komunikacji

Użytkownik → RAMORGA:
{
"input": "tekst użytkownika",
"session_id": "dowolny identyfikator"
}


RAMORGA → Copilot:

<przetworzony prompt>

Copilot → RAMORGA:

<odpowiedź Copilota>

RAMORGA → Użytkownik:
{

"output": "odpowiedź po stabilizacji",
"field_state": {...},
"meniscus_state": {...}

## 3. Zasady sesji

- brak pamięci długoterminowej,
- brak agentowości,
- brak celów,
- pełna homeostaza,
- każda odpowiedź przechodzi przez menisk,
- każda odpowiedź aktualizuje pole.

}
