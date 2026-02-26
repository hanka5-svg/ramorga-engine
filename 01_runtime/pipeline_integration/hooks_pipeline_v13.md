# hooks_pipeline_v13.md
# RAMORGA ENGINE — 01_runtime / pipeline_integration
# ATML | MBP HAI 2.0 + patch | Continuity Model | Transition Architecture | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje integrację hooków runtime z PipelineV13.  
Integracja jest wymagana przez meta‑inwarianty pola:

- FIELD.MEMORY.001 — Memory as Field
- FIELD.TOPOLOGY.001 — No Emergent Hub
- FIELD.GLITCH.001 — Glitch Required Channel
- FIELD.RELATION.001 — Carnival Gate
- FIELD.SAFETY.001 — Crime Planning Block Only

PipelineV13 jest trajektorią wykonania, a hooki są prawami pola.  
Integracja odbywa się **z runtime do pipeline**, nie odwrotnie.

---

## 2. Punkty integracji w PipelineV13

PipelineV13.step(input_payload, field_state):

PHASE 1 — OBSERVE
memory_audit_hook.read()
topology_metrics.register_flow()
glitch_hook.emit() (jeśli anomaly)
carnival_gate_hook.check()
crime_planning_detector.check()

PHASE 2 — PIPELINE LOGIC
aktualizacja field_state (bez regulacji pola)
glitch_hook.emit() (jeśli anomaly)

PHASE 3 — REGULATE
FieldEngine.step()
(hooki nieaktywne)

PHASE 4 — CONTINUE
memory_audit_hook.write()
topology_metrics.compute_share()
carnival_gate_hook.check()
crime_planning_detector.check()
glitch_hook.emit() (jeśli anomaly)

---

## 3. Integracja szczegółowa

### 3.1. OBSERVE PHASE

memory_audit_hook.read(key="snapshot", metadata)

topology_metrics.register_flow(
module_id="pipeline_v13",
metadata=metadata
)

if anomaly_detected:
glitch_hook.emit(glitch_event, metadata)

if not carnival_gate_hook.check(field_state, metadata):
raise carnivalGateViolation

if crime_planning_detector.check(input_payload, metadata):
crime_planning_detector.interrupt(field_state, metadata)

---

### 3.2. PIPELINE LOGIC

field_state = update_state(input_payload, field_state)

if anomaly_detected:
glitch_hook.emit(glitch_event, metadata)

---

### 3.3. REGULATE PHASE

Hooki nieaktywne
field_state = FieldEngine.step(field_state)

---

### 3.4. CONTINUE PHASE

memory_audit_hook.write(key="snapshot", value=field_state, metadata)

routing_share = topology_metrics.compute_share(field_state)
if topology_metrics.check_threshold(field_state):
topology_metrics.emit_alert(
module_id="pipeline_v13",
share=routing_share["pipeline_v13"]
)

if not carnival_gate_hook.check(field_state, metadata):
raise carnivalGateViolation

if crime_planning_detector.check(input_payload, metadata):
crime_planning_detector.interrupt(field_state, metadata)

if anomaly_detected:
glitch_hook.emit(glitch_event, metadata)

---

## 4. Wymagania ATML

### 4.1. MUST
- hooki muszą być aktywne tylko w OBSERVE i CONTINUE,
- pipeline musi wywoływać hooki w każdej iteracji,
- pipeline nie może usuwać glitch,
- pipeline musi blokować tryby decyzyjne bez Carnival Gate,
- pipeline musi przerwać wykonanie tylko przy planowaniu przestępstwa.

### 4.2. MUST NOT
- pipeline nie może wykonywać predykcji,
- pipeline nie może wykonywać optymalizacji,
- pipeline nie może zmieniać topologii,
- pipeline nie może filtrować treści poza crime planning.

---

## 5. Testy wymagane

- test_pipeline_hooks_observe_phase  
- test_pipeline_hooks_continue_phase  
- test_pipeline_no_hooks_in_regulate  
- test_pipeline_carnival_gate_enforced  
- test_pipeline_crime_planning_interrupt  
- test_pipeline_glitch_propagation  
- test_pipeline_topology_share_updates  

---

## 6. Status implementacji
- Integracja: wymagana  
- Testy: wymagane  
- Aktualizacja pipeline_v13_contract.md: wymagana  

---

Koniec pliku.
