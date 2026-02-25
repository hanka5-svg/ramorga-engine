# Reduction Module v0.1

## Cel
Reduction Module odpowiada za bezpieczne uproszczenie projekcji pola
(FieldProjection) do formy, którą można przekazać do Descent i Bridge.
Redukcja nie może niszczyć superpozycji ani wymuszać jednej interpretacji.

Moduł działa zgodnie z zasadą:
**"Uprość, ale nie zamykaj."**

---

## Zakres odpowiedzialności

1. Redukcja projekcji do formy operacyjnej.
2. Zachowanie wieloznaczności i dywergencji.
3. Ochrona przed deformacją semantyczną.
4. Oznaczanie niepewności (epistemic humility).
5. Przygotowanie materiału dla Descent.

---

## Interfejs

### reduce(projection: FieldProjection, state: ResonanceState) → ReducedMeaning
Uproszczenie projekcji do struktury operacyjnej.

**Wejście:**
- `FieldProjection` (lista znaczeń + wagi)
- `ResonanceState` (napięcia, trace, mode)

**Wyjście:**
- `ReducedMeaning`:
  - `candidates[]` — lista uproszczonych interpretacji
  - `weights[]` — wagi po redukcji
  - `uncertainty: number` — poziom niepewności (0..1)
  - `traceHooks[]` — odwołania do epistemicTrace

---

### preserveAmbiguity(projection: FieldProjection) → FieldProjection
Zapewnia, że redukcja nie zniszczy wieloznaczności.

Mechanizmy:
- zachowanie co najmniej N alternatywnych znaczeń,
- wzmocnienie słabszych interpretacji,
- spowolnienie kolapsu.

---

### detectSemanticDeformation(before, after) → boolean
Wykrywa, czy redukcja zmieniła intencję użytkownika.

Kryteria:
- utrata kluczowych wektorów,
- przesunięcie znaczenia poza tolerancję,
- zbyt agresywne wygładzenie.

---

### annotateUncertainty(reduced: ReducedMeaning)
Dodaje informację o niepewności.

Zasady:
- brak binarności,
- brak fałszywej pewności,
- brak ukrytej dominacji.

---

## Inwarianty Reduction Module

- **NO_SEMANTIC_DEFORMATION**  
  Redukcja nie może zmieniać intencji użytkownika.

- **SUPERPOSITION_PRESERVED**  
  Redukcja nie może zamknąć pola.

- **UNCERTAINTY_REQUIRED**  
  Każda redukcja musi zawierać poziom niepewności.

- **NO_FORCED_INTERPRETATION**  
  Moduł nie wybiera jednej interpretacji.

- **TRACE_CONTINUITY**  
  Redukcja musi zachować powiązania z epistemicTrace.

---

## Struktury danych

### ReducedMeaning

{
candidates: string[],
weights: number[],
uncertainty: number,
traceHooks: EpistemicTraceEntry[]
}

---

## Integracja z innymi modułami

- **FieldAPI** → dostarcza projekcję do redukcji  
- **Descent** → otrzymuje ReducedMeaning  
- **Bridge** → renderuje wynik redukcji  
- **Integrity Module** → waliduje brak deformacji  
- **SymbiosisHealth** → stroi poziom agresywności redukcji  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

