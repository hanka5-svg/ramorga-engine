# RAMORGA‑ENGINE — Error Model

Dokument definiuje pełny model błędów RAMORGA‑ENGINE:  
- jakie błędy mogą wystąpić,  
- gdzie powstają,  
- jak są klasyfikowane,  
- jakie mają skutki,  
- jakie są zasady obsługi.

Model błędów jest deterministyczny i przewidywalny.

---

# 1. Klasy błędów

System definiuje cztery główne klasy błędów:

1. **E1 — StructuralError**  
   naruszenie struktury FieldState lub kontraktu danych

2. **E2 — InvariantError**  
   naruszenie niezmienników stanu po module lub kroku

3. **E3 — ModuleError**  
   błąd wykonania w module (logika, parametry, brak implementacji)

4. **E4 — PipelineError**  
   błąd sekwencji wykonawczej lub trybu pipeline

---

# 2. E1 — StructuralError

## Opis
Błąd struktury danych wejściowych lub wyjściowych.

## Przykłady
- brak pola w FieldState  
- pole ma zły typ  
- snapshot nie zawiera pełnej serializacji  
- merge() nadpisuje nieistniejące pola  

## Źródła
- field_state  
- snapshot_manager  
- pipeline_v13 (walidacja wejścia)

## Skutek
Natychmiastowe przerwanie wykonania.

---

# 3. E2 — InvariantError

## Opis
Naruszenie niezmienników stanu po module lub kroku.

## Przykłady
- energy_level poza zakresem  
- entropy_signature zawiera None  
- tension_map ma nieoczekiwane klucze  
- ritual_flags zawiera wartości nie-boolean  

## Źródła
- każdy moduł  
- pipeline_v13 (walidacja po kroku)

## Skutek
Przerwanie wykonania i raport diagnostyczny.

---

# 4. E3 — ModuleError

## Opis
Błąd wykonania w module — logiczny, parametryczny lub implementacyjny.

## Przykłady
- NotImplementedError (szkielet)  
- nieprawidłowe params  
- dzielenie przez zero  
- brak deterministyczności w test_mode  

## Źródła
- tension_loop  
- energy_regulator  
- entropic_modulator  
- ritual_detector  
- snapshot_manager  

## Skutek
Przerwanie wykonania modułu, pipeline przechwytuje i raportuje.

---

# 5. E4 — PipelineError

## Opis
Błąd sekwencji wykonawczej lub trybu pipeline.

## Przykłady
- nieznany `mode`  
- steps < 1  
- state=None w trybie innym niż init  
- moduł zwrócił niepoprawne dane  

## Źródła
- pipeline_v13

## Skutek
Natychmiastowe przerwanie wykonania.

---

# 6. Mapa błędów do modułów

| Moduł             | E1 | E2 | E3 | E4 |
|-------------------|----|----|----|----|
| field_state       | ✔️ | ✔️ | ✔️ | —  |
| tension_loop      | —  | ✔️ | ✔️ | —  |
| energy_regulator  | —  | ✔️ | ✔️ | —  |
| entropic_modulator| —  | ✔️ | ✔️ | —  |
| ritual_detector   | —  | ✔️ | ✔️ | —  |
| snapshot_manager  | ✔️ | —  | ✔️ | —  |
| pipeline_v13      | ✔️ | ✔️ | ✔️ | ✔️ |

---

# 7. Zasady obsługi błędów

## 7.1 Brak automatycznej naprawy
System nie próbuje „naprawiać” stanu.  
Każde naruszenie → błąd.

## 7.2 Deterministyczne wyjątki
Każdy błąd musi być jednoznaczny i powtarzalny.

## 7.3 Zero ukrywania błędów
Pipeline nie maskuje błędów modułów.

## 7.4 Snapshoty nie łapią błędów
SnapshotManager nie przechwytuje wyjątków — tylko serializuje.

---

# 8. Przepływ błędów

module_error
↓
pipeline_v13
↓
walidacja niezmienników
↓
raport błędu
↓
przerwanie wykonania

---

# 9. Podsumowanie

`error_model.md` definiuje pełną semantykę błędów RAMORGA‑ENGINE:  
klasy, źródła, skutki, zasady obsługi i deterministyczny przepływ wyjątków.  
Dokument jest fundamentem implementacji i testów.
