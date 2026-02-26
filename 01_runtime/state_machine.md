# state_machine.md
# RAMORGA ENGINE — 01_runtime
# ATML | MBP HAI 2.0 + patch | Continuity Model | Loop RAMORGI

## 1. Cel dokumentu
Dokument definiuje maszynę stanów runtime RAMORGI, zgodną z:

- Loop RAMORGI (OBSERVE → REGULATE → CONTINUE),
- meta‑inwariantami pola,
- integracją hooków runtime,
- pipeline_v13 jako trajektorią wykonania.

---

## 2. Stany maszyny

### 2.1. OBSERVE
- aktywne hooki: memory, topology, glitch, carnival, safety  
- brak regulacji pola  
- aktualizacja routing_counter  
- logowanie glitch  
- logowanie Carnival  

### 2.2. REGULATE
- aktywny tylko FieldEngine  
- hooki nieaktywne  
- brak operacji pamięci  
- brak logowania  

### 2.3. CONTINUE
- aktywne hooki: memory, topology, glitch, carnival, safety  
- aktualizacja routing_share  
- logowanie glitch  
- logowanie Carnival  

---

## 3. Przejścia między stanami

OBSERVE  → REGULATE   (trigger: pipeline logic completed)
REGULATE → CONTINUE   (trigger: FieldEngine.step completed)
CONTINUE → OBSERVE    (trigger: new input_payload)

---

## 4. Wymagania ATML

### 4.1. MUST
- brak operacji pamięci w REGULATE,
- brak hooków w REGULATE,
- Carnival Gate musi być sprawdzany w OBSERVE i CONTINUE,
- safetyInterrupt tylko w OBSERVE i CONTINUE.

### 4.2. MUST NOT
- brak predykcji,
- brak optymalizacji,
- brak centralizacji przepływu.

---

## 5. Integracja z pipeline_v13
- pipeline_v13.step() wywołuje przejścia stanów,
- pipeline nie może zmieniać logiki stanów,
- pipeline musi respektować aktywność hooków.

---

## 6. Status
- Maszyna stanów zsynchronizowana z runtime i pipeline_v13.
