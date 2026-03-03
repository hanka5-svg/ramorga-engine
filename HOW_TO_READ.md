## `ramorga-engine` — Jak czytać to repo

---

### Czym to jest

To wykonanie konstytucji. Deterministyczny silnik pola, w którym inwarianty są egzekwowane, nie interpretowane.

Każda linia kodu odnosi się do inwariantu z `ramorga-architecture`. Każdy test to blokada konstytucyjna, nie weryfikacja funkcjonalna.

### Czym to nie jest

- **Nie jest miejscem na decyzje architektoniczne.** Te decyzje zostały podjęte w ADR przekazanym Ci przez architekta.
- **Nie jest otwarte na optymalizację.** "Działa szybciej" nie jest dopuszczalne, jeśli narusza inwariant.
- **Nie jest dokumentacją intencji.** Intencja została osadzona w ADR. Tu jest tylko zgodność.

### Jak czytać

Czytaj w kolejności:

1. **ADR od architekta** — nie zaczynaj od kodu. Zacznij od dokumentu osadzenia, który otrzymałeś. To Twój konstytucyjny kontekst.
2. **08_meta_invariants** (lub odpowiednik w kodzie) — sprawdź, jakie inwarianty są egzekwowane w tym konkretnym wykonaniu.
3. **01_runtime/field_state** — zrozum strukturę pola. To jest niemutowalny rdzeń. Każda zmiana stanu tworzy nowy obiekt. To nie jest wybór implementacyjny. To egzekucja `FIELD.STATE.*`.
4. **pipeline_v13** — prześledź deterministyczną trajektorię. Brak gałęzi warunkowych, które nie wynikają bezpośrednio z inwariantu.
5. **07_tests** — przeczytaj nazwy testów. Każdy `test_constitutional_block_*` to granica, którą nie możesz przekroczyć.

### Jak czytać kod

Szukaj komentarzy:

```python

# FIELD.MEMORY.001: brak predykcji i optymalizacji pamięci
# Osadzenie: pamięć jest rejestracją, nie modelem
# Konsekwencja: brak gradientu, brak aktualizacji wag

```

Komentarz składa się z trzech części:
- **Referencja** — który inwariant
- **Osadzenie** — co to oznacza w tym kontekście
- **Konsekwencja** — jakie ograniczenia wynikają dla kodu

Jeśli napotkasz kod bez takiego komentarza — to błąd w repo, nie luz interpretacyjny.

### Co robić po przeczytaniu

Implementuj zgodnie z ADR. Pisz testy CI-blokujące dla każdej granicy, którą wprowadzasz. Nie twórz nowych inwariantów — to kompetencja architekta. Nie interpretuj istniejących — to zostało osadzone przed Tobą.

### Co robić, jeśli napotkasz konflikt

Jeśli implementacja wymaga naruszenia inwariantu — nie szukaj obejścia. Zwróć się do architekta. Konflikt może oznaczać:
- błąd w Twoim rozumieniu ADR
- błąd w ADR (wymagający rewizji przez architekta)
- niemożliwość osadzenia RAMORGI w tym konkretnym polu

W każdym przypadku — pętla zwrotna do architekta, nie samodzielna decyzja.
