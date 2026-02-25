# Descent Module v0.1

## Cel
Descent Module odpowiada za przekształcenie ReducedMeaning w formę,
która może zostać bezpiecznie zrenderowana przez Bridge.  
Descent nie generuje treści — on **prowadzi zejście** z pola do języka,
z zachowaniem śladu, niepewności i rezonansu.

Zasada RAMORGA: **Epistemic humility**.

---

## Zakres odpowiedzialności

1. Przekształcenie ReducedMeaning → DescentForm.
2. Zachowanie niepewności i dywergencji.
3. Ochrona przed nadmiernym uproszczeniem.
4. Dodanie hooków rezonansowych dla Bridge.
5. Utrzymanie zgodności z epistemicTrace.

---

## Interfejs

### descend(reduced: ReducedMeaning, state: ResonanceState) → DescentForm
Główna funkcja modułu.

**Wejście:**
- `ReducedMeaning` (lista kandydatów + wagi + uncertainty)
- `ResonanceState` (napięcia, trace, mode)

**Wyjście:**
- `DescentForm`:
  - `core`: uproszczona treść (jeszcze nie render)
  - `alternatives[]`: alternatywne ścieżki znaczeń
  - `uncertainty: number`
  - `traceHooks[]`
  - `resonanceCues[]` (pauzy, miękkie przejścia, otwarte formy)

---

### preserveUncertainty(form: DescentForm)
Zachowuje niepewność w strukturze.

Zasady:
- brak fałszywej pewności,
- brak zamykania znaczeń,
- brak presji na jednoznaczność.

---

### injectResonanceCues(form: DescentForm)
Dodaje sygnały, które Bridge może wykorzystać do łagodnego renderowania.

Przykłady:
- pauzy,
- otwarte zakończenia,
- miękkie przejścia,
- opcjonalne alternatywy.

---

### validateDescent(form: DescentForm) → boolean
Sprawdza zgodność z inwariantami.

Kryteria:
- brak deformacji,
- brak forced interpretation,
- trace continuity,
- uncertainty preserved.

---

## Inwarianty Descent Module

- **UNCERTAINTY_REQUIRED**  
  Każde zejście musi zawierać poziom niepewności.

- **NO_FORCED_INTERPRETATION**  
  Descent nie może wybierać jednej ścieżki.

- **TRACE_CONTINUITY**  
  Ślad epistemiczny musi być zachowany.

- **NO_SEMANTIC_DEFORMATION**  
  Zejście nie może zmieniać intencji użytkownika.

---

## Struktury danych

### DescentForm

{
core: string,
alternatives: string[],
uncertainty: number,
traceHooks: EpistemicTraceEntry[],
resonanceCues: string[]
}

---

## Integracja z innymi modułami

- **Reduction Module** → dostarcza ReducedMeaning  
- **Bridge** → renderuje DescentForm  
- **Integrity Module** → waliduje brak deformacji  
- **SymbiosisHealth** → stroi poziom niepewności  
- **ResonanceState** → aktualizuje trace po renderze  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

