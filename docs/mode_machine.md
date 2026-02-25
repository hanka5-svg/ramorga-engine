# Mode Machine v0.1

## Cel
Mode Machine zarządza trybami operacyjnymi RAMORGA Engine:
- **CARNIVAL** — lekkość, zaproszenie, dywergencja,
- **HOMEOSTATIC** — stabilizacja, spowolnienie, regulacja,
- **DECISION** — precyzja, zakres, brak dominacji.

Tryby nie są reakcją na treść — są reakcją na **stan pola**.

Zasada RAMORGA: *Carnival before control* + *State rate limit*.

---

## Zakres odpowiedzialności

1. Ustalanie aktualnego trybu na podstawie:
   - napięć,
   - glitch frequency,
   - SymbiosisHealth,
   - modeStabilityCounter.

2. Zapobieganie oscylacjom między trybami (hysteresis).

3. Wymuszanie minimalnej stabilności przed zmianą trybu.

4. Przekazywanie trybu do Bridge, Descent i Adapt.

---

## Interfejs

### evaluateMode(state: ResonanceState, health: SymbiosisHealth) → Mode
Główna funkcja modułu.

Zasady:
- tryb zmienia się tylko, jeśli:
  - health przekracza próg,
  - stateStabilityCounter ≥ hysteresisCycles.

---

### shouldEnterCarnival(state, health) → boolean
Warunki wejścia w CARNIVAL:

- health ≥ 0.75  
- niska intensywność safety-tension  
- brak świeżych glitch o wysokiej wadze  
- superpositionPreserved == true  

---

### shouldEnterHomeostatic(state, health) → boolean
Warunki wejścia w HOMEOSTATIC:

- health < 0.50  
- glitchFrequency wysokie  
- napięcia safety rosną  
- decayRate wymaga zwiększenia  

---

### shouldEnterDecision(state, health) → boolean
Warunki wejścia w DECISION:

- health stabilne (0.60–0.80)  
- brak świeżych anomalii  
- wysoka koherencja  
- użytkownik sygnalizuje potrzebę precyzji (bez presji)  

---

### applyHysteresis(state: ResonanceState, nextMode: Mode)
Zapobiega oscylacjom.

Zasady:
- zmiana trybu wymaga N stabilnych cykli,
- N zależy od health:
  - health niskie → N większe,
  - health wysokie → N mniejsze.

---

### updateMode(state: ResonanceState, nextMode: Mode)
Aktualizuje tryb i resetuje licznik stabilności.

---

## Inwarianty Mode Machine

- **NO_MODE_OSCILLATION**  
  Tryb nie może przeskakiwać między CARNIVAL ↔ HOMEOSTATIC.

- **CARNIVAL_BEFORE_CONTROL**  
  Jeśli oba tryby są możliwe → wybierz CARNIVAL.

- **HEALTH_DRIVEN**  
  Tryb wynika z SymbiosisHealth, nie z treści.

- **NO_PUNITIVE_MODE_SWITCH**  
  Tryb nie może być reakcją na „błąd użytkownika”.

- **TRACE_CONTINUITY**  
  Zmiana trybu nie może usuwać śladów epistemicznych.

---

## Struktury danych

### Mode

'CARNIVAL' | 'HOMEOSTATIC' | 'DECISION'

### ModeTransition

{
from: Mode,
to: Mode,
reason: string,
timestamp: number
}

---

## Integracja z innymi modułami

- **Adapt Module** → dostarcza hysteresisCycles  
- **Update Module** → aktualizuje modeStabilityCounter  
- **Bridge Module** → dostosowuje ton do trybu  
- **Integrity Module** → waliduje brak naruszeń  
- **SymbiosisHealth** → główny regulator trybu  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.
