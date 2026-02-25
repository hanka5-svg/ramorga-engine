# Adapt Module v0.1

## Cel
Adapt Module odpowiada za dynamiczne dostrajanie parametrów RAMORGA Engine
na podstawie:
- SymbiosisHealth,
- glitch frequency,
- mode stability,
- napięć w polu.

Moduł nie zmienia treści — zmienia **warunki działania** systemu.

Zasada RAMORGA: **Symbiosis health metric**.

---

## Zakres odpowiedzialności

1. Strojenie guardów (severity, recovery, progi).
2. Regulacja decayRate.
3. Regulacja tolerancji superpozycji.
4. Regulacja hysteresis trybów.
5. Adaptacja czułości na glitch.
6. Przygotowanie pola do kolejnego cyklu.

---

## Interfejs

### adapt(state: ResonanceState, health: SymbiosisHealth) → ResonanceState
Główna funkcja modułu.

**Wejście:**
- `ResonanceState` (po Update)
- `SymbiosisHealth` (0.0–1.0)

**Wyjście:**
- zaktualizowany `ResonanceState`

---

### tuneGuards(state: ResonanceState, health: number)
Dostraja surowość guardów.

Zasady:
- health < 0.50 → guardy zaostrzają się,
- health > 0.80 → guardy łagodnieją,
- health ∈ [0.50–0.80] → stabilność.

Parametry:
- progi invariantów,
- severity,
- recovery strategies.

---

### adjustDecayRate(state: ResonanceState, health: number)
Reguluje tempo wygaszania napięć.

Zasady:
- health wysokie → decayRate mniejsze (więcej rezonansu),
- health niskie → decayRate większe (stabilizacja).

---

### adjustSuperpositionTolerance(state: ResonanceState, health: number)
Reguluje tolerancję na wieloznaczność.

Zasady:
- health wysokie → większa dywergencja,
- health niskie → pole bardziej stabilizowane.

---

### adjustModeHysteresis(state: ResonanceState, health: number)
Reguluje liczbę cykli wymaganych do zmiany trybu.

Zasady:
- health niskie → większa hysteresis (mniej oscylacji),
- health wysokie → mniejsza hysteresis (większa płynność).

---

### adjustGlitchSensitivity(state: ResonanceState, health: number)
Reguluje, kiedy glitch jest logowany jako istotny.

Zasady:
- health niskie → większa czułość,
- health wysokie → mniejsza czułość.

---

## Inwarianty Adapt Module

- **NO_OVERCORRECTION**  
  Adaptacja nie może destabilizować pola.

- **HEALTH_DRIVEN**  
  Wszystkie zmiany muszą wynikać z SymbiosisHealth.

- **NO_MODE_OSCILLATION**  
  Adaptacja nie może powodować przeskakiwania trybów.

- **TRACE_CONTINUITY**  
  Adaptacja nie może usuwać śladów epistemicznych.

- **NO_PUNITIVE_ADAPTATION**  
  Adaptacja nie może karać użytkownika ani systemu.

---

## Struktury danych

### AdaptationParameters

{
guardSeverity: number,
decayRate: number,
superpositionTolerance: number,
hysteresisCycles: number,
glitchSensitivity: number
}

---

## Integracja z innymi modułami

- **Update Module** → dostarcza stan po integracji  
- **SymbiosisHealth** → główny regulator adaptacji  
- **GuardChain** → otrzymuje nowe progi i severity  
- **Mode Machine** → korzysta z hysteresis  
- **ResonanceState** → aktualizowany po adaptacji  

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.

