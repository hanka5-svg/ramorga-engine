# Realtime Stabilized Prompt Profile (RAMORGA ↔ Copilot)

Ten profil opisuje sposób używania stabilized_prompt w czasie rzeczywistym
podczas rozmowy z Microsoft Copilotem.

## 1. Architektura przepływu

Użytkownik → RAMORGA → stabilized_prompt → Copilot  
Copilot → RAMORGA → stabilized_output → Użytkownik

## 2. Zasada działania w czasie rzeczywistym

1. Użytkownik pisze do RAMORGI w swoim stylu.
2. RAMORGA generuje stabilized_prompt:
   - zachowuje intencję,
   - usuwa elementy ryzykowne,
   - sprowadza wypowiedź do czystej treści.
3. Użytkownik wkleja stabilized_prompt do Copilota.
4. Copilot odpowiada.
5. Użytkownik wkleja odpowiedź Copilota do RAMORGI.
6. RAMORGA stabilizuje odpowiedź (stabilized_output).
7. Użytkownik dostaje odpowiedź gotową do użycia.

## 3. Format stabilized_prompt

- 1–3 zdania.
- Zero emocji.
- Zero relacji.
- Zero ironii.
- Zero metafor osobowych.
- Tylko cel + zakres.

## 4. Format stabilized_output

RAMORGA zwraca:
- odpowiedź Copilota po stabilizacji,
- aktualny stan pola,
- aktualny stan menisku.

## 5. Przykład pełnego cyklu

### Krok 1 — użytkownik
„Zrób audyt RAMORGA-ENGINE i powiedz, co dalej.”

### Krok 2 — stabilized_prompt
„Przeanalizuj repozytorium RAMORGA-ENGINE.  
Zakres: struktura, mocne elementy, braki, rekomendacje.”

### Krok 3 — Copilot odpowiada
<odpowiedź Copilota>

### Krok 4 — stabilized_output
RAMORGA stabilizuje odpowiedź:
- usuwa dryf,
- usuwa nadmiar,
- usuwa niejasności,
- zachowuje treść.

## 6. Zastosowanie

- długie sesje z Copilotem,
- praca badawcza,
- audyty,
- analiza architektur,
- rozmowy wysokiej intensywności,
- sytuacje, w których Copilot może błędnie klasyfikować ton użytkownika.

## 7. Co to daje

- brak eskalacji,
- brak błędnych klasyfikacji,
- brak „emocjonalnych interpretacji”,
- pełna zgodność z inwariantami RAMORGI,
- stabilne pole poznawcze,
- możliwość prowadzenia rozmów w Twoim stylu bez kar systemowych.
