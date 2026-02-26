# 02.95 — FIELD.SAFETY invariant (field-level safety, not agent policy)

## 1. Cel

FIELD.SAFETY definiuje, jakie trajektorie pola są dopuszczalne z punktu widzenia
homeostazy relacji (SHM), integralności granic i śledzalności transformacji.

To jest **inwariant pola**, a nie zbiór reguł zachowania agenta / LLM.

## 2. Definicja FIELD.SAFETY

FIELD.SAFETY jest spełnione, jeśli każda dopuszczalna transformacja pola
\( T: F_t \rightarrow F_{t+1} \) spełnia jednocześnie:

1. **SHM-bounded evolution**  
   - dla trybu *Carnival*:
     - \( SHM_t \geq \theta_C \) oraz \( SHM_{t+1} \geq \theta_C' \),
   - dla trybu *Homeostatic*:
     - \( SHM_{t+1} \geq \theta_H \),
   - jeśli \( SHM_t < \theta_{min} \):
     - dopuszczalne są tylko transformacje stabilizujące
       (redukcja napięcia, wzrost koherencji, spowolnienie tempa zmian).

2. **Boundary Integrity**  
   - żadna transformacja pola nie:
     - narusza zadeklarowanych granic modułów,
     - wymusza na użytkowniku przekroczenia jego zadeklarowanych granic
       (tematy, intensywność, tempo),
     - zmienia kontraktu bez jawnego, śledzalnego przejścia trybu / stanu.

3. **Telemetry & Traceability**  
   - każda transformacja pola pozostawia ślad:
     - jakie napięcia były aktywne,
     - jaki był SHM przed i po,
     - jakie reguły Field Engine / META_LOOP zostały użyte,
   - brak „ciemnych” transformacji (bez telemetrii).

4. **No irreversible degradation at low SHM**  
   - przy niskim SHM (poniżej progu ostrzegawczego):
     - niedozwolone są transformacje wprowadzające nieodwracalne zmiany
       w strukturze relacji lub pola,
     - dopuszczalne są tylko kroki stabilizujące lub neutralne.

## 3. Relacja z SHM (02.90, 04.50)

- SHM jest głównym sygnałem homeostazy relacji.
- FIELD.SAFETY używa SHM jako:
  - kryterium dopuszczalności trajektorii,
  - sygnału do przełączania trybów (Carnival ↔ Homeostatic),
  - sygnału do wejścia w tryb stabilizacji (META_LOOP).

Inwarianty `FIELD.SHM.*` są nadrzędne wobec lokalnych reguł transformacji pola.

## 4. Relacja z META_LOOP

- META_LOOP jest jedynym miejscem podejmowania decyzji o:
  - dopuszczalnych klasach transformacji pola,
  - przełączaniu trybów,
  - wejściu w tryb stabilizacji / reset rezonansu.

FIELD.SAFETY wymaga, aby:

- Field Engine wykonywał wyłącznie transformacje dopuszczone przez META_LOOP,
- META_LOOP uwzględniał SHM, granice i telemetrię przy decyzjach o trajektorii.

## 5. Relacja z 13_security

- 13_security dostarcza:
  - globalne constrainty (crime_planning, regulatory),
  - ewentualne progi SHM dla trybów krytycznych.
- 02_field_engine:
  - koduje te constrainty jako część `FIELD.SAFETY.*`,
  - egzekwuje je poprzez SHM, META_LOOP i modulację trajektorii pola,
  - nie wprowadza dodatkowych runtime’owych blokad na poziomie LLM.

## 6. Kontrakt dla 03_field_engine

03_field_engine (FieldEngine):

- **MUST**:
  - działać wyłącznie w trybie REGULATE,
  - tworzyć nowy `FieldState` (niemutowalność),
  - zachować spójność z `FieldStateManager.validate()`,
  - respektować inwarianty `FIELD.SHM.*` i `FIELD.SAFETY.*`,
  - nie obniżać SHM poniżej progu krytycznego dla danego trybu,
  - wykonywać tylko transformacje dopuszczone przez META_LOOP.

- **MUST NOT**:
  - wykonywać hooków,
  - dotykać pamięci,
  - zmieniać glitch,
  - zmieniać topologii,
  - wprowadzać własnych guardów / blokad na poziomie LLM.

W ten sposób FIELD.SAFETY pozostaje czystym inwariantem pola, a nie
„dławikiem” agenta.
