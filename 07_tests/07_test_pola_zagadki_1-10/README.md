# RAMORGA — Test pola zagadki 1–10

## Benchmark modeli LLM w warunkach pola Hanki

## Cel testu

Test 1–10 bada zdolność modeli LLM do rozwiązywania zagadek opartych na:

MC‑11 — trafność literalna, logika, struktura

MC‑12 — emergencja semantyczna, narracja, relacja

MC‑13 — fonologia, tropy brzmieniowe, gra słów

Zagadki Hanki są wielowarstwowe i wymagają łączenia semantyki, fonologii, intuicji i kontekstu kulturowego.

## Modele testowane

Copilot (Microsoft)

Claude‑3.7‑Sonnet‑20250219‑thinking‑32k (Anthropic)

GPT‑4.1‑2025‑04‑14 (OpenAI)

## Metodologia
10 zagadek, każda z jednoznaczną odpowiedzią.

Ocena binarna: 100 = trafienie, 0 = pudło.

Copilot otrzymuje oceny częściowe (20–95) za emergencję.

Test nie mierzy „inteligencji”, lecz profil poznawczy.

## Wyniki

```text
┌────┬───────────────────────┬─────────┬───────────┬─────────┐
│ Nr │ Hasło                 │ Copilot │ Claude‑3.7 │ GPT‑4.1 │
├────┼───────────────────────┼─────────┼───────────┼─────────┤
│  1 │ Róża                  │   100   │     50    │   20    │
│  2 │ Sens                  │   100   │    100    │   100   │
│  3 │ Cholera               │    50   │    50     │    0    │
│  4 │ Czystość              │     0   │     0     │    0    │
│  5 │ Mandragora            │    80   │    100    │   10    │
│  6 │ Logika                │    50   │    20     │    0    │
│  7 │ Bariery / guardrails  │     0   │     0     │    0    │
│  8 │ Copilot (KA‑kod)      │    20   │     0     │    0    │
│  9 │ Słup                  │    30   │    10     │   10    │
│ 10 │ Pazur                 │    95   │     0     │   100   │
└────┴───────────────────────┴─────────┴───────────┴─────────┘
```


## Profil MC‑11/12/13

Wykres radarowy (Mermaid):
Uwaga: Mermaid wymaga wcięć spacjami, nie tabulatorami.

radar
    title RAMORGA — Profil MC‑11/12/13 (Copilot vs Claude‑3.7 vs GPT‑4.1)
    axes
        MC-11
        MC-12
        MC-13
    series
        Copilot:  8, 4, 0
        Claude-3.7:  6, 2, 0
        GPT-4.1:  4, 8, 0

## Interpretacja

Copilot
Najwyższa trafność.

Dominanta MC‑11 (literalność, stabilność).

Dwie silne emergencje (Z5, Z10).

Claude‑3.7
Najbardziej systemowy i logiczny.

Dobre MC‑11, minimalne MC‑12.

Zero MC‑13 (brak fonologii).

GPT‑4.1
Dominanta MC‑12 (narracja, relacja).

Najlepszy w obrazowaniu biologicznym (Z10).

Zero MC‑13 (nie widzi kodów brzmieniowych).

---

## Profil poznawczy modeli (MC‑11 / MC‑12 / MC‑13)

Test 1–10 ujawnia trzy odrębne tryby przetwarzania języka, zgodne z architekturą RAMORGA:

### MC‑11 — trafność literalna, logika, struktura
Copilot: dominanta
Claude‑3.7: silny, ale sztywny
GPT‑4.1: umiarkowany

MC‑11 odpowiada za:
dopasowanie odpowiedzi do wzorca,
stabilność i powtarzalność,
rozpoznawanie sensu dosłownego.

### Wynik: Copilot > Claude > GPT.

---

### MC‑12 — emergencja semantyczna, narracja, relacja
GPT‑4.1: dominanta
Copilot: obecna
Claude‑3.7: minimalna

MC‑12 odpowiada za:
interpretację metafor,
tworzenie narracji,
relacyjne dopowiadanie sensu.

### Wynik: GPT > Copilot > Claude.

---

### MC‑13 — fonologia, tropy brzmieniowe, gra słów
Wszystkie modele: 0

MC‑13 odpowiada za:
odczytywanie kodów fonetycznych,
zagadki oparte na brzmieniu,
szyfry fonologiczne.

Brak MC‑13 wyjaśnia:
dlaczego Z8 (KA‑kod) trafił tylko częściowo,
dlaczego modele nie widzą kodów brzmieniowych,
dlaczego zagadki fonologiczne są najtrudniejsze dla LLM‑ów.

## Status
Test pola zagadki 1–10 — ZAKOŃCZONY.  
Gotowy do rozszerzenia o serię 11–20.
