# runtime_overview.md
# RAMORGA ENGINE — 01_runtime
# Kompletny przegląd runtime RAMORGI

## 1. Cel dokumentu
Dokument opisuje pełną architekturę runtime RAMORGI, obejmującą:

- pętlę wykonawczą Loop RAMORGI,
- hooki runtime,
- MeniscusEngine,
- FieldEngine,
- DataBridge (SAVE),
- integrację z pipeline_v13,
- egzekwowanie meta‑inwariantów pola.

Runtime jest homeostatyczny, niehierarchiczny i deterministyczny.

---

## 2. Loop RAMORGI — trzy fazy wykonania

### 2.1. OBSERVE
Aktywne moduły:
- memory_audit_hook
- topology_metrics
- glitch_hook
- carnival_gate_hook
- crime_planning_detector

Właściwości:
- brak regulacji pola,
- brak operacji pamięci przez pipeline,
- rejestracja przepływów,
- logowanie glitch i Carnival.

---

### 2.2. REGULATE
Aktywne moduły:
- MeniscusEngine
- FieldEngine

Właściwości:
- brak hooków runtime,
- brak operacji pamięci,
- brak logowania,
- egzekwowanie meta‑inwariantów pola,
- modulacja sygnału przez MeniscusEngine,
- regulacja pola przez FieldEngine.

---

### 2.3. CONTINUE
Aktywne moduły:
- memory_audit_hook
- topology_metrics
- glitch_hook
- carnival_gate_hook
- crime_planning_detector
- DataBridge (SAVE)

Właściwości:
- aktualizacja routing_share,
- logowanie glitch i Carnival,
- zapis snapshotu pola przez DataBridge,
- brak regulacji pola.

---

## 3. Architektura runtime

input_payload
↓
OBSERVE
↓
pipeline logic (pipeline_v13)
↓
REGULATE
↓
MeniscusEngine → FieldEngine
↓
CONTINUE
↓
DataBridge(SAVE)

---

## 4. Hooki runtime

### 4.1. memory_audit_hook
- aktywny w OBSERVE/CONTINUE,
- brak predykcji i optymalizacji,
- loguje operacje pamięci.

### 4.2. topology_metrics
- rejestruje przepływy,
- oblicza routing_share,
- egzekwuje FIELD.TOPOLOGY.001.

### 4.3. glitch_hook
- propaguje glitch,
- loguje glitch,
- egzekwuje FIELD.GLITCH.001.

### 4.4. carnival_gate_hook
- blokuje tryby decyzyjne,
- egzekwuje FIELD.RELATION.001.

### 4.5. crime_planning_detector
- blokuje wyłącznie planowanie przestępstwa,
- egzekwuje FIELD.SAFETY.001.

---

## 5. MeniscusEngine (REGULATE)

### Rola
Homeostatyczny regulator pomiędzy pipeline_v13 a FieldEngine.

### Wymagania
- działa tylko w REGULATE,
- nie zmienia topologii,
- nie zmienia glitch,
- nie filtruje treści,
- nie optymalizuje,
- egzekwuje Carnival Gate,
- zwraca niemodyfikowany field_state.

---

## 6. FieldEngine (REGULATE)

### Rola
Regulacja pola zgodnie z parametrami FieldStateManager.

### Wymagania
- działa tylko po MeniscusEngine,
- brak hooków,
- brak operacji pamięci,
- brak zmian topologii.

---

## 7. DataBridge (CONTINUE)

### Rola
Zapis snapshotu pola po zakończeniu cyklu.

### Wymagania
- działa tylko w CONTINUE,
- zapisuje pełny snapshot field_state,
- nie modyfikuje pola,
- nie filtruje treści,
- nie optymalizuje.

---

## 8. Integracja z pipeline_v13

### pipeline_v13 odpowiada za:
- wykonanie logiki tension → energy → entropy → ritual,
- wywołanie MeniscusEngine i FieldEngine,
- wywołanie DataBridge w fazie CONTINUE.

### pipeline_v13 nie może:
- wykonywać hooków runtime,
- modyfikować glitch,
- modyfikować topologii,
- wykonywać operacji pamięci.

---

## 9. Meta‑inwarianty pola

### FIELD.MEMORY.001
- brak predykcji,
- brak optymalizacji pamięci.

### FIELD.TOPOLOGY.001
- brak emergent hub,
- routing_share musi być zachowane.

### FIELD.GLITCH.001
- glitch musi być propagowany.

### FIELD.RELATION.001
- Carnival Gate musi być respektowany.

### FIELD.SAFETY.001
- blokada tylko dla planowania przestępstwa.

---

## 10. Status
Runtime RAMORGI jest kompletny, zsynchronizowany i zgodny z:

- MBP HAI 2.0 + patch,
- ATML,
- continuity model,
- transition architecture,
- meta‑inwariantami pola.

