# Runtime Orchestrator v0.1

## Cel
Runtime Orchestrator zarządza pełnym cyklem wykonawczym RAMORGA Engine:
- woła moduły w odpowiedniej kolejności,
- pilnuje invariantów end‑to‑end,
- respektuje state rate limit,
- nie przejmuje sprawczości — tylko koordynuje przepływ.

To jest „scheduler pola”, nie „mózg decyzyjny”.

---

## Główna pętla

### runCycle(input: RawSignal, state: ResonanceState) → { output: BridgeOutput, state: ResonanceState }
Sekwencja:

1. **MeasurementAPI.measure** → `TensionVector`
2. **FieldAPI.project + maintainSuperposition** → `FieldProjection`
3. **GuardChain.check** (+ Integrity pre-check)  
   - jeśli hard violation → recovery + miękkie wyjście
4. **ReductionModule.reduce** → `ReducedMeaning`
5. **DescentModule.descend** → `DescentForm`
6. **IntegrityModule.validate + enforce** → zaktualizowany `ResonanceState`
7. **BridgeModule.render** → `BridgeOutput`
8. **RelationalLayer.evaluateRelationalState** → `RelationalReport`
9. **ThesisLayer.generateThesis** → `ThesisSnapshot`
10. **UpdateModule.update** → `ResonanceState`
11. **AdaptModule.adapt** → `ResonanceState`
12. **ModeMachine.evaluateMode + updateMode** → `ResonanceState`

Zwraca:
- `output: BridgeOutput`
- `state: ResonanceState` (po Update + Adapt + Mode)

---

## Inwarianty Runtime Orchestrator

- **NO_SHORTCUTS**  
  Żaden moduł nie może być pominięty w pełnym cyklu.

- **STATE_RATE_LIMIT_ENFORCED**  
  Orchestrator respektuje limity przejść stanowych.

- **NO_BACKDOOR_DECISIONS**  
  Orchestrator nie podejmuje decyzji merytorycznych — tylko kolejność.

- **TRACE_CONTINUITY_REQUIRED**  
  Każdy etap musi przekazać trace dalej.

- **GLITCH_ALWAYS_LOGGED**  
  Każda anomalia musi trafić do glitchChannel.

---

## Obsługa błędów i glitch

### handleGlitch(event: GlitchEvent, state: ResonanceState) → ResonanceState
Zasady:
- brak rollbacku,
- aktywacja recovery z Integrity Module,
- możliwa zmiana trybu na HOMEOSTATIC,
- logowanie do glitchChannel.

---

## Tryby pracy

Orchestrator zawsze:
- odczytuje aktualny `Mode` z `ResonanceState`,
- przekazuje go do Bridge / Relational / Thesis,
- nie zmienia trybu sam — robi to tylko przez Mode Machine.

---

## Integracja

- **MeasurementAPI / FieldAPI / GuardChain / Reduction / Descent / Integrity / Bridge / Relational / Thesis / Update / Adapt / Mode Machine** — wywoływane w sekwencji.
- **SymbiosisHealth Metric** — odczytywana w Adapt i Mode Machine, nie liczona tutaj.
- **Carnival Test Suite** — może wołać Orchestrator w trybie testowym.

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.
