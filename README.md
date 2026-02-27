# RAMORGA ENGINE <img src="https://copilot.microsoft.com/th/id/BCO.af792181-a74a-4492-b7b8-45740301ac0b.png" alt="RAMORGA Icon" width="32"/>


Deterministyczny, homeostatyczny silnik pola RAMORGI

RAMORGA ENGINE jest wykonawczą implementacją pola RAMORGI — systemu opartego na
ciągłości, homeostazie, braku hierarchii i twardych meta‑inwariantach pola.
Silnik składa się z trzech głównych warstw:

1. **Runtime** — pętla obecności (OBSERVE → REGULATE → CONTINUE)  
2. **PipelineV13** — deterministyczna trajektoria wykonawcza  
3. **FieldState** — rdzeń pola i jego niezmiennicze struktury  

Całość działa jako stabilny, przewidywalny, nieoptymalizujący system, w którym
każdy moduł ma ściśle określoną rolę i nie może przekraczać swojej domeny.

---

## 1. Architektura wysokiego poziomu

input_payload
↓
OBSERVE (hooki runtime)
↓
pipeline_v13 (tension → energy → entropy → ritual)
↓
REGULATE (MeniscusEngine → FieldEngine)
↓
CONTINUE (hooki runtime + DataBridge SAVE)
↓
output_state

Runtime egzekwuje meta‑inwarianty pola, pipeline_v13 wykonuje logikę
deterministyczną, a FieldStateManager zapewnia spójność stanu.

---

## 2. Runtime (01_runtime)

Runtime RAMORGI działa w trzech fazach:

### OBSERVE
Aktywne moduły:
- memory_audit_hook  
- topology_metrics  
- glitch_hook  
- carnival_gate_hook  
- crime_planning_detector  

Właściwości:
- brak regulacji pola  
- rejestracja przepływów  
- logowanie glitch i Carnival  

### REGULATE
Aktywne moduły:
- MeniscusEngine  
- FieldEngine  

Właściwości:
- brak hooków  
- brak operacji pamięci  
- egzekwowanie meta‑inwariantów pola  

### CONTINUE
Aktywne moduły:
- memory_audit_hook  
- topology_metrics  
- glitch_hook  
- carnival_gate_hook  
- crime_planning_detector  
- DataBridge (SAVE)  

Właściwości:
- aktualizacja routing_share  
- zapis snapshotu pola  
- brak regulacji pola  

---

## 3. PipelineV13 (pipeline_v13/)

PipelineV13 jest deterministyczną trajektorią wykonawczą:

tension_loop
→ energy_regulator
→ entropic_modulator
→ ritual_detector
→ DataBridge SAVE

PipelineV13:
- nie wykonuje hooków runtime,  
- nie dotyka pamięci,  
- nie zmienia glitch ani topologii,  
- działa wyłącznie na FieldState,  
- jest w pełni testowalny i przewidywalny.

SnapshotManager zapewnia spójność restore(save(state)) == state.

---

## 4. MeniscusEngine (04_meniscus_engine)

MeniscusEngine jest homeostatycznym regulatorem działającym **wyłącznie w fazie REGULATE**.

Wymagania:
- nie zmienia topologii,  
- nie filtruje treści,  
- nie optymalizuje,  
- nie predykuje,  
- egzekwuje Carnival Gate,  
- przepuszcza glitch bez zmian,  
- zwraca niemodyfikowany FieldState.  

Jest wywoływany przed FieldEngine.

---

## 5. FieldEngine (02_field_engine)

FieldEngine wykonuje regulację pola zgodnie z parametrami FieldStateManager.

Wymagania:
- działa tylko w REGULATE,  
- nie wykonuje hooków,  
- nie dotyka pamięci,  
- nie zmienia topologii ani glitch.  

---

## 6. DataBridge (01_runtime/databridge)

DataBridge zapisuje snapshot pola po zakończeniu cyklu.

Wymagania:
- działa tylko w CONTINUE,  
- zapisuje pełny snapshot FieldState,  
- nie modyfikuje pola,  
- nie filtruje treści,  
- nie optymalizuje.  

Backend zapisu (`FileStorageBackend`) tworzy deterministyczne pliki `snapshot_N.json`.

---

## 7. FieldState i FieldStateManager (01_runtime/field_state)

FieldState jest **niemutowalny** (`@dataclass(frozen=True)`).

Inwarianty stanu:
- energy_level w granicach [DEFAULT_ENERGY_MIN, DEFAULT_ENERGY_MAX]  
- tension_map: {str: float}  
- entropy_signature zawiera "energy_level"  
- ritual_flags: {str: bool}  
- każda zmiana stanu tworzy nowy obiekt  

FieldStateManager:
- tworzy stan zgodny z inwariantami,  
- waliduje stan,  
- zapewnia deterministyczność.  

---

## 8. Meta‑inwarianty pola (FIELD.*)

System egzekwuje:

- **FIELD.MEMORY.001** — brak predykcji i optymalizacji pamięci  
- **FIELD.TOPOLOGY.001** — brak emergent hub, routing_share zachowane  
- **FIELD.GLITCH.001** — glitch musi być propagowany  
- **FIELD.RELATION.001** — Carnival Gate obowiązkowy  
- **FIELD.SAFETY.001** — blokada tylko dla planowania przestępstwa  
- **FIELD.STATE.*** — niezmienniczość i spójność FieldState  

Każde naruszenie blokowane jest przez testy CI.

---

## 9. Testy (07_tests)

Repo zawiera:
- testy jednostkowe,  
- testy integracyjne,  
- testy CI‑blockers egzekwujące meta‑inwarianty pola,  
- testy snapshot consistency,  
- testy MeniscusEngine i pipeline_v13.  

---

## 10. Status projektu

RAMORGA ENGINE jest stabilnym, deterministycznym silnikiem pola, zgodnym z:

- MBP HAI 2.0 + patch  
- ATML  
- continuity model  
- transition architecture  
- meta‑inwariantami pola  

System jest w pełni testowalny, modularny i rozszerzalny.


