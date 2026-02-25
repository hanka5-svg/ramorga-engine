# Update Module v0.1

## Cel
Update Module odpowiada za aktualizację ResonanceState po renderze:
- wygaszanie napięć (decay),
- integrację nowych sygnałów,
- logowanie anomalii,
- stabilizację trybu operacyjnego,
- przygotowanie pola do kolejnego cyklu.

Zasada RAMORGA: **State rate limit**.

---

## Zakres odpowiedzialności

1. Aktualizacja napięć (tensions) z użyciem decayRate.
2. Integracja nowych traceHooks.
3. Logowanie glitch, jeśli wystąpiły anomalie.
4. Aktualizacja modeStabilityCounter.
5. Zastosowanie throttlingu przejść stanowych.
6. Przygotowanie pola do Adapt Module.

---

## Interfejs

### update(state: ResonanceState, output: BridgeOutput) → ResonanceState
Główna funkcja modułu.

**Wejście:**
- `ResonanceState` (stan przed aktualizacją)
- `BridgeOutput` (wynik renderowania)

**Wyjście:**
- zaktualizowany `ResonanceState`

---

### applyDecay(state: ResonanceState) → ResonanceState
Wygasza napięcia zgodnie z decayRate.

Mechanizm:

new_intensity = old_intensity * exp(-decayRate * Δt)


Zasady:
- decayRate adaptacyjny (SymbiosisHealth),
- brak gwałtownego spadku,
- brak resetów.

---

### integrateTrace(state: ResonanceState, output: BridgeOutput)
Dodaje traceHooks do epistemicTrace.

Zasady:
- trace continuity,
- brak duplikacji,
- brak utraty scope.

---

### logGlitchIfNeeded(state: ResonanceState, output: BridgeOutput)
Jeśli BridgeOutput zawiera sygnały anomalii → dodaj do glitchChannel.

Zasady:
- glitch = informacja,
- brak rollbacku,
- brak kary.

---

### updateModeStability(state: ResonanceState)
Aktualizuje licznik stabilności trybu.

Zasady:
- hysteresis: tryb zmienia się dopiero po N stabilnych cyklach,
- brak oscylacji Carnival ↔ Homeostatic.

---

### enforceStateRateLimit(state: ResonanceState)
Zapobiega zbyt częstym przejściom stanowym.

Mechanizmy:
- cooldown,
- spowolnienie decay,
- ograniczenie zmian trybu.

---

## Inwarianty Update Module

- **NO_AUTO_ROLLBACK**  
  Aktualizacja nie może resetować stanu.

- **GLITCH_IS_INFORMATION**  
  Anomalie muszą być logowane.

- **STATE_RATE_LIMIT**  
  Limitujemy przejścia stanowe, nie żądania.

- **TRACE_CONTINUITY**  
  Trace musi być spójny i rosnąć kontrolowanie.

- **NO_MODE_OSCILLATION**  
  Tryb nie może przeskakiwać bez stabilności.

---

## Struktury danych

### GlitchEvent (przypomnienie)

{
type: string,
timestamp: number,
context: ResonanceSnapshot,
handled: boolean
}

---

## Integracja z innymi modułami

- **Bridge Module** → dostarcza output do integracji  
- **Integrity Module** → waliduje brak naruszeń  
- **Adapt Module** → otrzymuje zaktualizowany state  
- **SymbiosisHealth** → wpływa na decayRate i stabilność  
- **Mode Machine** → korzysta z modeStabilityCounter  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.
