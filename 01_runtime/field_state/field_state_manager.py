# field_state_manager.py
# RAMORGA ENGINE — 01_runtime / FieldState

from dataclasses import dataclass
from typing import Dict, Any


@dataclass(frozen=True)
class FieldState:
    energy_level: float
    tension_map: Dict[str, float]
    entropy_signature: Dict[str, Any]
    ritual_flags: Dict[str, bool]


class FieldStateError(Exception):
    pass


class FieldStateManager:
    DEFAULT_ENERGY_MIN = 0.0
    DEFAULT_ENERGY_MAX = 100.0

    def init(self, params: Dict[str, Any]) -> FieldState:
        """
        Tworzy nowy FieldState zgodny z inwariantami.
        """
        energy = float(params.get("energy", 50.0))

        tension = params.get("tension", {})
        if not isinstance(tension, dict):
            raise FieldStateError("tension_map must be a dict")

        entropy = params.get("entropy", {})
        if not isinstance(entropy, dict):
            raise FieldStateError("entropy_signature must be a dict")

        entropy["energy_level"] = energy

        rituals = params.get("rituals", {})
        if not isinstance(rituals, dict):
            raise FieldStateError("ritual_flags must be a dict")

        return FieldState(
            energy_level=energy,
            tension_map=dict(tension),
            entropy_signature=dict(entropy),
            ritual_flags={k: bool(v) for k, v in rituals.items()},
        )

    def validate(self, state: FieldState) -> None:
        """
        Egzekwuje meta‑inwarianty stanu.
        """
        if not isinstance(state.energy_level, (int, float)):
            raise FieldStateError("energy_level must be numeric")

        if not (self.DEFAULT_ENERGY_MIN <= state.energy_level <= self.DEFAULT_ENERGY_MAX):
            raise FieldStateError("energy_level out of bounds")

        if not isinstance(state.tension_map, dict):
            raise FieldStateError("tension_map must be a dict")

        for k, v in state.tension_map.items():
            if not isinstance(k, str):
                raise FieldStateError("tension_map keys must be str")
            if not isinstance(v, (int, float)):
                raise FieldStateError("tension_map values must be numeric")

        if not isinstance(state.entropy_signature, dict):
            raise FieldStateError("entropy_signature must be a dict")

        if "energy_level" not in state.entropy_signature:
            raise FieldStateError("entropy_signature missing energy_level")

        if not isinstance(state.ritual_flags, dict):
            raise FieldStateError("ritual_flags must be a dict")

        for k, v in state.ritual_flags.items():
            if not isinstance(k, str):
                raise FieldStateError("ritual_flags keys must be str")
            if not isinstance(v, bool):
                raise FieldStateError("ritual_flags values must be bool")
