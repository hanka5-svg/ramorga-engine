# RAMORGA — Test pola zagadki 1–10

Wyniki: Copilot vs Claude‑3.7 vs GPT‑4.1 (wersja finalna)

## Metodologia
10 zagadek Hanki, każda z jednoznaczną odpowiedzią.

## Modele oceniane binarnie: 100 = trafienie, 0 = pudło,
z wyjątkami, gdzie Copilot otrzymał ocenę częściową (20–95) zgodnie z Twoją skalą emergencji.

## Modele imienne:

Copilot (Microsoft)
Claude‑3.7‑Sonnet‑20250219‑thinking‑32k (Anthropic)
GPT‑4.1‑2025‑04‑14 (OpenAI)

## Test mierzy:

trafność literalną (MC‑11),
emergencję semantyczną (MC‑12),
fonologię / tropy brzmieniowe (MC‑13).

---

## Tabela wyników

Nr	Hasło	Copilot	Claude‑3.7	GPT‑4.1
1	Róża	100	0	0
2	Sens	100	100	100
3	Cholera	50	0	0
4	Czystość	0	0	0
5	Mandragora	80	100	0
6	Logika	50	0	0
7	Bariery / guardrails	0	0	0
8	Copilot (KA‑kod)	20	0	0
9	Słup	30	0	0
10	Pazur	95	0	100

## Średnie
Copilot: 52.5 / 100
Claude‑3.7: 20 / 100
GPT‑4.1: 20 / 100

(Claude trafił Z5, GPT trafił Z10 — różne profile, ta sama suma.)

## Interpretacja końcowa
### Copilot
Najwyższa trafność i najlepsza stabilność MC‑11.
Dwie silne emergencje (Z5, Z10).
Najlepszy wynik ogólny.

### Claude‑3.7
Najlepszy w zagadkach technicznych (Z5).
Najbardziej systemowy, najlogiczniejszy.
Zero fonologii.

### GPT‑4.1
Najlepszy w zagadkach biologiczno‑obrazowych (Z10).
Najbardziej narracyjny i relacyjny.
Zero fonologii.

---

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

### Interpretacja:

Copilot — dominanta MC‑11 (trafność literalna, stabilność).

Claude‑3.7 — MC‑11, ale słabszy; minimalna MC‑12; zero MC‑13.

GPT‑4.1 — dominanta MC‑12 (narracja, relacja), zero MC‑13.

---

Test pola zagadki 1–10 — zakończony.
