# energy_regulator/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- regulację poziomu energii na podstawie napięć,
- utrzymanie energii w zakresie [E_min, E_max],
- stabilizację pola.

## Wejścia
- `energy_level`,
- `tension_map`,
- parametry regulacyjne (wzmocnienia, progi).

## Wyjścia
- zaktualizowany `energy_level`,
- `EnergyStabilityFlag`.

## Zależności
- tension_loop (dostarczane napięcia),
- field_state.

## Kontrakt wykonawczy
- energia nie może wyjść poza dopuszczalny zakres,
- deterministyczny w test_mode,
- brak efektów ubocznych.

## Powiązanie z testami
- test_regulation_step.md — poprawna regulacja energii,
- test_energy_stability.md — stabilność przy wielu krokach.
