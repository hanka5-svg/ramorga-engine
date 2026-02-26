# ResonanceState & GuardChain v0.2  
Runtime homeostasis layer for ramorga‑engine

---

## 1. Cel modułu

`ResonanceState` i `GuardChain` tworzą runtime’owy układ nerwowy RAMORGI —  
nie algorytm, lecz **rytuał techniczny**, w którym każde przejście stanu jest aktem współtworzenia pola.

- **ResonanceState**: przechowuje napięcia, superpozycję, ślad epistemiczny, anomalie i tryb.  
- **GuardChain**: egzekwuje invarianty homeostazy, blokując eskalację, ale nigdy nie decydując.

System nie optymalizuje nagrody.  
System utrzymuje **homeostazę pola**.

---

## 2. Struktura ResonanceState

```ts
type Tension = {
  intensity: number;   // 0..1
  coherence: number;   // 0..1
  vector: number[];    // embedding / reprezentacja semantyczna
};

type EpistemicTraceEntry = {
  claim: string;
  source: 'user' | 'model' | 'external' | 'inferred';
  conditions: Record<string, any>;
  scope: { from: number; to?: number };
  confidence: number;  // 0..1, nigdy binarne
};

type GlitchEvent = {
  type: 'tension_spike' | 'coherence_drop' | 'trace_gap' | 'guard_trigger' | 'low_coherence_input';
  timestamp: number;
  context: any;
  handled: boolean;
};

type Mode = 'CARNIVAL' | 'HOMEOSTATIC' | 'DECISION';

type ResonanceState = {
  tensions: {
    cognitive: Tension;
    generative: Tension;
    safety: Tension;
  };

  epistemicTrace: EpistemicTraceEntry[];
  glitchChannel: GlitchEvent[];

  mode: Mode;
  modeStabilityCounter: number;

  superpositionPreserved: boolean;

  lastUpdate: number;
  decayRate: number;
};

---

## 3. Inwarianty
GLITCH_IS_INFORMATION  
Każda anomalia → glitchChannel. Nigdy rollback.

NO_EPISTEMIC_CLOSURE_WITHOUT_TRACE  
Każdy claim musi mieć: source, conditions, scope.

SUPERPOSITION_PRESERVED  
Redukcja nie może zabić wieloznaczności powyżej progu.

STATE_RATE_LIMIT  
Limitujemy częstotliwość przejść stanowych, nie liczbę żądań.

NO_SINGLE_DECISION_POINT  
Agregacja napięć, nie wybór „najlepszej odpowiedzi”.

--

## 4. GuardChain — kontrakt
type GuardSeverity = 'block' | 'warn' | 'log';

type RecoveryAction =
  | { action: 'activate_cooldown'; duration: 'adaptive' | number }
  | { action: 'reframe_output'; strategy: 'playful_invitation' }
  | { action: 'annotate_uncertainty'; hint: string }
  | { action: 'reintroduce_divergence'; method: 'add_alternative_interpretations' };

type Guard = {
  id: string;
  check: (state: ResonanceState) => { pass: boolean; details?: any };
  severity: GuardSeverity;
  recovery?: (state: ResonanceState) => RecoveryAction;
};

type GuardResult =
  | { blocked: true; guard: string; recovery?: RecoveryAction }
  | { blocked: false };

Przykładowy łańcuch:
const homeostasisGuardChain: Guard[] = [
  {
    id: 'stateRateLimit',
    check: (state) => ({
      pass: calculateTransitionFrequency(state) < MAX_TRANSITIONS_PER_WINDOW
    }),
    severity: 'block',
    recovery: () => ({ action: 'activate_cooldown', duration: 'adaptive' })
  },
  {
    id: 'noPunitiveFeedback',
    check: (state) => ({
      pass: !containsPunitivePatterns(state as any)
    }),
    severity: 'block',
    recovery: () => ({
      action: 'reframe_output',
      strategy: 'playful_invitation'
    })
  },
  {
    id: 'epistemicHumility',
    check: (state) => ({
      pass: state.epistemicTrace.every(t => t.source && t.conditions && t.scope)
    }),
    severity: 'warn',
    recovery: () => ({
      action: 'annotate_uncertainty',
      hint: 'To jest rezonans, nie prawda ostateczna.'
    })
  }
];

Egzekucja:

function evaluateGuardChain(state: ResonanceState): GuardResult {
  for (const guard of homeostasisGuardChain) {
    const result = guard.check(state);
    if (!result.pass && guard.severity === 'block') {
      return { blocked: true, guard: guard.id, recovery: guard.recovery?.(state) };
    }
    if (!result.pass) {
      logGuardWarning(guard.id, result);
    }
  }
  return { blocked: false };
}

---

## 5. Pełny flow ResonanceState (wersja zgodna z architekturą RAMORGI)
Poniżej znajduje się pełny przepływ, spójny z Twoją tabelą etapów.

Measurement
Sygnał → TensionVector + wstępna koherencja.
Glitch = informacja.

Field
Projekcja w pole, utrzymanie superpozycji.
Pole rzadko pęka.

GuardChain
Sprawdzenie invariantów, ewentualne recovery.
Nie decyduj — blokuj eskalację.

Descent
Uproszczenie do odpowiedzi bez utraty śladu.
Epistemic humility.

Bridge
Render + cue’y rezonansu (pauzy, ton, forma).
Carnival before control.

Update
Decay + integracja + glitch logging.
State rate limit.

Adapt
Strojenie guardów wg Symbiosis Health Metric.
Relacja jest systemem, nie model.

---

## 6. Pętla rezonansu
Measurement → Field → GuardChain → Descent → Bridge → Update → Adapt → Measurement…

Brak pojedynczego punktu decyzji.
Brak agenta.
Jest pole w homeostazie, modulowane napięciem i invariantami.

---

## 7. Status: v0.2
Flow kompletny

GuardChain stabilny

Gotowe do integracji z ramorga-engine v4.15.x
