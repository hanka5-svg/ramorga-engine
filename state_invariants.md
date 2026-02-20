# RAMORGA‑ENGINE — State Invariants

Dokument definiuje niezmienniki stanu FieldState, które muszą być spełnione
po każdym kroku wykonania PipelineV13 oraz po każdym module regulacyjnym.

Niezmienniki są twardymi regułami systemu — naruszenie któregokolwiek
oznacza błąd implementacji.

---

# 1. Inwarianty strukturalne

## 1.1 FieldState musi mieć wszystkie pola
Po każdym kroku:

state.energy_level        != None
state.tension_map         != None
state.entropy_signature   != None
state.ritual_flags        != None

## 1.2 Typy pól są niezmienne

energy_level        → float
tension_map         → Dict[str, Any]
entropy_signature   → Dict[str, Any]
ritual_flags        → Dict[str, bool]

## 1.3 Brak ukrytych pól
FieldState nie może zawierać żadnych dodatkowych kluczy.

---

# 2. Inwarianty energetyczne

## 2.1 Energia musi być w zakresie
Po każdym module:

E_min <= energy_level <= E_max

Zakres definiowany w params.

## 2.2 Energia nie może być NaN ani Inf

not math.isnan(energy_level)
not math.isinf(energy_level)

## 2.3 Energia nie może zmieniać się skokowo bez przyczyny
Zmiana energii musi wynikać wyłącznie z energy_regulator.

---

# 3. Inwarianty napięć (tension_map)

## 3.1 tension_map musi być słownikiem

isinstance(tension_map, dict)

## 3.2 Klucze muszą być stabilne
Moduły nie mogą dodawać ani usuwać kluczy bez wyraźnego powodu.

## 3.3 Wartości muszą być liczbowe lub strukturalnie spójne
Brak None, brak typów losowych.

---

# 4. Inwarianty entropii (entropy_signature)

## 4.1 entropy_signature musi być słownikiem

isinstance(entropy_signature, dict)

## 4.2 Brak wartości None
Każda wartość musi być liczbą lub strukturą zgodną ze specyfikacją.

## 4.3 Modulacja entropii musi być deterministyczna
Dla tych samych wejść → te same wyjścia.

---

# 5. Inwarianty rytuałów (ritual_flags)

## 5.1 ritual_flags musi być słownikiem booli

all(isinstance(v, bool) for v in ritual_flags.values())

## 5.2 ritual_detector nie może modyfikować innych pól
Tylko `ritual_flags`.

---

# 6. Inwarianty snapshotów

## 6.1 Snapshot musi być pełną serializacją stanu
Żadne pole nie może być pominięte.

## 6.2 Restore musi odtwarzać stan bit‑po‑bicie

state == restore(save(state))

## 6.3 Snapshot nie może modyfikować stanu
Operacja czysto odczytowa.

---

# 7. Inwarianty wykonawcze PipelineV13

## 7.1 Kolejność modułów jest stała

tension_loop → energy_regulator → entropic_modulator → ritual_detector → snapshot?

## 7.2 Każdy moduł operuje tylko na swoich polach
- tension_loop → tylko tension_map  
- energy_regulator → tylko energy_level  
- entropic_modulator → tylko entropy_signature  
- ritual_detector → tylko ritual_flags  
- snapshot_manager → niczego nie zmienia  

## 7.3 Brak efektów ubocznych
Żaden moduł nie może modyfikować parametrów wejściowych poza swoim polem.

## 7.4 Determinizm
W trybie testowym:
- brak losowości,
- brak zależności od czasu,
- brak dryfu.

---

# 8. Inwariant globalny

**Po każdym kroku wykonania stan musi być:**

- kompletny,  
- spójny,  
- serializowalny,  
- deterministyczny,  
- zgodny z zakresem energetycznym,  
- zgodny z kontraktami danych,  
- zgodny z kolejnością modułów.

To jest fundament RAMORGA‑ENGINE.
