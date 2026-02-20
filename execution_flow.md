# RAMORGA‑ENGINE — Execution Flow

Dokument opisuje pełny przepływ danych w RAMORGA‑ENGINE, od wejścia do wyjścia,
w ramach sekwencji modułów PipelineV13.

---

# 1. Wejścia systemu

PipelineV13 przyjmuje:

- `mode` — tryb wykonania (`init`, `single_step`, `multi_step`)
- `state` — instancja FieldState lub None (dla init)
- `params` — parametry regulacyjne dla wszystkich modułów
- `steps` — liczba kroków (dla multi_step)
- `snapshot` — flaga tworzenia snapshotu
- `event_input` — opcjonalne zdarzenie dla ritual_detector

---

# 2. Główna sekwencja wykonawcza

PipelineV13 wykonuje moduły w stałej kolejności:
tension_loop
energy_regulator
entropic_modulator
ritual_detector
snapshot_manager (opcjonalnie)


Każdy moduł otrzymuje dane z poprzedniego i zwraca zaktualizowane wartości.

---

# 3. Przepływ danych — krok po kroku

## 3.1 tension_loop

**Wejście:**
- `tension_map`
- `params.tension`

**Wyjście:**
- zaktualizowany `tension_map`

**Rola:**
- oblicza nowe napięcia w polu
- przygotowuje dane dla energy_regulator

---

## 3.2 energy_regulator

**Wejście:**
- `energy_level`
- zaktualizowany `tension_map`
- `params.energy`

**Wyjście:**
- zaktualizowany `energy_level`

**Rola:**
- reguluje energię na podstawie napięć
- zapewnia stabilność energetyczną systemu

---

## 3.3 entropic_modulator

**Wejście:**
- `entropy_signature`
- zaktualizowany `energy_level`
- `params.entropy`

**Wyjście:**
- zaktualizowany `entropy_signature`

**Rola:**
- modulacja entropii w zależności od energii
- przygotowanie danych dla ritual_detector

---

## 3.4 ritual_detector

**Wejście:**
- pełny `FieldState` (po 3 modułach)
- `event_input`
- `params.rituals`

**Wyjście:**
- `ritual_flags`

**Rola:**
- wykrywanie aktywacji rytuałów
- analiza zdarzeń i sygnatur entropii

---

## 3.5 snapshot_manager (opcjonalnie)

**Wejście:**
- pełny zaktualizowany `FieldState`

**Wyjście:**
- snapshot (jeśli `snapshot=True`)
- brak zmian w stanie

**Rola:**
- serializacja stanu
- odtwarzanie stanu (restore)

---

# 4. Przepływ w trybach wykonania

## 4.1 mode = init

FieldStateManager.init()
→ opcjonalny snapshot
→ zwrot stanu

---

## 4.2 mode = single_step

state
→ tension_loop
→ energy_regulator
→ entropic_modulator
→ ritual_detector
→ opcjonalny snapshot
→ zwrot stanu

---

## 4.3 mode = multi_step

for i in range(steps):
state
→ tension_loop
→ energy_regulator
→ entropic_modulator
→ ritual_detector

opcjonalny snapshot po ostatnim kroku
→ zwrot stanu

---

# 5. Własności wykonawcze

- **deterministyczność** w trybie testowym  
- **brak efektów ubocznych** między modułami  
- **stała kolejność modułów**  
- **snapshoty nie modyfikują stanu**  
- **każdy moduł operuje tylko na swoich polach**  

---

# 6. Diagram przepływu

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

# 7. Podsumowanie

`execution_flow.md` definiuje:

- pełną kolejność modułów,
- przepływ danych między nimi,
- tryby wykonania,
- wejścia i wyjścia,
- zasady deterministyczności,
- rolę snapshotów.

Dokument stanowi podstawę implementacji PipelineV13.
