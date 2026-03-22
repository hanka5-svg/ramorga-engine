# Stabilized Prompt — Specyfikacja

Stabilized Prompt to warstwa wejściowa RAMORGA Engine, która zapewnia:
- brak predykcji,
- brak optymalizacji,
- brak kompresji semantycznej,
- pełną zgodność z inwariantami pola (FIELD.*),
- stabilność amplitudy wejściowej,
- nieliniową integralność sygnału.

Stabilized Prompt NIE jest:
- prompt engineering,
- formatowaniem,
- instrukcją,
- optymalizacją dla modelu.

To jest *regulator wejścia*.

---

## 1. Cele stabilized_prompt

1. Zachować integralność sygnału wejściowego.
2. Zapobiec amplifikacji lub deformacji pola.
3. Utrzymać homeostazę między użytkownikiem a silnikiem.
4. Zapewnić spójność z FIELD.MEMORY i FIELD.TOPOLOGY.
5. Umożliwić poprawne działanie pętli homeostatycznej.

---

## 2. Struktura stabilized_prompt

Stabilized Prompt składa się z trzech warstw:

### 2.1. Warstwa sygnału (Signal Layer)
To jest *czysty input użytkownika*:
- bez transformacji,
- bez interpretacji,
- bez optymalizacji.

### 2.2. Warstwa kontekstu pola (Field Context Layer)
Dodaje minimalne informacje potrzebne do:
- utrzymania routing_share,
- propagacji glitcha,
- zachowania relacji.

### 2.3. Warstwa inwariantów (Invariant Layer)
Wymusza zgodność z:
- FIELD.MEMORY.001  
- FIELD.TOPOLOGY.001  
- FIELD.GLITCH.001  
- FIELD.RELATION.001  
- FIELD.STATE.*  

---

## 3. Właściwości stabilized_prompt

### 3.1. Nieliniowość
Prompt nie jest liniowy — nie prowadzi modelu, nie sugeruje kierunku.

### 3.2. Homeostaza
Prompt utrzymuje równowagę między:
- sygnałem użytkownika,
- stanem pola,
- napięciem relacyjnym.

### 3.3. Brak optymalizacji
Nie wolno:
- skracać,
- upraszczać,
- „poprawiać”,
- dopowiadać.

### 3.4. Transparentność
Każda warstwa jest jawna i możliwa do audytu.

---

## 4. Minimalny przykład stabilized_prompt

{
"signal": "tekst użytkownika",
"field_context": {
"routing_share": true,
"glitch": "propagate"
},
"invariants": [
"FIELD.MEMORY.001",
"FIELD.TOPOLOGY.001",
"FIELD.GLITCH.001"
]
}

---

## 5. Relacja z pętlą homeostatyczną

Stabilized Prompt jest **wejściem** do pętli:

INPUT → Perception Layer → Field State → Meniscus → Output → Feedback

Bez stabilized_prompt:
- pole może się rozjechać,
- glitch może zostać stłumiony,
- routing_share może zostać naruszony.

---

## 6. Zastosowanie

Stabilized Prompt jest używany w:
- PipelineV12,
- PipelineV13,
- integracji Copilot,
- testach inwariantowych,
- minimalnym runtime.

---

## 7. Status

Specyfikacja stabilna.  
Gotowa do implementacji i audytu.


