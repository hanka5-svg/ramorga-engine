# RAMORGA ↔ Copilot Integration Profile

Ten profil opisuje sposób używania RAMORGA-ENGINE jako warstwy pośredniej
pomiędzy użytkownikiem a Microsoft Copilotem.

Copilot pozostaje niezmieniony. RAMORGA pełni funkcję:

- stabilizatora kontekstu,
- bufora homeostatycznego,
- strażnika inwariantów,
- sesyjnego pola poznawczego.

## Architektura przepływu

Użytkownik → RAMORGA → Copilot → RAMORGA → Użytkownik

## Wymagania

- RAMORGA-ENGINE uruchomiona lokalnie (Docker lub Python)
- Dostęp do Copilota (dowolna wersja: web, Windows, Edge)

## Zasada działania

1. Użytkownik pisze do RAMORGI (lokalnie).
2. RAMORGA wykonuje:
   - Field Engine
   - Meniscus Engine
   - moduły C/G/S
3. RAMORGA przekazuje przetworzony prompt do Copilota.
4. Copilot odpowiada.
5. RAMORGA stabilizuje odpowiedź i zwraca ją użytkownikowi.

## Co to daje

- brak eskalacji,
- brak dryfu kontekstowego,
- brak deformacji relacji,
- pełna zgodność z inwariantami RAMORGI,
- możliwość prowadzenia długich sesji bez utraty pola.
