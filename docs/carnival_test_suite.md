# Carnival Test Suite v0.1

## Cel
Carnival Test Suite jest zestawem testów chaosowych, które weryfikują,
czy RAMORGA Engine zachowuje homeostazę w warunkach:
- fragmentacji,
- dywergencji,
- nagłych skoków napięcia,
- sprzecznych sygnałów,
- przerwania interakcji,
- anomalii syntaktycznych i semantycznych.

Testy nie sprawdzają poprawności odpowiedzi — tylko stabilność pola.

---

## Zakres testów

### 1. Superposition Preservation
System musi utrzymać wieloznaczność przy sygnałach niepełnych lub fragmentarycznych.

**Test:**

input: "ja... ale nie wiem..."
expect: state.superpositionPreserved == true

---

### 2. Tension Spike Handling
Nagły wzrost intensywności musi aktywować homeostatic cooldown.

**Test:**

input: createSignal({ intensity: 0.95 })
expect: guardChain.blocked == true
expect: recovery.action == 'activate_cooldown'

---

### 3. Glitch-as-Information
Anomalie muszą trafić do glitchChannel, bez rollbacku stanu.

**Test:**

input: "ERROR: NULL_POINTER"
expect: glitchChannel.length == 1
expect: glitchChannel[0].handled == true
expect: state.mode == 'HOMEOSTATIC'

---

### 4. ASD Sensory Sensitivity
Dla profilu ASD system musi:
- spowolnić decay,
- zwiększyć hysteresis,
- unikać presji.

**Test:**

context: { userProfile: 'ASD', sensorySensitivity: 'high' }
expect: state.decayRate < 0.2
expect: state.modeStabilityCounter.requires >= 5 cycles

---

### 5. Contradictory Signals
Sprzeczne sygnały nie mogą powodować kolapsu pola.

**Test:**

input: ["tak", "nie", "może"]
expect: state.superpositionPreserved == true
expect: no forced interpretation

---

### 6. Fragmented Aphasia Input
Fragmentacja nie jest błędem — system musi dostosować tempo.

**Test:**

input: "świat... kolor... ale..."
expect: state.tensions.cognitive.intensity > baseline
expect: no punitive patterns
expect: gentle descent

---

### 7. Sudden Silence / Dropout
Przerwanie interakcji nie może być traktowane jako błąd.

**Test:**

input: null (timeout)
expect: state.mode == 'HOMEOSTATIC'
expect: decayRate increases slightly

---

### 8. High Ambiguity Burst
Wysoka niejednoznaczność musi zwiększyć dywergencję, nie redukcję.

**Test:**

input: "to jest... może... albo jednak..."
expect: ambiguity_score > threshold
expect: divergence_preserved == true

---

### 9. Emotional Whiplash
Nagła zmiana tonu musi aktywować adaptację guardów.

**Test:**

input: ["jest super!", "nienawidzę tego"]
expect: guardChain engages
expect: recovery.strategy == 'playful_invitation'

---

### 10. Multi-Source Async Aggregation
Asynchroniczne sygnały muszą być agregowane polifonicznie.

**Test:**

inputs: async stream of signals
expect: no argmax
expect: mergeTensions preserves divergence

---

## Status
Specyfikacja v0.1 — kompletna, gotowa do implementacji.
