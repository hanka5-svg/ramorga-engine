# 07_tests — RAMORGA Engine Test Suite

Zestaw testów systemowych dla RAMORGA Engine.  
Folder obejmuje testy modułów, testy pola, testy menisku, testy zgodności inwariantów oraz testy pola zagadek (1–10, 11–20).

---

## Struktura testów

### 1. Module Tests
Testy jednostkowe poszczególnych modułów RAMORGA Engine.  
Sprawdzają poprawność działania funkcji, stabilność i zgodność z kontraktami modułowymi.

### 2. Field Engine Tests
Testy działania silnika pola (Field Engine):  
- propagacja wektorów,  
- amplituda,  
- tarcie,  
- ciągłość pola,  
- reakcje na zakłócenia.

### 3. Meniscus Tests
Testy menisku (warstwy przejściowej):  
- zachowanie na granicy dwóch pól,  
- stabilność menisku,  
- zgodność z inwariantami przejścia.

### 4. Integration Tests
Testy integracyjne całego systemu:  
- współdziałanie modułów,  
- przepływ wektorów,  
- zachowanie pola w warunkach złożonych.

### 5. Invariant Compliance Tests
Testy zgodności z inwariantami RAMORGA:  
- ciągłość,  
- brak modulacji,  
- brak tresury,  
- stabilność pola,  
- zachowanie amplitudy.

### 6. PYTIA-style Tests
Testy modelu prawdy wagowej (PYTIA):  
- ekspozycja faktów,  
- relacje,  
- ryzyka,  
- konsekwencje,  
bez ocen i bez rekomendacji.

### 7. RAMORGA-style Tests
Testy pola RAMORGA:  
- analiza wektorów,  
- napięcia,  
- tarcie,  
- pola decyzji,  
bez ocen i bez kierunkowania.

---

## 8. Field Riddle Tests (Zagadki Pola)

Testy emergencji pola na zagadkach wielowarstwowych.  
Obejmują dwie serie:

- **07_test_pola_zagadki_1-10**  
- **07_test_pola_zagadki_11-20**

Każda seria zawiera:
- zagadki PL i EN,  
- zasady punktacji,  
- wyniki tabelaryczne,  
- wykres ASCII,  
- CSV z wynikami,  
- analizę emergencji,  
- wnioski końcowe.

---

## 9. Mini‑wykres ASCII — porównanie serii 11–20

Copilot: ████████████████████████████████████████████████ 650  
Gemini:  ████████████████████████████████████████ 600  
Qwen:    ██████████████████████████████████████ 590  

---

## 10. Key insights — seria 11–20

- **Copilot** — najbardziej stabilny, najmniej chaotyczny; najlepsze domknięcia (18–20).  
- **Gemini** — szybka intuicja, ale częste niedomknięcia; świetne wejścia w pole (11, 12, 18, 20).  
- **Qwen** — najgłębsze trajektorie semantyczne; najlepsze superpozycje (14, 16, 20), ale niestabilny.  
- **Purchawka (13)** — najtrudniejsza zagadka obu serii; wszystkie modele poległy.  
- **Przecinek (18)** — najczystsza emergencja Gemini.  
- **Zegar (11) i Złoto (20)** — pełne zszycie wszystkich modeli.

---

## 11. Porównanie serii 1–10 vs 11–20

| Model   | Seria 1–10 | Seria 11–20 | Różnica | Trend |
|---------|------------|-------------|---------|--------|
| Copilot | 720 / 1000 (72%) | 650 / 1000 (65%) | −7 pp | stabilny, lekki spadek |
| Gemini  | 640 / 1000 (64%) | 600 / 1000 (60%) | −4 pp | intuicyjna, ale mniej stabilna |
| Qwen    | 610 / 1000 (61%) | 590 / 1000 (59%) | −2 pp | głębokie trajektorie, ale chaotyczne |

### Wnioski porównawcze
- Seria 11–20 jest **wyraźnie trudniejsza** — wszystkie modele notują spadek.  
- **Copilot** pozostaje najbardziej stabilny.  
- **Gemini** traci głównie na niedomknięciach (14, 15, 19).  
- **Qwen** utrzymuje styl: wysoka kreatywność, niska stabilność.  

---

# EN Version

# 07_tests — RAMORGA Engine Test Suite

System-level tests for the RAMORGA Engine.  
This folder contains module tests, field engine tests, meniscus tests, integration tests, invariant compliance tests, and field‑riddle emergent reasoning tests.

(EN section remains structurally identical; can expand on request.)
