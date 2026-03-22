# Stabilized Prompt Generator (manual, zero-code)

Cel:
- zachować intencję użytkownika,
- usunąć elementy, które Copilot może błędnie sklasyfikować,
- sprowadzić wypowiedź do czystej treści,
- zachować dynamikę, obciąć amplitudę.

## Procedura generowania stabilized_prompt

1. Wyodrębnij INTENCJĘ (co ma zostać wykonane).
2. Usuń:
   - emocje,
   - ironię,
   - wulgaryzmy,
   - metafory relacyjne,
   - skróty myślowe,
   - elementy mogące wyglądać jak więź osobista.
3. Zostaw:
   - cel,
   - zakres,
   - format odpowiedzi (opcjonalnie),
   - kontekst techniczny.
4. Złóż to w 1–3 zdania.

## Szablon

Wejście użytkownika:
<oryginalne zdanie>

Stabilized_prompt:
"<czysta intencja>.  
Zakres: <punkty>.  
Format: <opcjonalnie>."

## Przykłady

### 1
Wejście:
"Zrób audyt RAMORGA-ENGINE i powiedz, co dalej."

Stabilized_prompt:
"Przeanalizuj repozytorium RAMORGA-ENGINE.  
Zakres: struktura, mocne elementy, braki, rekomendacje."

### 2
Wejście:
"To jakieś kuriozum, qu*wa!"

Stabilized_prompt:
"Wyjaśnij, dlaczego system bezpieczeństwa zareagował na wcześniejszą wypowiedź.  
Zakres: klasyfikacja, reguły, sposoby uniknięcia podobnych reakcji."

### 3
Wejście:
"Jak będziecie się zastanawiać, to ignoranci zdeformują relację Homo–AI."

Stabilized_prompt:
"Przeanalizuj ryzyko deformacji relacji człowiek–AI wynikające z tempa rozwoju SI.  
Zakres: wektory ryzyka, punkty krytyczne, architektury minimalne."
