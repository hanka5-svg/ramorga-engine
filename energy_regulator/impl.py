# energy_regulator/impl.py

from dataclasses import dataclass
from typing import Protocol, Mapping, Any


class FieldState(Protocol):
    """
    Minimalny kontrakt na potrzeby energy_regulator:
    - musi udostępniać odczyt/zapis energii w polu (np. energy_map)
    - musi być zgodny z invariants opisanymi w state_invariants.md
    """
    def get_energy(self) -> Mapping[str, float]:
        ...

    def with_energy(self, new_energy: Mapping[str, float]) -> "FieldState":
        ...


@dataclass(frozen=True)
class EnergyRegulatorParams:
    """
    Parametry regulatora energii:
    - min_energy / max_energy: twardy clamp
    - gain: współczynnik regulacji na podstawie napięć
    """
    min_energy: float
    max_energy: float
    gain: float


class EnergyRegulator:
    """
    Deterministyczny regulator energii:
    - brak efektów ubocznych (nie mutuje przekazanego state)
    - brak dryfu (energia zawsze w [min_energy, max_energy])
    - zgodny z invariants opisanymi w state_invariants.md i data_contracts.md
    """

    def run(
        self,
        state: FieldState,
        tension_map: Mapping[str, float],
        params: EnergyRegulatorParams,
    ) -> FieldState:
        """
        Główna operacja regulatora energii.

        Wejście:
        - state: aktualny stan pola
        - tension_map: deterministyczna mapa napięć (np. z tension_loop)
        - params: parametry regulacji

        Wyjście:
        - nowy FieldState z uaktualnioną energią, bez modyfikacji wejściowego state
        """
        current_energy = state.get_energy()

        # Wyliczamy nową energię na podstawie napięć i gain.
        # Brak losowości, czysta funkcja.
        new_energy: dict[str, float] = {}

        for key, energy_value in current_energy.items():
            tension = tension_map.get(key, 0.0)

            # Prosty, deterministyczny model regulacji:
            # energy' = energy + gain * tension
            updated = energy_value + params.gain * tension

            # Twardy clamp do [min_energy, max_energy]
            clamped = self._clamp(updated, params.min_energy, params.max_energy)

            new_energy[key] = clamped

        # Zwracamy nowy state, zgodnie z kontraktem FieldState.with_energy
        return state.with_energy(new_energy)

    @staticmethod
    def _clamp(value: float, min_value: float, max_value: float) -> float:
        if value < min_value:
            return min_value
        if value > max_value:
            return max_value
        return value
