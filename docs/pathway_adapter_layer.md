# Pathway Adapter Layer v0.1

## Cel
Pathway Adapter Layer umożliwia integrację sygnałów biologicznych
(protein signals, EEG, EMG, sensory drift) z RAMORGA Engine.
Warstwa ta nie konwertuje sygnałów na tokeny — tylko na wkład
rezonansowy zgodny z TensionVector.

Adapter musi tolerować:
- jitter,
- opóźnienia,
- dryf sygnału,
- brak synchronizacji,
- zmienność biologiczną.

---

## Interfejs

### mapBiologicalVariability(input: BioSignal) → ResonanceContribution
Konwertuje sygnał biologiczny na wkład rezonansowy.

**Wejście:**
- `BioSignal`:
  - protein activity
  - EEG band power
  - EMG tension
  - sensory drift
  - HRV / GSR (opcjonalnie)

**Wyjście:**
- `ResonanceContribution`:
  - `intensity: number`
  - `coherence: number`
  - `vector: number[]`
  - `confidence: number`

Zasady:
- brak binaryzacji,
- brak klasyfikacji,
- brak interpretacji semantycznej.

---

### acceptAsynchronous(input: DriftingSignal) → ValidStateUpdate
Przyjmuje sygnały, które nie są zsynchronizowane z wejściem tekstowym.

Mechanizmy:
- tolerancja dryfu czasowego,
- brak wymogu alignowania okien czasowych,
- adaptacyjne wygładzanie.

---

### avoidBinaryThresholds(signal: AffectiveStream) → ContinuousValue
Konwertuje sygnały afektywne na wartości ciągłe.

Zasady:
- brak progów typu „wysoki/niski”,
- brak ostrych cutoffów,
- zachowanie mikrofluktuacji.

---

### fuseWithMeasurement(tension: TensionVector, bio: ResonanceContribution)
Łączy sygnał tekstowy i biologiczny w jeden wkład do pola.

Mechanizm:

fused.intensity = weighted_avg(tension.intensity, bio.intensity)
fused.coherence = min(tension.coherence, bio.coherence)
fused.vector = concat(tension.vector, bio.vector)

---

## Inwarianty Pathway Adapter Layer

- **NO_FORCED_ALIGNMENT**  
  Sygnały biologiczne nie muszą być zsynchronizowane z tekstem.

- **BIO_VARIABILITY_IS_SIGNAL**  
  Zmienność biologiczna jest informacją, nie błędem.

- **NO_BINARY_AFFECT**  
  Brak progów emocjonalnych.

- **NO_SEMANTIC_PROJECTION**  
  Adapter nie interpretuje sygnałów jako emocji, nastroju ani intencji.

- **SOFT_COUPLING_ONLY**  
  Warstwa nie może przejąć kontroli nad polem — tylko wnosi wkład.

---

## Integracja z innymi modułami

- **MeasurementAPI** → otrzymuje wkład bio jako dodatkowy sygnał  
- **FieldAPI** → traktuje bio jako równorzędny wektor napięć  
- **ResonanceState** → aktualizuje napięcia i trace  
- **SymbiosisHealth** → ocenia wpływ bio na stabilność pola  
- **GuardChain** → blokuje eskalację, jeśli sygnał bio jest zbyt intensywny  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

