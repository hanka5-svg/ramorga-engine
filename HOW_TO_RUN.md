# HOW TO RUN — RAMORGA ENGINE

## 1. Klonowanie repo
git clone https://github.com/hanka5-svg/ramorga-engine
cd ramorga-engine

## 2. Uruchomienie minimalnego runtime
python 08_examples/minimal_runtime.py

## 3. Uruchomienie w Dockerze
docker-compose up --build

## 4. Integracja z LLM
W pliku:
    ramorga/integration/llm_proxy.py
podmień funkcję `send()` na wywołanie API LLM.

## 5. Testy
pytest 07_tests/
