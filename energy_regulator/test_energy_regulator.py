# energy_regulator/test_energy_regulator.py

from dataclasses import dataclass
from typing import Mapping

from energy_regulator.impl import EnergyRegulator, EnergyRegulatorParams


@dataclass(frozen=True)
class DummyFieldState:
    energy_map: Mapping[str, float]

    def get_energy(self) -> Mapping[str, float]:
        return self.energy_map

    def with_energy(self, new_energy: Mapping[str, float]) -> "DummyFieldState":
        # Tworzymy nową instancję – brak efektów ubocznych.
        return DummyFieldState(energy_map=dict(new_energy))


def test_energy_regulator_updates_energy_deterministically():
    regulator = EnergyRegulator()
    params = EnergyRegulatorParams(min_energy=0.0, max_energy=10.0, gain=1.0)

    state = DummyFieldState(energy_map={"a": 1.0, "b": 2.0})
    tension_map = {"a": 3.0, "b": -1.0}

    new_state = regulator.run(state, tension_map, params)

    assert new_state.energy_map == {"a": 4.0, "b": 1.0}
    # Wejściowy state nie został zmodyfikowany
    assert state.energy_map == {"a": 1.0, "b": 2.0}


def test_energy_regulator_clamps_to_min_and_max():
    regulator = EnergyRegulator()
    params = EnergyRegulatorParams(min_energy=0.0, max_energy=5.0, gain=2.0)

    state = DummyFieldState(energy_map={"low": 0.5, "high": 4.5})
    tension_map = {"low": -10.0, "high": 10.0}

    new_state = regulator.run(state, tension_map, params)

    assert new_state.energy_map["low"] == 0.0  # clamp do min
    assert new_state.energy_map["high"] == 5.0  # clamp do max


def test_energy_regulator_handles_missing_tension_keys_as_zero():
    regulator = EnergyRegulator()
    params = EnergyRegulatorParams(min_energy=0.0, max_energy=10.0, gain=1.0)

    state = DummyFieldState(energy_map={"a": 1.0, "b": 2.0})
    tension_map = {"a": 5.0}  # brak klucza "b" → traktujemy jako 0.0

    new_state = regulator.run(state, tension_map, params)

    assert new_state.energy_map["a"] == 6.0
    assert new_state.energy_map["b"] == 2.0  # bez zmian


def test_energy_regulator_is_pure_and_reproducible():
    regulator = EnergyRegulator()
    params = EnergyRegulatorParams(min_energy=0.0, max_energy=10.0, gain=0.5)

    state = DummyFieldState(energy_map={"a": 2.0})
    tension_map = {"a": 4.0}

    new_state_1 = regulator.run(state, tension_map, params)
    new_state_2 = regulator.run(state, tension_map, params)

    # Deterministyczność: te same wejścia → te same wyjścia
    assert new_state_1.energy_map == new_state_2.energy_map == {"a": 4.0}
    # Brak dryfu: wielokrotne wywołanie na tym samym wejściu nie zmienia wyniku
    assert state.energy_map == {"a": 2.0}
