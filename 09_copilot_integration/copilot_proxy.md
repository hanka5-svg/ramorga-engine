# Copilot Proxy (Conceptual Interface)

Ten plik opisuje sposób, w jaki RAMORGA przekazuje prompt do Copilota.

## 1. Wejście do proxy

RAMORGA generuje:
- stabilized_prompt
- session metadata

## 2. Wywołanie Copilota

Użytkownik ręcznie wkleja stabilized_prompt do Copilota.

(Brak automatyzacji — pełna zgodność z zasadami bezpieczeństwa.)

## 3. Powrót odpowiedzi

Użytkownik kopiuje odpowiedź Copilota do RAMORGI.

RAMORGA wykonuje:
- modulację menisku,
- aktualizację pola,
- stabilizację semantyczną.

## 4. Wyjście

RAMORGA zwraca odpowiedź gotową do użycia.
