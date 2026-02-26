# runtime_contract.md
# RAMORGA ENGINE — Runtime Contract

## 1. Rola runtime
Runtime RAMORGI egzekwuje meta‑inwarianty pola i prowadzi pętlę wykonawczą:
OBSERVE → REGULATE → CONTINUE.

## 2. Interfejs
Runtime nie posiada pojedynczej funkcji wejściowej — jest zbiorem hooków i
regulatorów wywoływanych przez pipeline_v13.

## 3. Fazy

### OBSERVE
MUST:
- logować glitch, routing, carnival, memory
- nie modyfikować pola

MUST NOT:
- regulować pola
- wykonywać predykcji lub optymalizacji

### REGULATE
MUST:
- wywołać MeniscusEngine
- wywołać FieldEngine

MUST NOT:
- wykonywać hooków
- dotykać pamięci

### CONTINUE
MUST:
- wykonać hooki
- zapisać snapshot przez DataBridge

MUST NOT:
- regulować pola

## 4. Inwarianty
Runtime egzekwuje:
- FIELD.MEMORY.001
- FIELD.TOPOLOGY.001
- FIELD.GLITCH.001
- FIELD.RELATION.001
- FIELD.SAFETY.001
