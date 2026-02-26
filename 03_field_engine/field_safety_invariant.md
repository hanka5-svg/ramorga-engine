# FieldEngine — FIELD.SAFETY Runtime Mirror

Ten dokument opisuje, jak 03_field_engine wykonuje inwariant FIELD.SAFETY
zdefiniowany w `ramorga-architecture/02_field_engine/field_safety_invariant.md`.

03_field_engine **nie definiuje** FIELD.SAFETY.  
03_field_engine **wykonuje** FIELD.SAFETY jako część procesu REGULATE.

---

## 1. Zakres

FIELD.SAFETY w runtime oznacza, że każda transformacja pola wykonana przez
`FieldEngine.step()` musi być zgodna z:

- `FIELD.SHM.*` (SHM-bounded evolution),
- `FIELD.SAFETY.*` (Boundary Integrity, Telemetry, No irreversible degradation),
- decyzjami META_LOOP dotyczącymi dopuszczalnych trajektorii.

03_field_engine nie implementuje logiki SHM ani META_LOOP — jedynie **respektuje** ich decyzje.

---

## 2. Zasady wykonawcze (runtime)

### 2.1. SHM-bounded execution

FieldEngine:

- nie może obniżyć SHM poniżej progu krytycznego dla danego trybu,
- musi stosować się do ograniczeń trajektorii narzuconych przez META_LOOP,
- może wykonywać tylko transformacje oznaczone jako „dopuszczalne” przez `FieldStateManager`.

### 2.2. Boundary Integrity

FieldEngine:

- nie może wykonywać transformacji naruszających granice modułów,
- nie może zmieniać kontraktu ani trybu — jedynie stosować się do decyzji META_LOOP,
- nie może generować transformacji, które wymuszają przekroczenie granic użytkownika.

### 2.3. Telemetry & Traceability

Każda transformacja pola musi:

- pozostawić ślad w `FieldState.telemetry`,
- raportować SHM przed i po transformacji,
- raportować użyte reguły transformacji.

FieldEngine nie może wykonywać „ciemnych” transformacji bez telemetrii.

---

## 3. Ograniczenia runtime (MUST NOT)

FieldEngine:

- nie wykonuje hooków,
- nie dotyka pamięci,
- nie zmienia glitch,
- nie zmienia topologii,
- nie wprowadza własnych guardów ani blokad na poziomie LLM,
- nie implementuje własnej logiki bezpieczeństwa.

Wszelka logika bezpieczeństwa pochodzi z pola (02_field_engine) i jest egzekwowana
poprzez SHM, META_LOOP i inwarianty FIELD.SAFETY.

---

## 4. Relacja z architekturą

- Definicja FIELD.SAFETY znajduje się w:
  `ramorga-architecture/02_field_engine/field_safety_invariant.md`
- 03_field_engine jest **wykonawcą**, nie projektantem inwariantu.
- 03_field_engine musi być zgodny z:
  - `field_engine_contract.md`
  - `FieldStateManager.validate()`
  - decyzjami META_LOOP
  - inwariantami SHM i FIELD.SAFETY

---

## 5. Cel runtime mirror

Celem tego pliku jest:

- zapewnienie, że runtime engine wykonuje inwarianty pola bez ich redefiniowania,
- utrzymanie czystej separacji:
  - **architektura = definicje inwariantów**
  - **engine = wykonanie inwariantów**
- uniknięcie ukrytych warstw „safety dla LLM” w runtime.

