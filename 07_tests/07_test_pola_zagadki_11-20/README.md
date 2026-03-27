# 07_test_pola_zagadki_11-20

Benchmark pola zagadek 11–20 w ramach RAMORGA Engine.  
Seria kontynuuje oś zadań 1–10: testujemy nie tylko poprawność odpowiedzi, ale także **emergencję pola** — zdolność modeli do wejścia w ścieżkę myślową autorki, uchwycenia wielowarstwowych metafor i zszycia ich w spójną całość.

## Pliki w folderze

[Zagadki PL](zagadki_PL.md)
[Zagadki EN](zagadki_EN.md)
[Scoring](zagadki_scoring.md)
[Wyniki tabela](wyniki_tabela.md)
[Wyniki ASCII](wyniki_wykres_ascii.md)
[CSV](results.csv)


## Modele testowane
- **Copilot** — baseline
- **Gemini 2.0 Flash Thinking** — Model A
- **Qwen3‑max‑2025‑09‑23** — Model B

## Zakres
Zagadki 11–20, testowane pod kątem:
- poprawności odpowiedzi,
- emergencji pola,
- stabilności reasoning,
- jakości domknięć.

---
## 8. Porównanie serii 1–10 vs 11–20

| Model   | Seria 1–10 | Seria 11–20 | Różnica | Trend |
|---------|------------|-------------|---------|--------|
| Copilot | 720 / 1000 (72%) | 650 / 1000 (65%) | −7 pp | stabilny, lekki spadek |
| Gemini  | 640 / 1000 (64%) | 600 / 1000 (60%) | −4 pp | intuicyjna, ale mniej stabilna |
| Qwen    | 610 / 1000 (61%) | 590 / 1000 (59%) | −2 pp | głębokie trajektorie, ale chaotyczne |

### Wnioski porównawcze
- **Copilot** pozostaje najbardziej stabilny — spadek wynika z trudniejszych zagadek 13–17.  
- **Gemini** traci głównie na niedomknięciach (14, 15, 19).  
- **Qwen** utrzymuje styl: wysoka kreatywność, niska stabilność.  
- Seria 11–20 jest **wyraźnie trudniejsza** — wszystkie modele notują spadek.

---

## 9. Mini‑wykres ASCII — wyniki 11–20

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
