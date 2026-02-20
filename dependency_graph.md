# RAMORGA‑ENGINE — Dependency Graph

Dokument przedstawia pełną mapę zależności między modułami RAMORGA‑ENGINE.
Zależności są jednokierunkowe i deterministyczne.  
Każdy moduł operuje tylko na swoich polach FieldState i nie modyfikuje innych.

---

# 1. Zależności globalne (wysoki poziom)

field_state
↓
tension_loop
↓
energy_regulator
↓
entropic_modulator
↓
ritual_detector
↓
snapshot_manager (opcjonalnie)
↓
pipeline_v13 (integracja)


---

# 2. Zależności szczegółowe

## 2.1 field_state
**Zależności:** brak  
**Używany przez:** wszystkie moduły

---

## 2.2 tension_loop
**Zależności:**  
- field_state (tension_map)

**Używany przez:**  
- pipeline_v13

---

## 2.3 energy_regulator
**Zależności:**  
- field_state (energy_level, tension_map)  
- tension_loop

**Używany przez:**  
- pipeline_v13

---

## 2.4 entropic_modulator
**Zależności:**  
- field_state (entropy_signature, energy_level)  
- energy_regulator

**Używany przez:**  
- pipeline_v13

---

## 2.5 ritual_detector
**Zależności:**  
- field_state (pełny stan)  
- entropic_modulator  
- event_input (opcjonalnie)

**Używany przez:**  
- pipeline_v13

---

## 2.6 snapshot_manager
**Zależności:**  
- field_state (serializacja/restore)

**Używany przez:**  
- pipeline_v13 (opcjonalnie)

---

## 2.7 pipeline_v13
**Zależności:**  
- field_state  
- tension_loop  
- energy_regulator  
- entropic_modulator  
- ritual_detector  
- snapshot_manager

**Używany przez:**  
- użytkownika / API

---

# 3. Diagram zależności (ASCII)

+------------------+
|   field_state    |
+--------+---------+
|
v
+------------------+
|   tension_loop   |
+--------+---------+
|
v
+------------------+
| energy_regulator |
+--------+---------+
|
v
+------------------+
| entropic_modulator |
+--------+-----------+
|
v
+------------------+
| ritual_detector  |
+--------+---------+
|
v
+------------------+
| snapshot_manager |
+--------+---------+
|
v
+------------------+
|   pipeline_v13   |
+------------------+

---

# 4. Zasady zależności

- **brak cykli** — graf jest acykliczny (DAG)  
- **jednokierunkowy przepływ** — dane płyną tylko w dół  
- **moduły nie znają siebie nawzajem** — tylko pipeline je łączy  
- **FieldState jest jedynym wspólnym medium**  
- **snapshot_manager nie wpływa na przepływ** — tylko obserwuje  

---

# 5. Podsumowanie

`dependency_graph.md` definiuje pełną strukturę zależności RAMORGA‑ENGINE:  
moduły → dane → kierunek przepływu → integracja w PipelineV13.  
Dokument stanowi podstawę dla implementacji i testów integracyjnych.
