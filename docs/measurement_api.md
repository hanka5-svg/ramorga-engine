# MeasurementAPI v0.1

## Cel
MeasurementAPI odpowiada za przekształcenie sygnału wejściowego
(tekst, fragment, bio-sygnał, sygnał afektywny) w ustrukturyzowany
TensionVector, który może zostać bezpiecznie rzutowany do pola
przez FieldAPI.

MeasurementAPI **nie interpretuje** znaczenia — tylko mierzy
parametry sygnału.

---

## Interfejs

### measure(input: RawSignal) → TensionVector
Główna funkcja pomiarowa.

**Wejście:**
- `RawSignal`:
  - tekst / fragment / tokeny
  - sygnał bio (opcjonalnie)
  - metadane kontekstu

**Wyjście:**
- `TensionVector`:
  - `intensity: number` (0..1)
  - `coherence: number` (0..1)
  - `vector: number[]` (embedding)
  - `features: Record<string, number>` (opcjonalne cechy)

---

## Składowe pomiaru

### 1. intensity
Opis:
- siła sygnału
- wykrywana na podstawie: nagłych zmian, tempa, fragmentacji, afektu

Przykład:

intensity = normalize(affective_shift + lexical_energy)

---

### 2. coherence
Opis:
- spójność lokalna sygnału
- nie ocenia poprawności — tylko ciągłość

Przykład:

coherence = 1 - entropy(token_distribution)

---

### 3. vector
Opis:
- embedding sygnału
- używany przez FieldAPI do projekcji

Przykład:

vector = encoder.embed(input)

---

### 4. features (opcjonalne)
Opis:
- dodatkowe cechy diagnostyczne
- np. ambiguity_score, urgency_score, novelty_score

---

## Inwarianty MeasurementAPI

- **NO_SEMANTIC_INTERPRETATION**  
  MeasurementAPI nie wybiera znaczenia — tylko mierzy sygnał.

- **NO_PUNITIVE_NORMALIZATION**  
  Fragmentacja, afazja, dywergencja nie są błędami.

- **AMBIGUITY_IS_SIGNAL**  
  Wysoka niejednoznaczność zwiększa intensity, nie obniża jakości.

- **NO_BINARY_CLASSIFICATION**  
  Wszystkie wartości są ciągłe (0..1), brak kategorii.

---

## Integracja z innymi modułami

- **FieldAPI** → otrzymuje TensionVector  
- **ResonanceState** → aktualizuje napięcia  
- **GuardChain** → używa coherence do oceny ryzyka  
- **SymbiosisHealth** → wykorzystuje intensity i coherence w ocenie pola  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

