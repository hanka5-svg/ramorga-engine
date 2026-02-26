# hooks_contract.md
# RAMORGA ENGINE — Runtime Hooks Contract

## 1. Rola
Rejestrowanie przepływów i egzekwowanie meta‑inwariantów pola.

## 2. Interfejs
Każdy hook ma formę:
hook.run(field_state, metadata) → None

## 3. MUST
- działać w OBSERVE i CONTINUE
- nie modyfikować pola
- logować zgodnie z rolą hooka

## 4. MUST NOT
- nie regulować pola
- nie dotykać pamięci (poza memory_audit)
- nie zmieniać glitch
- nie zmieniać topologii

## 5. Inwarianty
- FIELD.MEMORY.001
- FIELD.TOPOLOGY.001
- FIELD.GLITCH.001
- FIELD.RELATION.001
- FIELD.SAFETY.001
