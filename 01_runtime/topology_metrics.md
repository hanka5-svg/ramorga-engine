# topology_metrics.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel modułu
Moduł topology_metrics odpowiada za egzekwowanie meta‑inwariantu
FIELD.TOPOLOGY.001 — „Brak emergentnego centrum”.

Celem modułu jest:
- monitorowanie udziału ruchu (routingShare) dla każdego modułu,
- wykrywanie topologicznej centralizacji,
- generowanie alertów diagnostycznych (bez działań optymalizacyjnych),
- utrzymanie topologii zgodnej z zasadą braku hierarchii.

---

## 2. Zakres odpowiedzialności
### 2.1. Odpowiedzialności
- zbieranie metryk przepływu sygnału,
- aktualizacja routingShare w field_state,
- wykrywanie przekroczenia progu centralizacji,
- generowanie topologyAlert.

### 2.2. Zakres niedozwolony
Moduł **NIE może**:
- zmieniać topologii,
- optymalizować przepływu,
- wymuszać trasowania,
- podejmować decyzji wykonawczych,
- ingerować w regulację pola.

---

## 3. Interfejs
### 3.1. Funkcje eksportowane

topology_metrics.register_flow(module_id, metadata) → None
topology_metrics.compute_share(field_state) → dict
topology_metrics.check_threshold(field_state) → bool
topology_metrics.emit_alert(module_id, share) → None

### 3.2. Parametry
- `module_id` — identyfikator modułu wykonującego operację,
- `metadata` — struktura ATML zawierająca:
  - request_id,
  - cycle_id,
  - loopPhase,
  - timestamp.

---

## 4. Struktura danych
### 4.1. routingShare (ATML)

field_state.routing_share = {
module_id: float  # udział procentowy ruchu
}

### 4.2. routingCounter (wewnętrzne)

routingCounter = {
module_id: int  # liczba operacji
}

---

## 5. Wymagania ATML
### 5.1. Wymagania MUST
- każdy przepływ sygnału MUSI zostać zarejestrowany,
- routingShare MUSI być aktualizowany w każdej iteracji pętli,
- przekroczenie progu MUSI generować topologyAlert,
- moduł MUSI działać w fazach OBSERVE i CONTINUE.

### 5.2. Wymagania MUST NOT
- moduł NIE może zmieniać trasowania,
- moduł NIE może optymalizować przepływu,
- moduł NIE może agregować danych w sposób umożliwiający predykcję.

---

## 6. Progi diagnostyczne
### 6.1. Wartość domyślna

TOPOLOGY_THRESHOLD = 0.35  # 35% udziału ruchu

### 6.2. Interpretacja
- share ≤ threshold → topologia stabilna,
- share > threshold → potencjalne emergentne centrum.

---

## 7. Alert topologiczny
### 7.1. Struktura alertu

TopologyAlert = {
"event_id": UUID,
"timestamp": int,
"module_id": str,
"share": float,
"threshold": float,
"request_id": str,
"cycle_id": str
}

### 7.2. Reakcja
- zapis alertu do field_state.topology_log,
- brak działań wykonawczych,
- brak optymalizacji.

---

## 8. Integracja z Loop RAMORGI
### 8.1. Fazy pętli
- OBSERVE — aktywny,
- REGULATE — nieaktywny,
- CONTINUE — aktywny.

### 8.2. Wymagania
- rejestracja przepływu tylko w OBSERVE i CONTINUE,
- brak operacji w REGULATE.

---

## 9. Testy wymagane
- test_topology_register_flow,
- test_topology_compute_share,
- test_topology_threshold_detection,
- test_topology_alert_logging,
- test_topology_no_optimisation.

---

## 10. Status implementacji
- Moduł: nowy plik,
- Integracja z pipeline_v13: wymagana,
- Integracja z FieldEngine: diagnostyczna,
- Testy: wymagane.

---

Koniec pliku.
