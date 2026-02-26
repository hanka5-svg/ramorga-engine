# module_map.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument opisuje mapę modułów runtime RAMORGI oraz ich relacje z:

- hookami runtime,
- field_state,
- pipeline_v13,
- FieldEngine,
- DataBridge.

---

## 2. Moduły runtime

### 2.1. memory_audit_hook
- egzekwuje FIELD.MEMORY.001  
- aktywny w OBSERVE/CONTINUE  
- loguje operacje pamięci  

### 2.2. topology_metrics
- egzekwuje FIELD.TOPOLOGY.001  
- rejestruje przepływy  
- oblicza routing_share  

### 2.3. glitch_hook
- egzekwuje FIELD.GLITCH.001  
- propaguje glitch  
- loguje glitch  

### 2.4. carnival_gate_hook
- egzekwuje FIELD.RELATION.001  
- blokuje tryby decyzyjne  

### 2.5. crime_planning_detector
- egzekwuje FIELD.SAFETY.001  
- blokuje wyłącznie planowanie przestępstwa  

---

## 3. Relacje między modułami

input_payload
↓
PipelineV13
↓ (OBSERVE)
hooki runtime
↓
pipeline logic
↓ (REGULATE)
FieldEngine
↓ (CONTINUE)
hooki runtime
↓
DataBridge (SAVE)

---

## 4. Integracja z field_state
- routing_share  
- routing_counter  
- glitch_log  
- carnival_log  
- safety_log  

---

## 5. Status
- Mapa modułów zsynchronizowana z runtime i pipeline_v13.
