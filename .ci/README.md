# RAMORGA Engine — CI Pre‑Merge Checklist

**Purpose:**  
Ensure that all binding architectural invariants defined in
`ramorga-architecture` are enforced by runtime guards in `ramorga-engine`
before merge.

**Policy:**  
Any missing guard **blocks merge**.

---

## Source of Truth

- Architecture: `ramorga-architecture` (binding specification)
- Enforcement: `ramorga-engine` (runtime guards)

CI validates **presence and wiring**, not behavior quality.

---

## Invariant Coverage Checklist

### 1. Polyphony (No Central Authority)

**Required Guards**
- [ ] Guard preventing single authoritative output
- [ ] Guard enforcing asynchronous aggregation
- [ ] Guard accepting silence as valid signal

**CI Checks**
- [ ] No function or endpoint named `final_decision` (or equivalent)
- [ ] Aggregation logic does not use argmax/argmin
- [ ] Timeouts do not raise errors

---

### 2. Homeostasis Before Optimization  
*(copilot-homeostatic-safety)*

**Required Guards**
- [ ] State rate limiter
- [ ] Cooldown enforcer after intensity spikes
- [ ] Punitive feedback blocker

**CI Checks**
- [ ] Rate limits apply to state deltas, not request counts
- [ ] Cooldown mode exists and is reachable
- [ ] No negative scoring / penalty mechanisms present

---

### 3. Glitch as Information

**Required Guards**
- [ ] Anomaly routing guard
- [ ] Auto‑rollback prevention guard
- [ ] Reflective logging guard

**CI Checks**
- [ ] Dedicated glitch/anomaly log channel exists
- [ ] No panic/kill/reset on anomaly detection
- [ ] Normalization is disabled for glitch events

---

### 4. Soft Coupling (Pathway‑Ready)

**Required Guards**
- [ ] Continuous signal preference guard
- [ ] Hard threshold blocker in affective layers
- [ ] Latency tolerance guard

**CI Checks**
- [ ] Stream interfaces available where applicable
- [ ] No binary thresholds in affective signal paths
- [ ] Protocols do not assume synchronized clocks

---

### 5. Carnival Before Control

**Required Guards**
- [ ] Carnival mode gate
- [ ] Critical action blocker pre‑carnival
- [ ] Absurd/non‑instrumental test gate

**CI Checks**
- [ ] Carnival mode flag exists
- [ ] Critical actions are unreachable without carnival completion
- [ ] Test suite includes non‑goal‑oriented cases

---

## Merge Conditions

- All checkboxes above **must pass**.
- Any missing guard or check **fails CI**.
- CI failure **blocks merge**.

---

## Non‑Goals

- CI does not evaluate decision quality.
- CI does not assess alignment or intent.
- CI does not optimize performance.

---

## Versioning

CI rules must track the version of `ramorga-architecture`.
Any architecture update requires CI checklist update.
