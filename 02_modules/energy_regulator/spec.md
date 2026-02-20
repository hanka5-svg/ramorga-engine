# energy_regulator/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- stabilizację energii pola,
- kompensację skoków energii,
- utrzymanie homeostazy energetycznej.

## Wejścia
- `FieldState`
- `TensionDelta`

## Wyjścia
- `EnergyAdjustment`
- `EnergyStabilityFlag` (np. STABLE / OVERLOADED / DEPLETED)

## Zależności
- logiczne: field_state, tension_loop
- współpraca z field_state przy aktualizacji stanu

## Testy (powiązanie)
- test_energy_stability.md → stabilność energii przy różnych TensionDelta
- test_regulation_step.md → poprawne sprzężenie z tension_loop
