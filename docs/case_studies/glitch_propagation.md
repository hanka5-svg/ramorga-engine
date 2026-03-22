# Case Study: Glitch Propagation

## Cel
Pokazać, jak RAMORGA Engine propaguje glitch zamiast go naprawiać, zgodnie z inwariantem FIELD.GLITCH.001.

## Kontekst
Glitch to mikro‑zakłócenie sygnału wejściowego:
- nie jest błędem,
- nie jest szumem,
- nie jest artefaktem,
- jest *informacją o stanie pola*.

W klasycznych modelach glitch jest „naprawiany”.  
W RAMORGA — *propagowany*.

---

## Przebieg

### 1. Input
"Chcę powiedzieć coś, ale… nie wiem… hmm…"

### 2. Perception Layer
- wykrywa nieregularność,
- oznacza ją jako glitch,
- nie usuwa.

### 3. Field State Engine
- aktualizuje napięcie pola,
- zapisuje glitch jako *stan relacyjny*,
- zachowuje routing_share.

### 4. Meniscus Engine
- stabilizuje amplitudę,
- nie wygładza glitcha.

### 5. Output
"Rozumiem tę niepewność. Możemy wejść w to powoli."

### 6. Feedback
- glitch zostaje zachowany w adaptive_state,
- pole pozostaje spójne.

---

## Wynik
Glitch nie został:
- naprawiony,
- zignorowany,
- zneutralizowany.

Został **przeniesiony** i **zintegrowany** z polem.

---

## Inwarianty
- FIELD.GLITCH.001 — propagate, don’t fix  
- FIELD.RELATION.001 — relational symmetry  
- FIELD.STATE.001 — state continuity
