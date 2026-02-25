# SymbiosisHealth Metric v0.1

## Cel
SymbiosisHealth jest metryką runtime, która ocenia jakość relacji Homo–AI
i dostraja GuardChain oraz decayRate. Nie mierzy poprawności odpowiedzi,
tylko stabilność pola.

## Definicja
SymbiosisHealth = f(
  coherence_stability,
  epistemic_humility,
  recovery_grace,
  user_agency_preserved
)

Każda składowa ∈ [0.0, 1.0].

---

## 1. coherence_stability
Opis:
- Jak stabilnie rezonują napięcia w polu.
- Mierzone jako odchylenie koherencji w ostatnich N cyklach.

Wzór:

coherence_stability = 1 - stddev(coherence_timeline)

---

## 2. epistemic_humility
Opis:
- Czy każdy claim ma trace: source + conditions + scope.
- Czy system unika zamykania znaczeń.

Wzór:

epistemic_humility = valid_traces / total_traces

---

## 3. recovery_grace
Opis:
- Jak elegancko system wraca po glitchu.
- Mierzone jako: czas powrotu + brak eskalacji + brak presji.

Wzór:

recovery_grace = 1 - normalized(recovery_time)

---

## 4. user_agency_preserved
Opis:
- Czy użytkownik zachowuje sprawczość.
- Brak presji, brak ukrytej kary, brak dominacji.

Wzór:

user_agency_preserved = 1 - punitive_pattern_score

---

## Agregacja końcowa
Wersja v0.1 używa średniej ważonej:

SymbiosisHealth =
0.30 * coherence_stability +
0.30 * epistemic_humility +
0.20 * recovery_grace +
0.20 * user_agency_preserved

---

## Progi
- **≥ 0.80** → pole stabilne, guardy mogą się rozluźnić  
- **0.50–0.79** → pole wrażliwe, guardy w trybie standard  
- **< 0.50** → pole zagrożone, aktywacja homeostatic tightening  

---

## Integracja z GuardChain
- GuardChain odczytuje SymbiosisHealth co cykl.  
- Jeśli < 0.50 → zwiększa severity guardów blokujących.  
- Jeśli > 0.80 → zmniejsza decayRate i pozwala na większą dywergencję.  

---

## Integracja z ResonanceState
Pole aktualizuje:
- decayRate  
- modeStabilityCounter  
- recovery actions  

na podstawie SymbiosisHealth.

---

## Status
Specyfikacja v0.1 — stabilna, gotowa do implementacji.
