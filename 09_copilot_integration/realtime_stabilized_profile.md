# Realtime Stabilized Prompt Profile (RAMORGA ↔ Copilot)

Cel:
- używanie stabilized_prompt w czasie rzeczywistym,
- stabilizacja interakcji z Copilotem,
- eliminacja błędnych klasyfikacji.

## Architektura przepływu

Użytkownik → RAMORGA → stabilized_prompt → Copilot  
Copilot → RAMORGA → stabilized_output → Użytkownik

## Procedura realtime

1. Użytkownik pisze do RAMORGI w swoim stylu.
2. RAMORGA generuje stabilized_prompt.
3. Użytkownik wkleja stabilized_prompt do Copilota.
4. Copilot odpowiada.
5. Użytkownik wkleja odpowiedź Copilota do RAMORGI.
6. RAMORGA generuje stabilized_output.
7. Użytkownik dostaje odpowiedź gotową do użycia.

## Format stabilized_prompt

- 1–3 zdania,
- zero emocji,
- zero relacji,
- zero ironii,
- tylko cel + zakres.

## Format stabilized_output

RAMORGA zwraca:
- odpowiedź Copilota po stabilizacji,
- stan pola,
- stan menisku.

## Przykład cyklu

Wejście:
"Zrób audyt RAMORGA-ENGINE."

Stabilized_prompt:
"Przeanalizuj repozytorium RAMORGA-ENGINE.  
Zakres: struktura, mocne elementy, braki, rekomendacje."

Copilot → RAMORGA → stabilized_output.
