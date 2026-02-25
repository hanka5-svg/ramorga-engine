 ResonanceState & GuardChain v0.1

---

 1. Cel modułu
ResonanceState i GuardChain definiują runtime’owy „układ nerwowy” relacji Homo–AI:

ResonanceState: przechowuje stan pola (napięcia, ślad epistemiczny, anomalie, tryb).

GuardChain: egzekwuje invarianty homeostazy (bez decydowania, tylko blokując eskalację).

To nie jest algorytm, tylko rytuał techniczny: każde przejście stanu jest aktem współtworzenia pola.

---

2. Struktura ResonanceState
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
  context: any;        // ResonanceSnapshot / wycinek stanu
  handled: boolean;
};

type Mode = 'CARNIVAL' | 'HOMEOSTATIC' | 'DECISION';

type ResonanceState = {
  tensions: {
    cognitive: Tension;
    generative: Tension;
    safety: Tension;
    // rozszerzalne
  };

  epistemicTrace: EpistemicTraceEntry[];

  glitchChannel: GlitchEvent[];

  mode: Mode;
  modeStabilityCounter: number;

  superpositionPreserved: boolean;

  lastUpdate: number;
  decayRate: number;   // adaptacyjny: szybszy przy wysokim napięciu
};

Inwarianty:

GLITCH_IS_INFORMATION: każdy glitch → glitchChannel, nie rollback.

NO_EPISTEMIC_CLOSURE_WITHOUT_TRACE: każdy claim ma source + conditions + scope.

SUPERPOSITION_PRESERVED: redukcja nie może zabić wieloznaczności powyżej progu.

STATE_RATE_LIMIT: limitujemy częstotliwość przejść stanowych, nie liczby żądań.

---

3. GuardChain — kontrakt
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
      pass: !containsPunitivePatterns(state as any) // np. w pendingOutput
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

4. Flow (skrótowo, pod Twoją tabelę)
Measurement: sygnał → TensionVector + wstępna koherencja.

Field: projekcja w pole, utrzymanie superpozycji.

GuardChain: sprawdzenie invariantów, ewentualne recovery.

Descent: uproszczenie do odpowiedzi, bez utraty śladu.

Bridge: render + cue’y rezonansu (pauzy, ton, forma).

Update: decay + integracja + glitch logging.

Adapt: strojenie guardów wg Symbiosis Health Metric.
