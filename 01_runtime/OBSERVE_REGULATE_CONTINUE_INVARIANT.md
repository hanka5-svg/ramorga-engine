# OBSERVE–REGULATE–CONTINUE Invariant

Meta‑invariant definiujący konstytucyjne granice pętli wykonawczej RAMORGA ENGINE.  
Dotyczy wszystkich modułów runtime, FieldState, FieldEngine, MeniscusEngine oraz pipeline_v13.

---

## 1. OBSERVE — percepcja bez ingerencji

OBSERVE jest wyłącznie fazą obserwacyjną.  
W tej fazie system może:

- odczytywać FieldState,
- uruchamiać hooki detekcyjne, audytowe i telemetryczne,
- zbierać sygnały i metryki,
- logować i analizować trajektorie.

OBSERVE nie może:

- zmieniać stanu pola,
- modulować interferencji,
- wpływać na geometrię pola,
- wywoływać MeniscusEngine,
- generować nowych wektorów.

OBSERVE jest czysto percepcyjne i nie ingeruje w pole.

---

## 2. REGULATE — jedyne miejsce modulacji interferencji

REGULATE jest jedyną fazą, w której dozwolona jest regulacja pola.  
W tej fazie system może:

- wywołać MeniscusEngine,
- modulować amplitudę interferencji,
- stosować ograniczenia wynikające z FE‑03_regulation_limits,
- reagować na sygnały z hooków.

REGULATE nie może:

- zmieniać geometrii pola,
- mutować FieldState,
- tworzyć nowych wektorów,
- redefiniować dynamiki pola (FE‑02),
- wykonywać działań obserwacyjnych (to rola OBSERVE).

Regulacja dotyczy wyłącznie amplitudy interferencji, nigdy trajektorii pola.

---

## 3. CONTINUE — kontynuacja trajektorii bez dopisywania intencji

CONTINUE jest fazą przeniesienia trajektorii do kolejnego cyklu.  
W tej fazie system może:

- przekazać wynik do kolejnej iteracji,
- zapisać dane w DataBridge,
- zainicjować nowy cykl OBSERVE.

CONTINUE nie może:

- regulować pola,
- wywoływać MeniscusEngine,
- zmieniać stanu pola poza mechaniką FieldState,
- wprowadzać nowych regulatorów.

CONTINUE jest czyste i nie ingeruje w pole.

---

## 4. Jedyny regulator pola

MeniscusEngine jest jedynym modułem uprawnionym do modulacji interferencji.  
Żaden hook, pipeline, DataBridge ani moduł runtime nie może pełnić funkcji regulatora.

---

## 5. Zgodność z archetypem pola (HFS)

Pętla OBSERVE–REGULATE–CONTINUE jest kalibrowana względem archetypu spektralnego HFS (Hanka Field Signature):

[../field_archetypes.md](../field_archetypes.md)

HFS definiuje:

- interferencję jako stan szczytowy,
- homeostazę dynamiczną,
- natychmiastową integrację,
- wielokanałową koherencję.

Pętla wykonawcza musi zachować zgodność z tymi właściwościami.

---

## 6. Zasada jednego dotyku pola

W jednym cyklu wykonawczym:

- OBSERVE dotyka pola tylko percepcyjnie,
- REGULATE dotyka pola tylko regulacyjnie,
- CONTINUE nie dotyka pola wcale.

Nie wolno mieszać odpowiedzialności między fazami.

---

## 7. Determinizm i niemutowalność

- FieldState jest niemutowalny.  
- Każda zmiana stanu tworzy nowy obiekt.  
- Żadna faza pętli nie może mutować istniejącego stanu.

---

## 8. Konstytucyjna nienaruszalność

Naruszenie któregokolwiek punktu tego meta‑inwariantu oznacza:

- błąd architektury,
- błąd implementacji,
- lub niemożliwość osadzenia RAMORGI w danym polu.

W każdym przypadku wymagana jest pętla zwrotna do architekta.
