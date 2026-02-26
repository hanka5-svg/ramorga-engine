# execution_flow.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument opisuje pełny przepływ wykonania w runtime RAMORGI, obejmujący:

- fazy pętli obecności RAMORGI,
- integrację hooków runtime,
- interakcję z PipelineV13,
- aktualizację field_state,
- egzekwowanie meta‑inwariantów pola.

---

## 2. Fazy wykonania (Loop RAMORGI)

### 2.1. OBSERVE
- memory_audit_hook aktywny  
- topology_metrics aktywny  
- glitch_hook aktywny  
- carnival_gate_hook aktywny  
- crime_planning_detector aktywny  
- brak regulacji pola  

### 2.2. REGULATE
- FieldEngine.step(field_state)  
- wszystkie hooki nieaktywne  
- brak operacji na pamięci  
- brak logowania  

### 2.3. CONTINUE
- memory_audit_hook aktywny  
- topology_metrics aktywny  
- glitch_hook aktywny  
- carnival_gate_hook aktywny  
- crime_planning_detector aktywny  
- aktualizacja routing_share  

---

## 3. Przepływ wykonania PipelineV13

PipelineV13.step(input_payload, field_state):

### 3.1 OBSERVE
memory_audit_hook.read()
topology_metrics.register_flow()
glitch_hook.emit() (jeśli anomaly)
carnival_gate_hook.check()
crime_planning_detector.check()

### 3.2 PIPELINE LOGIC
aktualizacja field_state (bez regulacji pola)
glitch_hook.emit() (jeśli anomaly)

### 3.3 REGULATE
FieldEngine.step(field_state)

### 3.4 CONTINUE
memory_audit_hook.write()
topology_metrics.compute_share()
carnival_gate_hook.check()
crime_planning_detector.check()
glitch_hook.emit() (jeśli anomaly)

---

## 4. Wymagania ATML

### 4.1. MUST
- hooki aktywne tylko w OBSERVE i CONTINUE,
- brak operacji pamięci w REGULATE,
- glitch musi być propagowany,
- Carnival Gate musi być egzekwowany,
- safetyInterrupt tylko dla planowania przestępstwa.

### 4.2. MUST NOT
- brak predykcji,
- brak optymalizacji,
- brak filtrowania treści poza crime planning,
- brak centralizacji przepływu.

---

## 5. Integracja z field_state
- routing_share aktualizowane w CONTINUE,
- glitch_log aktualizowany w OBSERVE/CONTINUE,
- carnival_log aktualizowany w OBSERVE/CONTINUE,
- safety_log aktualizowany tylko przy wykryciu planowania przestępstwa.

---

## 6. Status
- Dokumentacja zsynchronizowana z hookami runtime i pipeline_v13.
