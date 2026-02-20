# RAMORGA‑ENGINE — Test Plan (T1–T4)

Dokument definiuje pełny plan testów dla modułów RAMORGA‑ENGINE oraz integracji PipelineV13.

---

# 1. Zakres testów

Testy obejmują:

- moduły podstawowe:
  - field_state
  - tension_loop
  - energy_regulator
  - entropic_modulator
  - ritual_detector
  - snapshot_manager

- moduł integracyjny:
  - pipeline_v13

- cztery główne kategorie testów:
  - T1 — inicjalizacja
  - T2 — pojedynczy krok regulacji
  - T3 — stabilność energii (wielokrotne kroki)
  - T4 — snapshoty

---

# 2. Struktura testów

Każdy moduł posiada:
- test harness (szkielet),
- testy jednostkowe (NotImplementedError na etapie szkieletów),
- powiązanie z PipelineV13.

PipelineV13 posiada:
- testy integracyjne T1–T4.

---

# 3. Kategorie testów

## T1 — Test inicjalizacji
### Cel
Zweryfikować poprawną konstrukcję stanu oraz poprawne działanie trybu `init`.

### Dotyczy modułów
- field_state
- pipeline_v13

### Kryteria
- poprawna walidacja parametrów,
- poprawna konstrukcja FieldState,
- snapshot opcjonalny.

---

## T2 — Test jednego kroku regulacji
### Cel
Zweryfikować poprawne działanie sekwencji:
1. tension_loop  
2. energy_regulator  
3. entropic_modulator  
4. ritual_detector  

### Dotyczy modułów
- tension_loop
- energy_regulator
- entropic_modulator
- ritual_detector
- pipeline_v13

### Kryteria
- poprawna aktualizacja pól,
- brak efektów ubocznych,
- deterministyczność w test_mode.

---

## T3 — Test stabilności energii
### Cel
Zweryfikować brak dryfu energii przy wielu krokach regulacji.

### Dotyczy modułów
- energy_regulator
- entropic_modulator
- pipeline_v13

### Kryteria
- energia pozostaje w zakresie [E_min, E_max],
- brak chaotycznych oscylacji entropii,
- brak kumulacji błędów.

---

## T4 — Test snapshotów
### Cel
Zweryfikować poprawną serializację i odtwarzanie stanu.

### Dotyczy modułów
- snapshot_manager
- pipeline_v13

### Kryteria
- snapshot = pełna deterministyczna serializacja,
- restore = identyczność bitowa,
- snapshot po kroku ≠ snapshot po init.

---

# 4. Powiązanie testów z modułami

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

# 5. Determinizm

W trybie testowym:
- brak losowości,
- brak zależności od czasu,
- snapshoty deterministyczne,
- wszystkie moduły muszą zwracać identyczne wyniki dla identycznych wejść.

---

# 6. Kryteria zakończenia

Testy uznaje się za kompletne, gdy:
- wszystkie moduły mają pełne test harness,
- wszystkie testy T1–T4 są zaimplementowane,
- wszystkie moduły przechodzą testy po implementacji,
- snapshoty przechodzą test restore bit‑po‑bicie.

---

# 7. Uwagi końcowe

Dokument jest podstawą do implementacji testów i integracji modułów RAMORGA‑ENGINE.
