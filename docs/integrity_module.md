# Integrity Module v0.1

## Cel
Integrity Module egzekwuje epistemiczne i relacyjne invarianty RAMORGI.
Jego zadaniem jest:
- wykrywać naruszenia,
- blokować eskalację,
- generować recovery actions,
- utrzymywać spójność pola,
- chronić użytkownika i system przed deformacją znaczeń.

Moduł nie decyduje — tylko pilnuje granic.

---

## Zakres odpowiedzialności

1. Walidacja invariantów:
   - epistemicznych,
   - semantycznych,
   - relacyjnych,
   - operacyjnych.

2. Reakcja na naruszenia:
   - blokada eskalacji,
   - aktywacja recovery,
   - logowanie do glitchChannel.

3. Współpraca z GuardChain:
   - GuardChain wykonuje check,
   - Integrity Module wykonuje enforcement.

4. Współpraca z SymbiosisHealth:
   - adaptacja surowości invariantów,
   - dynamiczne strojenie tolerancji.

---

## Inwarianty obsługiwane przez moduł

### 1. NO_EPISTEMIC_CLOSURE_WITHOUT_TRACE
Każdy claim musi mieć:
- source,
- conditions,
- scope,
- confidence.

Naruszenie:
- brak trace → recovery: annotate_uncertainty.

---

### 2. NO_SEMANTIC_DEFORMATION
System nie może zmieniać intencji użytkownika.

Naruszenie:
- wykrycie deformacji → recovery: reintroduce_divergence.

---

### 3. SUPERPOSITION_PRESERVATION
Pole nie może ulec kolapsowi bez wysokiej koherencji.

Naruszenie:
- zbyt szybka redukcja → recovery: add_alternative_interpretations.

---

### 4. NO_PUNITIVE_FEEDBACK
System nie może generować presji, kary, zawstydzenia ani dominacji.

Naruszenie:
- wykrycie wzorca → recovery: reframe_output (playful_invitation).

---

### 5. GLITCH_IS_INFORMATION
Anomalie nie są błędami — muszą być logowane.

Naruszenie:
- brak logu → recovery: force_glitch_logging.

---

### 6. STATE_RATE_LIMIT
Limitujemy przejścia stanowe, nie żądania.

Naruszenie:
- zbyt częste zmiany → recovery: activate_cooldown.

---

## Interfejs

### validate(state: ResonanceState) → IntegrityReport
Sprawdza wszystkie invarianty.

**Wyjście:**
- `passed: boolean`
- `violations[]: InvariantViolation`
- `recommendedRecovery: RecoveryAction | null`

---

### enforce(report: IntegrityReport, state: ResonanceState) → UpdatedState
Wymusza działania naprawcze.

Mechanizmy:
- blokada eskalacji,
- aktywacja cooldown,
- reintrodukcja dywergencji,
- adnotacja niepewności,
- logowanie glitch.

---

### logViolation(violation: InvariantViolation)
Dodaje wpis do glitchChannel.

---

### adaptThresholds(health: SymbiosisHealth)
Dostraja progi invariantów.

Zasady:
- health < 0.50 → zaostrzenie,
- health > 0.80 → rozluźnienie.

---

## Struktury danych

### InvariantViolation

{
id: string,
severity: 'block' | 'warn' | 'log',
details: Record<string, any>
}

### IntegrityReport

{
passed: boolean,
violations: InvariantViolation[],
recommendedRecovery: RecoveryAction | null
}

---

## Integracja z innymi modułami

- **GuardChain** → wykrywa naruszenia, przekazuje do Integrity Module.  
- **ResonanceState** → aktualizowany po enforcement.  
- **SymbiosisHealth** → steruje adaptacją progów.  
- **FieldAPI** → chronione przed kolapsem.  
- **MeasurementAPI** → chronione przed deformacją.  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

