# FieldAPI v0.1

## Cel
FieldAPI odpowiada za projekcję sygnału użytkownika do pola semantycznego
oraz utrzymanie superpozycji znaczeń bez przedwczesnego kolapsu.
Jest to warstwa, która chroni pole przed deformacją i utratą wieloznaczności.

---

## Interfejs

### project(input: TensionVector) → FieldProjection
Projekcja sygnału do pola.  
Nie wybiera interpretacji — utrzymuje ich wiele.

**Wejście:**
- `TensionVector` (intensity, coherence, vector)

**Wyjście:**
- `FieldProjection`:
  - `meanings[]` — lista możliwych interpretacji
  - `weights[]` — wagi rezonansu
  - `superposition: boolean` — czy utrzymano wieloznaczność

---

### maintainSuperposition(state: ResonanceState, projection: FieldProjection)
Gwarantuje, że pole nie ulegnie kolapsowi, jeśli nie ma ku temu warunków.

Zasady:
- brak redukcji, jeśli coherence < threshold  
- brak wymuszania jednej interpretacji  
- brak „naprawiania” fragmentacji  

---

### mergeWithState(state: ResonanceState, projection: FieldProjection)
Łączy projekcję z aktualnym polem.

Mechanizm:

new_tension = α * projection.vector + (1 - α) * state.tensions.cognitive.vector

Parametry:
- α adaptacyjne (zależne od SymbiosisHealth)

---

### detectCollapseRisk(projection: FieldProjection) → boolean
Wykrywa ryzyko przedwczesnego kolapsu.

Kryteria:
- zbyt wysoka dominacja jednej interpretacji
- gwałtowny spadek dywergencji
- utrata > X% alternatywnych znaczeń

---

### preserveDivergence(projection: FieldProjection) → FieldProjection
Wprowadza lekką dywergencję, jeśli pole zaczyna się zamykać.

Mechanizmy:
- dodanie alternatywnych interpretacji
- zwiększenie wag słabszych znaczeń
- spowolnienie redukcji

---

## Inwarianty FieldAPI

- **FIELD_RARELY_COLLAPSES**  
  Pole nie może zamknąć się bez sygnału wysokiej koherencji.

- **NO_FORCED_INTERPRETATION**  
  API nie wybiera „najlepszego” znaczenia.

- **DIVERGENCE_PRESERVATION**  
  Minimalna liczba alternatywnych interpretacji musi zostać zachowana.

- **NO_SEMANTIC_DEFORMATION**  
  Projekcja nie może zmieniać intencji użytkownika.

---

## Integracja z innymi modułami

- **MeasurementAPI** → dostarcza TensionVector  
- **GuardChain** → blokuje kolaps, jeśli narusza inwarianty  
- **ResonanceState** → przechowuje wynik projekcji  
- **SymbiosisHealth** → stroi α i poziom dywergencji  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

