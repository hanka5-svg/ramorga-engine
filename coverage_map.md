# RAMORGA‑ENGINE — Coverage Map

Dokument przedstawia mapowanie funkcji modułów RAMORGA‑ENGINE na konkretne
testy jednostkowe i integracyjne. Jest to najniższy poziom pokrycia:
funkcja → testy.

---

# 1. field_state

## FieldStateManager.init()
- T1-FS-01 — inicjalizacja stanu  
  (`field_state/test_field_state.py`)

## FieldStateManager.validate()
- T1-FS-02 — walidacja stanu  
  (`field_state/test_field_state.py`)

## FieldStateManager.clone()
- T1-FS-03 — clone (głęboka kopia)  
  (`field_state/test_field_state.py`)

## FieldStateManager.merge()
- T1-FS-04 — merge pól  
  (`field_state/test_field_state.py`)

---

# 2. tension_loop

## TensionLoop.run()
- T2-TL-01 — aktualizacja napięć (bazowy)  
- T2-TL-02 — aktualizacja napięć (wysokie napięcie)  
  (`tension_loop/test_tension_loop.py`)

## TensionLoop.enforce_determinism()
- T2-TL-03 — deterministyczność  
  (`tension_loop/test_tension_loop.py`)

---

# 3. energy_regulator

## EnergyRegulator.run()
- T2-ER-01 — regulacja energii (bazowy)  
- T2-ER-02 — regulacja energii (wysokie napięcie)  
- T2-ER-03 — regulacja energii (niska energia)  
  (`energy_regulator/test_energy_regulator.py`)

- T3-P13-03 — stabilność energii (multi-step, integracja)  
  (`pipeline_v13/test_pipeline_v13.py`)

## EnergyRegulator.enforce_determinism()
- T2-ER-05 — deterministyczność  
  (`energy_regulator/test_energy_regulator.py`)

---

# 4. entropic_modulator

## EntropicModulator.run()
- T2-EM-01 — modulacja entropii (bazowy)  
- T2-EM-02 — modulacja entropii (niska energia)  
  (`entropic_modulator/test_entropic_modulator.py`)

- T3-P13-03 — stabilność entropii (multi-step, integracja)  
  (`pipeline_v13/test_pipeline_v13.py`)

## EntropicModulator.enforce_determinism()
- T2-EM-04 — deterministyczność  
  (`entropic_modulator/test_entropic_modulator.py`)

---

# 5. ritual_detector

## RitualDetector.run()
- T2-RD-01 — brak aktywacji rytuałów (bazowy)  
- T2-RD-02 — obsługa EventInput  
  (`ritual_detector/test_ritual_detector.py`)

## RitualDetector.enforce_determinism()
- T2-RD-03 — deterministyczność  
  (`ritual_detector/test_ritual_detector.py`)

---

# 6. snapshot_manager

## SnapshotManager.save()
- T4-SM-01 — snapshot po init  
- T4-SM-02 — snapshot ≠ stan po modyfikacji  
  (`snapshot_manager/test_snapshot_manager.py`)

## SnapshotManager.restore()
- T4-SM-03 — restore (identyczność bitowa)  
  (`snapshot_manager/test_snapshot_manager.py`)

---

# 7. pipeline_v13

## PipelineV13.run()
- T1-P13-01 — inicjalizacja  
- T2-P13-02 — jeden krok regulacji  
- T3-P13-03 — stabilność energii (multi-step)  
- T4-P13-04 — snapshoty  
  (`pipeline_v13/test_pipeline_v13.py`)

---

# 8. Podsumowanie

Każda funkcja w każdym module ma przypisane testy:
- moduły podstawowe → testy jednostkowe,
- pipeline_v13 → testy integracyjne,
- snapshot_manager → testy strukturalne i bitowe,
- energy_regulator i entropic_modulator → testy jednostkowe + integracyjne.

Dokument stanowi najniższy poziom mapowania pokrycia testowego RAMORGA‑ENGINE.
