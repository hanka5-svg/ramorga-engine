# 07_test_pola_zagadki_21-30

Benchmark pola RAMORGA dla zagadek 21–30.  
Seria testuje:  
- poprawność collapse’u pola,  
- emergencję i stabilność reasoning,  
- zgodność odpowiedzi modeli z osią semantyczną pola,  
- odporność na odchylenia (C-score).
oraz jakość dopasowania modeli w trybie Arena.

Test obejmuje trzy orkiestracje:
- **Gemini**  
- **Qwen**  
- **Model X (Grok)**  

Każda zagadka została oceniona w dwóch wymiarach:
1. **Odpowiedź pola (C-score)** — — referencja RAMORGI 
2. **Arena modeli** — punktacja 0–100 (lub 0–90 w drugiej turze)

---

## 📊 Pliki w folderze

- **zagadki_PL.md** — oryginalne zagadki w języku polskim  
- **zagadki_EN.md** — wersja angielska  
- **zagadki_scoring.md** — zasady oceniania i metodologia  
- **wyniki_tabela.md** — pełna tabela wyników 21–30  
- **wyniki_wykres_ascii.md** — wizualizacja ASCII scoringu  
- **results.csv** — dane surowe do analizy

---

📈 Wyniki — podsumowanie serii 21–30
Pole RAMORGI (C‑score)
810 / 1000 (81%)

Arena modeli

Model	Suma	%
Gemini	640 / 1000	64%
Qwen	730 / 1000	73%
Model X	670 / 1000	67%

Gemini   ████████████████████████████████ 640
Qwen     ████████████████████████████████████████ 730
Model X  ████████████████████████████████████ 670


## 🧵 Podsumowanie pola (21–30)

Seria 21–30 pokazuje pełne spektrum pracy pola RAMORGA:
od czystych hard‑collapse’ów (lustro, cisza, dźwięk, zazdrość),
przez częściowe zszycia (wektor, morwa, biblioteczka),
aż po miejsca, gdzie pole wymagało korekty (Paryż, zapadka).

### Najmocniejsze zszycia (HC:100)
- lustro / odbicie  
- cisza / pole / echo / pamięć przestrzeni  
- dźwięk / kwant / fala / drganie  
- zazdrość  

### Częściowe collapse’y
- wektor (C:90) — brakowało jednego kliknięcia  
- biblioteczka (C:90) — książka zamiast regału  
- morwa (C:60) — owoc zamiast konkretu  
- zapadka (C:60) — domena trafiona, element nie  

### Największe odchylenie
- Paryż (C:10) — pole poszło w Montreal, łapiąc tylko francuskość

### Modele
- **Gemini**: bardzo silne wejścia w 21, 23, 25, 29  
- **Qwen**: najlepsza emergencja w 23, 27, 29  
- **Model X**: stabilny, często trafiał w sedno (21, 23, 25, 29), ale miał też duże odchylenia (26, 30)

Seria 21–30 zamyka się jako pełna mapa pola:
od fizyki i akustyki, przez emocje i literaturę,
po botanikę, mechanikę i architekturę treści.

---

## ⭐ Komentarz do SAMEGO POLA (21–30)

21) lustro / odbicie — HC:100  
22) cisza / pole / echo / pamięć — HC:100  
23) dźwięk / kwant / fala / drganie — HC:100  
24) susza / suchość / brak wody — C:100  
25) Paryż — C:10  
26) wektor — C:90  
27) morwa / owoc — C:60  
28) biblioteczka — C:90  
29) zazdrość — C:100  
30) zapadka — C:60  

Pole RAMORGA wykazało:
- pełną stabilność w zagadkach fizycznych i emocjonalnych,  
- częściowe odchylenia w zagadkach botanicznych i mechanicznych,  
- jedno duże odchylenie geograficzne (Paryż → Montreal).

---

## 📁 Linki

- **Tabela wyników:** `wyniki_tabela.md`  
- **Wykres ASCII:** `wyniki_wykres_ascii.md`  
- **Zasady scoringu:** `zagadki_scoring.md`  

---

## 🔚 Status

**Seria 21–30 — ZAKOŃCZONA.**  
Kolejna edycja (31–40) będzie tworzona przez modele jako zagadki dla pola RAMORGA.
