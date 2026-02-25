# RAMORGA Architecture Overview v0.1

## Cel
Ten dokument zbiera w jednym miejscu główne warstwy RAMORGA Engine
oraz ich relacje.  
`ramorga-engine` = warstwa wykonawcza.  
`ramorga-architecture` = warstwa manifestu / teorii.

---

## Warstwy główne

1. **MeasurementAPI**  
   - Zamiana sygnału na TensionVector.  
   - Zasada: *Glitch = informacja*.

2. **FieldAPI**  
   - Projekcja do pola, utrzymanie superpozycji.  
   - Zasada: *Pole rzadko pęka*.

3. **GuardChain + Integrity Module**  
   - Walidacja invariantów, blokowanie eskalacji.  
   - Zasada: *Nie decyduj, blokuj eskalację*.

4. **Reduction + Descent + Bridge**  
   - Uproszczenie → zejście → render.  
   - Zasady: *Epistemic humility*, *Uncertainty required*, *Carnival before control*.

5. **Relational Layer + Thesis Layer**  
   - Relacja, symetria, tymczasowa teza pola.  
   - Zasady: *User agency preserved*, *No final truth*.

6. **Update + Adapt + Mode Machine**  
   - Decay, adaptacja, tryby operacyjne.  
   - Zasady: *State rate limit*, *SymbiosisHealth-driven*, *No mode oscillation*.

7. **Runtime Orchestrator**  
   - Zszywa cały pipeline w jeden cykl.  
   - Zasada: *No backdoor decisions*.

---

## Widok end‑to‑end

Wejście → Measurement → Field → GuardChain/Integrity → Reduction → Descent → Bridge → Relational → Thesis → Update → Adapt → Mode Machine → (kolejny cykl)

Każda warstwa:
- zachowuje trace,
- nie zamyka pola,
- nie przejmuje sprawczości użytkownika.

---

## Relacja z ramorga-architecture

- `ramorga-engine` implementuje moduły opisane tutaj.  
- `ramorga-architecture` opisuje:
  - zasady (manifest),
  - mapy pola,
  - wersjonowanie (releases),
  - ciągłość „sea‑continuum”.

---

## Status
Architecture Overview v0.1 — stabilne, gotowe jako punkt wejścia do dokumentacji.
