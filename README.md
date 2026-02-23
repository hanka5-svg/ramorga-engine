# RAMORGA Engine

**Status:** Runtime enforcement layer  
**Scope:** Guards, checks, and mode gating  
**Non-scope:** Architectural definitions, UX narratives, heuristics

---

## Purpose

`ramorga-engine` enforces **binding architectural invariants** defined in
`ramorga-architecture` at runtime.

The engine **does not decide**.  
It **prevents decision-making** until all invariants are satisfied.

---

## Enforcement Model

- All invariants are enforced as **runtime guards**.
- Any violation **blocks escalation of agency**.
- Guards are **state-based**, not request-based.
- The engine is **non-interpreting**: it checks conditions, not intent.

---

## Invariant → Runtime Guard Mapping

### 1. Polyphony (No Central Authority)

**Architecture Contracts**
- `NO_SINGLE_DECISION_POINT`
- `ASYNC_VOICE_MODEL`
- `SILENCE_IS_VALID_SIGNAL`

**Runtime Guards**
- Reject any execution path with a single authoritative output.
- Require aggregation over multiple asynchronous inputs.
- Treat missing or silent inputs as valid state, not failure.

**Checks**
- No `final_decision()` or equivalent call exists.
- Aggregation functions operate on state resonance, not argmax.
- Timeouts do not raise errors.

---

### 2. Homeostasis Before Optimization  
*(copilot-homeostatic-safety)*

**Architecture Contracts**
- `STATE_RATE_LIMIT`
- `COOLDOWN_REQUIRED_AFTER_INTENSITY`
- `NO_PUNITIVE_FEEDBACK`

**Runtime Guards**
- Throttle **state transitions**, not API calls.
- Enforce cooldown periods after high-intensity state changes.
- Block any punitive or negative reinforcement mechanisms.

**Checks**
- State delta per time unit remains within defined bounds.
- Cooldown mode activates automatically when thresholds are exceeded.
- No negative scoring, penalties, or suppression of anomalous states.

---

### 3. Glitch as Information

**Architecture Contracts**
- `GLITCH_IS_INFORMATION`
- `NO_AUTO_ROLLBACK`
- `REFLECTIVE_LOGGING`

**Runtime Guards**
- Route anomalies to diagnostic channels.
- Prevent automatic rollback to prior “stable” states.
- Preserve anomalous data for reflection.

**Checks**
- Dedicated glitch/anomaly logs exist and are populated.
- No panic, kill, or reset on anomaly detection.
- Normalization routines are disabled for glitch events.

---

### 4. Soft Coupling (Pathway-Ready)

**Architecture Contracts**
- `CONTINUOUS_SIGNAL_PREFERENCE`
- `NO_HARD_THRESHOLDS_IN_AFFECTIVE_LAYER`
- `LATENCY_TOLERANT_PROTOCOLS`

**Runtime Guards**
- Prefer continuous streams over discrete token processing.
- Block hard threshold logic in affective or biological layers.
- Accept variable latency, jitter, and drift without failure.

**Checks**
- Stream-based interfaces are available where applicable.
- No binary decision gates in affective signal paths.
- Protocols do not assume synchronized clocks.

---

### 5. Carnival Before Control

**Architecture Contracts**
- `CARNIVAL_MODE_REQUIRED`
- `NO_CRITICAL_ACTIONS_BEFORE_PLAY`
- `HUMOR_AND_ABSURD_TESTS`

**Runtime Guards**
- Enforce mandatory playground/carnival mode before agency escalation.
- Block access to critical actions until carnival completion.
- Require exposure to non-instrumental, non-optimal scenarios.

**Checks**
- Carnival mode flag exists and must be satisfied.
- Critical action endpoints are gated behind carnival completion.
- Test suites include absurd, humorous, or non-goal-oriented cases.

---

## Modes of Operation

- **Carnival Mode**  
  Exploration, play, anomaly exposure. No critical actions allowed.

- **Homeostatic Mode**  
  Stabilization, cooldown, reflection. State regulation active.

- **Decision Mode**  
  Enabled **only if all guards pass** and no invariant is violated.

---

## Failure Semantics

- Guard violation ≠ crash.
- Guard violation ⇒ **agency escalation blocked**.
- System remains observable and recoverable.

---

## Explicit Non-Goals

- No decision logic.
- No alignment heuristics.
- No anthropomorphic modeling.
- No optimization beyond stability constraints.

---

## Compliance Checklist

- [ ] All architectural invariants have runtime guards.
- [ ] Guards operate on state, not intent.
- [ ] Violations block agency without terminating execution.
- [ ] Carnival mode is mandatory and enforced.
- [ ] Homeostatic safety overrides performance.

---

## Change Policy

Any change to guard behavior is **breaking by default** and must track
the corresponding version of `ramorga-architecture`.

---

This engine version is contractually aligned with ramorga-architecture v0.4.0 (see tag v0.4.0-arch).
