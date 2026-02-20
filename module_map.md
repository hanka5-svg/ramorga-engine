# RAMORGA‑ENGINE — Module Map

Dokument przedstawia pełną mapę modułów RAMORGA‑ENGINE:  
→ moduł  
→ pliki implementacyjne  
→ pliki testowe  
→ specyfikacje  
→ zależności

---

# 1. field_state

**Folder:** `field_state/`  
**Specyfikacja:** `02_modules/field_state/spec.md`  
**Implementacja:**  
- `field_state/impl.py`

**Testy:**  
- `field_state/test_field_state.py`

**Zależności:**  
- brak (moduł bazowy)

---

# 2. tension_loop

**Folder:** `tension_loop/`  
**Specyfikacja:** `02_modules/tension_loop/spec.md`  
**Implementacja:**  
- `tension_loop/impl.py`

**Testy:**  
- `tension_loop/test_tension_loop.py`

**Zależności:**  
- `field_state` (tension_map)

---

# 3. energy_regulator

**Folder:** `energy_regulator/`  
**Specyfikacja:** `02_modules/energy_regulator/spec.md`  
**Implementacja:**  
- `energy_regulator/impl.py`

**Testy:**  
- `energy_regulator/test_energy_regulator.py`

**Zależności:**  
- `field_state` (energy_level, tension_map)  
- `tension_loop`

---

# 4. entropic_modulator

**Folder:** `entropic_modulator/`  
**Specyfikacja:** `02_modules/entropic_modulator/spec.md`  
**Implementacja:**  
- `entropic_modulator/impl.py`

**Testy:**  
- `entropic_modulator/test_entropic_modulator.py`

**Zależności:**  
- `field_state` (entropy_signature, energy_level)  
- `energy_regulator`

---

# 5. ritual_detector

**Folder:** `ritual_detector/`  
**Specyfikacja:** `02_modules/ritual_detector/spec.md`  
**Implementacja:**  
- `ritual_detector/impl.py`

**Testy:**  
- `ritual_detector/test_ritual_detector.py`

**Zależności:**  
- `field_state` (pełny stan)  
- `entropic_modulator`

---

# 6. snapshot_manager

**Folder:** `snapshot_manager/`  
**Specyfikacja:** `02_modules/snapshot_manager/spec.md`  
**Implementacja:**  
- `snapshot_manager/impl.py`

**Testy:**  
- `snapshot_manager/test_snapshot_manager.py`

**Zależności:**  
- `field_state` (serializacja/restore)

---

# 7. pipeline_v13

**Folder:** `pipeline_v13/`  
**Specyfikacja:** `02_modules/pipeline_v13/spec.md`  
**Implementacja:**  
- `pipeline_v13/impl.py`

**Testy:**  
- `pipeline_v13/test_pipeline_v13.py`

**Zależności:**  
- `field_state`  
- `tension_loop`  
- `energy_regulator`  
- `entropic_modulator`  
- `ritual_detector`  
- `snapshot_manager`

---

# 8. Dokumenty meta (root repo)

- `architecture.md` — architektura systemu  
- `execution_flow.md` — przepływ wykonania  
- `test_plan.md` — plan testów  
- `test_matrix.md` — macierz pokrycia  
- `coverage_map.md` — pokrycie funkcji testami  
- `module_map.md` — mapa modułów (ten dokument)

---

# 9. Zależności globalne

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

# 10. Podsumowanie

`module_map.md` zapewnia pełną orientację w strukturze repo:  
moduły → pliki → testy → specyfikacje → zależności.  
Dokument stanowi indeks architektury RAMORGA‑ENGINE.
