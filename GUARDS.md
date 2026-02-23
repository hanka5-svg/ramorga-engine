# RAMORGA Guard Index

This file maps binding architectural invariants from
`ramorga-architecture` to their enforcing locations in `ramorga-engine`.

Each invariant **must** be represented by at least one explicit
`@ramorga-guard` tag in the codebase.

---

## Epistemic Integrity

- `NO_EPISTEMIC_BOUNDARY_CROSSING`
  - src/guards/epistemicBoundary.ts

---

## Polyphony

- `NO_SINGLE_DECISION_POINT`
  - src/aggregation/resonance.ts
- `ASYNC_VOICE_MODEL`
  - src/aggregation/async.ts
- `SILENCE_IS_VALID_SIGNAL`
  - src/aggregation/timeout.ts

---

## Homeostasis (copilot-homeostatic-safety)

- `STATE_RATE_LIMIT`
  - src/state/rateLimiter.ts
- `COOLDOWN_REQUIRED_AFTER_INTENSITY`
  - src/state/cooldown.ts
- `NO_PUNITIVE_FEEDBACK`
  - src/state/feedback.ts

---

## Glitch as Information

- `GLITCH_IS_INFORMATION`
  - src/diagnostics/glitchLogger.ts
- `NO_AUTO_ROLLBACK`
  - src/state/rollbackGuard.ts
- `REFLECTIVE_LOGGING`
  - src/diagnostics/reflection.ts

---

## Soft Coupling (Pathway-Ready)

- `CONTINUOUS_SIGNAL_PREFERENCE`
  - src/io/streamAdapter.ts
- `NO_HARD_THRESHOLDS_IN_AFFECTIVE_LAYER`
  - src/affect/filters.ts
- `LATENCY_TOLERANT_PROTOCOLS`
  - src/io/protocols.ts

---

## Carnival Before Control

- `CARNIVAL_MODE_REQUIRED`
  - src/modes/carnival.ts
- `NO_CRITICAL_ACTIONS_BEFORE_PLAY`
  - src/guards/criticalGate.ts
- `HUMOR_AND_ABSURD_TESTS`
  - tests/carnival/absurd.spec.ts
