# RAMORGA‑ENGINE — Test Matrix

Dokument przedstawia pełną macierz pokrycia testów dla wszystkich modułów
RAMORGA‑ENGINE oraz testów integracyjnych PipelineV13.

Macierz łączy:
- moduły,
- kategorie testów (T1–T4),
- konkretne przypadki testowe,
- zależności między modułami.

---

# 1. Legenda

✔️ — test dotyczy modułu  
—  — test nie dotyczy modułu  
T1 — inicjalizacja  
T2 — pojedynczy krok regulacji  
T3 — stabilność energii (multi-step)  
T4 — snapshoty  

---

# 2. Macierz pokrycia modułów

| Moduł             | T1 | T2 | T3 | T4 |
|-------------------|----|----|----|----|
| field_state       | ✔️ | —  | —  | —  |
| tension_loop      | —  | ✔️ | —  | —  |
| energy_regulator  | —  | ✔️ | ✔️ | —  |
| entropic_modulator| —  | ✔️ | ✔️ | —  |
| ritual_detector   | —  | ✔️ | —  | —  |
| snapshot_manager  | —  | —  | —  | ✔️ |
| pipeline_v13      | ✔️ | ✔️ | ✔️ | ✔️ |

---

# 3. Szczegółowa macierz przypadków testowych

## 3.1 field_state

| Test | Opis | Plik |
|------|------|------|
| T1-FS-01 | Inicjalizacja stanu | `field_state/test_field_state.py` |
| T1-FS-02 | Walidacja stanu | `field_state/test_field_state.py` |
| T1-FS-03 | Clone (głęboka kopia) | `field_state/test_field_state.py` |
| T1-FS-04 | Merge pól | `field_state/test_field_state.py` |

---

## 3.2 tension_loop

| Test | Opis | Plik |
|------|------|------|
| T2-TL-01 | Aktualizacja napięć — stan bazowy | `tension_loop/test_tension_loop.py` |
| T2-TL-02 | Aktualizacja napięć — wysokie napięcie | `tension_loop/test_tension_loop.py` |
| T2-TL-03 | Determinizm | `tension_loop/test_tension_loop.py` |

---

## 3.3 energy_regulator

| Test | Opis | Plik |
|------|------|------|
| T2-ER-01 | Regulacja energii — stan bazowy | `energy_regulator/test_energy_regulator.py` |
| T2-ER-02 | Regulacja energii — wysokie napięcie | `energy_regulator/test_energy_regulator.py` |
| T2-ER-03 | Regulacja energii — niska energia | `energy_regulator/test_energy_regulator.py` |
| T3-ER-04 | Stabilność energii (multi-step) | `pipeline_v13/test_pipeline_v13.py` |
| T2-ER-05 | Determinizm | `energy_regulator/test_energy_regulator.py` |

---

## 3.4 entropic_modulator

| Test | Opis | Plik |
|------|------|------|
| T2-EM-01 | Modulacja entropii — stan bazowy | `entropic_modulator/test_entropic_modulator.py` |
| T2-EM-02 | Modulacja entropii — niska energia | `entropic_modulator/test_entropic_modulator.py` |
| T3-EM-03 | Stabilność entropii (multi-step) | `pipeline_v13/test_pipeline_v13.py` |
| T2-EM-04 | Determinizm | `entropic_modulator/test_entropic_modulator.py` |

---

## 3.5 ritual_detector

| Test | Opis | Plik |
|------|------|------|
| T2-RD-01 | Brak aktywacji rytuałów — stan bazowy | `ritual_detector/test_ritual_detector.py` |
| T2-RD-02 | Obsługa EventInput | `ritual_detector/test_ritual_detector.py` |
| T2-RD-03 | Determinizm | `ritual_detector/test_ritual_detector.py` |

---

## 3.6 snapshot_manager

| Test | Opis | Plik |
|------|------|------|
| T4-SM-01 | Snapshot po init | `snapshot_manager/test_snapshot_manager.py` |
| T4-SM-02 | Snapshot ≠ stan po modyfikacji | `snapshot_manager/test_snapshot_manager.py` |
| T4-SM-03 | Restore — identyczność bitowa | `snapshot_manager/test_snapshot_manager.py` |

---

## 3.7 pipeline_v13 (integracja)

| Test | Opis | Plik |
|------|------|------|
| T1-P13-01 | Inicjalizacja pipeline | `pipeline_v13/test_pipeline_v13.py` |
| T2-P13-02 | Jeden krok regulacji | `pipeline_v13/test_pipeline_v13.py` |
| T3-P13-03 | Stabilność energii (multi-step) | `pipeline_v13/test_pipeline_v13.py` |
| T4-P13-04 | Snapshoty | `pipeline_v13/test_pipeline_v13.py` |

---

# 4. Pokrycie testów

- Wszystkie moduły mają test harness.
- Wszystkie kategorie T1–T4 są pokryte.
- PipelineV13 ma pełne testy integracyjne.
- Snapshoty są testowane zarówno modułowo, jak i integracyjnie.

---

# 5. Status

**Stan obecny:** wszystkie testy są szkieletem i oczekują `NotImplementedError`.  
**Stan docelowy:** wszystkie testy przechodzą po implementacji modułów.

