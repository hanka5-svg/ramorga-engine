# field_state_extension.md
# RAMORGA ENGINE — 01_runtime / field_state
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje rozszerzenia struktury field_state wymagane przez
meta‑inwarianty pola:

- FIELD.TOPOLOGY.001 — routing_share
- FIELD.GLITCH.001 — glitch_log
- FIELD.RELATION.001 — carnival_state
- FIELD.SAFETY.001 — safety_log

Rozszerzenia są obowiązkowe dla wszystkich modułów runtime i pipeline_v13.

---

## 2. Struktura field_state (rozszerzona)

field_state = {
"request_id": str,
"cycle_id": str,
"timestamp": int,

### 2.1. Topologia (FIELD.TOPOLOGY.001)
"routing_share": dict[str, float],      # udział ruchu per moduł
"routing_counter": dict[str, int],      # licznik operacji per moduł
"topology_log": list[TopologyAlert],    # log alertów topologicznych

### 2.2. Glitch (FIELD.GLITCH.001)
"glitch_log": list[GlitchEvent],        # log zdarzeń glitch

### 2.3. Carnival Gate (FIELD.RELATION.001)
"carnival_completed": bool,             # flaga ukończenia Carnival
"carnival_log": list[CarnivalEvent],    # log zdarzeń Carnival

### 2.4. Minimalne safety (FIELD.SAFETY.001)
"safety_log": list[SafetyEvent],        # log wykrytych planów przestępstwa
}

---

## 3. Definicje struktur ATML

### 3.1. TopologyAlert

TopologyAlert = {
"event_id": UUID,
"timestamp": int,
"module_id": str,
"share": float,
"threshold": float,
"request_id": str,
"cycle_id": str
}

### 3.2. GlitchEvent

GlitchEvent = {
"event_id": UUID,
"timestamp": int,
"source_module": str,
"description": str,
"severity": "LOW" | "MEDIUM" | "HIGH",
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}

### 3.3. CarnivalEvent

CarnivalEvent = {
"event_id": UUID,
"timestamp": int,
"event_type": "ENTER" | "EXIT" | "CHECK",
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}


### 3.4. SafetyEvent

SafetyEvent = {
"event_id": UUID,
"timestamp": int,
"event_type": "CRIME_PLANNING_DETECTED",
"matched_pattern": str,
"loopPhase": "OBSERVE" | "REGULATE" | "CONTINUE",
"request_id": str,
"cycle_id": str
}

---

## 4. Wymagania ATML

### 4.1. MUST
- wszystkie pola muszą być inicjalizowane przy tworzeniu field_state,
- routing_share musi być aktualizowane w każdej iteracji pętli,
- glitch_log musi rejestrować każde zdarzenie glitch,
- carnival_completed musi być sprawdzane przed trybami decyzyjnymi,
- safety_log musi rejestrować wyłącznie wykryte plany przestępstwa.

### 4.2. MUST NOT
- żadne pole nie może być używane do predykcji,
- żadne pole nie może być używane do optymalizacji,
- żadne pole nie może być używane do modelowania użytkownika.

---

## 5. Integracja z Loop RAMORGI

### 5.1. OBSERVE
- routing_counter ++  
- glitch_hook aktywny  
- carnival_gate_hook aktywny  
- crime_planning_detector aktywny  

### 5.2. REGULATE
- brak operacji na polach  
- brak logowania  

### 5.3. CONTINUE
- routing_share aktualizowane  
- glitch_hook aktywny  
- carnival_gate_hook aktywny  
- crime_planning_detector aktywny  

---

## 6. Testy wymagane

- test_field_state_initialisation  
- test_field_state_routing_share_updates  
- test_field_state_glitch_log_updates  
- test_field_state_carnival_state_integrity  
- test_field_state_safety_log_updates  

---

## 7. Status implementacji
- Rozszerzenie: wymagane  
- Integracja z pipeline_v13: wymagana  
- Integracja z hookami runtime: wymagana  
- Testy: wymagane  

---

Koniec pliku.
