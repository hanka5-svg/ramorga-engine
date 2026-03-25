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
Pełna tabela znajduje się w pliku:
wyniki_tabela.md

## Profil MC‑11/12/13

Wykres radarowy (Mermaid):

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
Copilot — najwyższa trafność, dominanta MC‑11, dwie emergencje.

Claude‑3.7 — najbardziej systemowy, logiczny, zero fonologii.

GPT‑4.1 — najbardziej narracyjny, relacyjny, zero fonologii.

## Status
Test pola zagadki 1–10 — ZAKOŃCZONY.  
Gotowy do rozszerzenia o serię 11–20.
