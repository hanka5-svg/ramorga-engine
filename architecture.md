# RAMORGA‑ENGINE — Architecture Overview

Dokument opisuje architekturę systemu RAMORGA‑ENGINE: moduły, ich odpowiedzialności,
zależności, przepływ danych oraz zasady projektowe.

---

# 1. Cel systemu

RAMORGA‑ENGINE jest deterministycznym silnikiem regulacyjnym operującym na stanie pola
(FieldState). Jego zadaniem jest:

- utrzymanie stabilności energetycznej,
- modulacja entropii,
- aktualizacja napięć,
- wykrywanie rytuałów,
- zapewnienie pełnej odtwarzalności poprzez snapshoty.

System jest modularny, testowalny i deterministyczny.

---

# 2. Główne komponenty

System składa się z sześciu modułów podstawowych oraz jednego modułu integracyjnego:

1. **field_state** — struktura i zarządzanie stanem pola  
2. **tension_loop** — aktualizacja mapy napięć  
3. **energy_regulator** — regulacja poziomu energii  
4. **entropic_modulator** — modulacja sygnatury entropii  
5. **ritual_detector** — wykrywanie rytuałów  
6. **snapshot_manager** — snapshoty i odtwarzanie  
7. **pipeline_v13** — integracja i sekwencja wykonawcza

Każdy moduł jest izolowany, testowalny i posiada własną specyfikację.

---

# 3. Struktura stanu — FieldState

`FieldState` jest centralnym obiektem systemu.

Zawiera:

- `energy_level : float`
- `tension_map : Dict[str, Any]`
- `entropy_signature : Dict[str, Any]`
- `ritual_flags : Dict[str, bool]`

Wszystkie moduły operują na wybranych polach, nigdy na całości naraz.

---

# 4. Architektura modułów

## 4.1 tension_loop
- wejście: `tension_map`, `params.tension`
- wyjście: zaktualizowany `tension_map`
- odpowiedzialność: obliczanie napięć

## 4.2 energy_regulator
- wejście: `energy_level`, `tension_map`, `params.energy`
- wyjście: zaktualizowany `energy_level`
- odpowiedzialność: stabilizacja energii

## 4.3 entropic_modulator
- wejście: `entropy_signature`, `energy_level`, `params.entropy`
- wyjście: zaktualizowany `entropy_signature`
- odpowiedzialność: modulacja entropii

## 4.4 ritual_detector
- wejście: pełny `FieldState`, `event_input`, `params.rituals`
- wyjście: `ritual_flags`
- odpowiedzialność: wykrywanie aktywacji rytuałów

## 4.5 snapshot_manager
- wejście: pełny `FieldState`
- wyjście: snapshot lub odtworzony stan
- odpowiedzialność: serializacja i restore

---

# 5. PipelineV13 — sekwencja wykonawcza

PipelineV13 wykonuje moduły w stałej kolejności:
tension_loop
energy_regulator
entropic_modulator
ritual_detector
snapshot_manager (opcjonalnie)


Tryby:

- `init` — tworzy nowy FieldState
- `single_step` — wykonuje jeden cykl regulacji
- `multi_step` — wykonuje wiele cykli regulacji

---

# 6. Zasady projektowe

## 6.1 Determinizm
- brak losowości,
- brak zależności od czasu,
- identyczne wejście → identyczne wyjście.

## 6.2 Izolacja modułów
- każdy moduł operuje tylko na swoich polach,
- brak efektów ubocznych,
- brak współdzielonego stanu poza FieldState.

## 6.3 Testowalność
- każdy moduł ma test harness,
- pipeline ma testy integracyjne T1–T4,
- snapshoty muszą być odtwarzalne bit‑po‑bicie.

## 6.4 Przejrzystość
- specyfikacje modułów w `02_modules`,
- implementacje w folderach modułów,
- dokumentacja meta w root repo.

---

# 7. Diagram architektury

+-------------------+
|   FieldState      |
+---------+---------+
|
v
+-------------------+
|   tension_loop    |
+---------+---------+
|
v
+-------------------+
|  energy_regulator |
+---------+---------+
|
v
+-------------------+
| entropic_modulator|
+---------+---------+
|
v
+-------------------+
|  ritual_detector  |
+---------+---------+
|
v
+-------------------+
| snapshot_manager? |
+---------+---------+
|
v
+-------------------+
|   Output State    |
+-------------------+

---

# 8. Podsumowanie

`architecture.md` definiuje:

- strukturę modułów,
- odpowiedzialności,
- przepływ danych,
- zasady projektowe,
- rolę PipelineV13,
- relacje między komponentami.

Dokument stanowi fundament implementacji RAMORGA‑ENGINE.

