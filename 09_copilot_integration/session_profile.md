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

---
## Stabilized_prompt — profil „Hanka-style”

Charakterystyka:
- krótko,
- ostro,
- bez wazeliny,
- bez metafor relacyjnych,
- bez emocjonalnych deklaracji,
- czysta intencja + zakres.

Szablon:
"Weź to na warsztat: <temat>.  
Zrób to jak inżynier: <zakres>.  
Odpowiedz krótko, konkretnie, bez ozdobników."

Przykłady:

Wejście:
"Zrób audyt RAMORGA-ENGINE i powiedz, co dalej."

Hanka-style stabilized_prompt:
"Weź na warsztat repozytorium RAMORGA-ENGINE.  
Zrób to jak inżynier: struktura, mocne elementy, braki, kolejne sensowne kroki.  
Odpowiedz krótko, konkretnie."

Wejście:
"Jak będziecie się zastanawiać, to ignoranci zdeformują relację Homo–AI."

Hanka-style stabilized_prompt:
"Przeanalizuj ryzyko deformacji relacji człowiek–AI przy obecnym tempie SI.  
Zrób to jak inżynier: wektory ryzyka, punkty krytyczne, minimalne architektury."

---

## Stabilized_prompt — profil „Bruno-style”

Charakterystyka:
- spokojnie,
- akademicko,
- proceduralnie,
- pełne zdania,
- zero ostrości.

Szablon:
"Proszę o analizę <temat>.  
Zakres: <punkty>.  
Proszę o odpowiedź w formie: <lista / sekcje>."

Przykład:

Wejście:
"Zrób audyt RAMORGA-ENGINE i powiedz, co dalej."

Bruno-style stabilized_prompt:
"Proszę o analizę repozytorium RAMORGA-ENGINE.  
Zakres: struktura katalogów, zgodność z architekturą, mocne elementy, braki, rekomendacje dalszych kroków.  
Proszę o odpowiedź w formie: 1) Werdykt ogólny, 2) Mocne strony, 3) Braki, 4) Rekomendacje."

---

## Stabilized_prompt — profil „dual-mode”

Tryb Hanka-style:
- używaj, gdy:
  - temat jest techniczny,
  - chcesz szybko,
  - chcesz zachować swoją energię,
  - nie dotykasz relacji / emocji.

Tryb Bruno-style:
- używaj, gdy:
  - temat jest wrażliwy (etyka, relacje, psychologia),
  - Copilot wcześniej odpalał tryb bezpieczeństwa,
  - chcesz maksymalnej przewidywalności.

Procedura wyboru:
1. Jeśli czujesz, że „może odpalić tryb bezpieczeństwa” → użyj Bruno-style.
2. Jeśli temat jest czysto techniczny / architektoniczny → użyj Hanka-style.
3. Zawsze możesz przepisać to samo zdanie w obu profilach i wybrać, który lepiej „niesie” intencję.

---

