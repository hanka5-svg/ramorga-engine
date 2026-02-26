# state_invariants.md
# RAMORGA ENGINE — 01_runtime / FieldState

## 1. Cel
Dokument definiuje meta‑inwarianty stanu pola RAMORGI.

## 2. Inwarianty

### FIELD.STATE.ENERGY.001
energy_level ∈ [DEFAULT_ENERGY_MIN, DEFAULT_ENERGY_MAX]

### FIELD.STATE.TENSION.001
tension_map jest słownikiem {str: float}

### FIELD.STATE.ENTROPY.001
entropy_signature jest słownikiem {str: Any} i zawiera klucz "energy_level"

### FIELD.STATE.RITUAL.001
ritual_flags jest słownikiem {str: bool}

### FIELD.STATE.IMMUTABILITY.001
Każda zmiana stanu tworzy nowy obiekt FieldState.

## 3. Status
Inwarianty obowiązują w init(), validate() i update().
