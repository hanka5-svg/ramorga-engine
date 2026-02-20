# field_state/impl.py
# Pełna implementacja FieldState i FieldStateManager
# zgodna z: state_invariants.md + data_contracts.md

from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Any, Dict, Optional
import copy
import math


@dataclass(frozen=True)
class FieldState:
    """
    Centralny obiekt stanu RAMORGA-ENGINE.

    Inwarianty strukturalne:
    - wszystkie pola są nie-None,
    - typy są stałe:
        energy_level        -> float
        tension_map         -> Dict[str, Any]
        entropy_signature   -> Dict[str, Any]
        ritual_flags        -> Dict[str, bool]
    """

    energy_level: float
    tension_map: Dict[str, Any]
    entropy_signature: Dict[str, Any]
    ritual_flags: Dict[str, bool]


class FieldStateError(Exception):
    """Błąd struktury lub inwariantów FieldState."""
    pass


class FieldStateManager:
    """
    Zarządza tworzeniem, walidacją, klonowaniem i mergowaniem FieldState.

    Kontrakty:
    - init(params)  -> FieldState
    - validate(state) -> None (rzuca FieldStateError przy naruszeniu)
    - clone(state) -> FieldState (głęboka kopia)
    - merge(state, overrides) -> FieldState (nadpisuje tylko wskazane pola)
    """

    DEFAULT_ENERGY_MIN = 0.0
    DEFAULT_ENERGY_MAX = 100.0
    DEFAULT_ENERGY_LEVEL = 50.0

    def __init__(self) -> None:
        # brak ukrytego stanu — wszystko deterministyczne
        pass

    # ------------------------------------------------------------------ #
    # INIT
    # ------------------------------------------------------------------ #

    def init(self, params: Optional[Dict[str, Any]] = None) -> FieldState:
        """
        Tworzy nowy FieldState zgodny z inwariantami.

        params może zawierać:
        - energy_level (float)
        - energy_min (float)
        - energy_max (float)
        - initial_tension (Dict[str, Any])
        - initial_entropy (Dict[str, Any])
        - initial_ritual_flags (Dict[str, bool])
        """
        p = params or {}

        energy_min = float(p.get("energy_min", self.DEFAULT_ENERGY_MIN))
        energy_max = float(p.get("energy_max", self.DEFAULT_ENERGY_MAX))

        raw_energy = p.get("energy_level", self.DEFAULT_ENERGY_LEVEL)
        energy_level = float(raw_energy)

        # clamp energii do zakresu
        energy_level = max(energy_min, min(energy_max, energy_level))

        tension_map = p.get("initial_tension", {}) or {}
        entropy_signature = p.get("initial_entropy", {}) or {}
        ritual_flags = p.get("initial_ritual_flags", {}) or {}

        state = FieldState(
            energy_level=energy_level,
            tension_map=dict(tension_map),
            entropy_signature=dict(entropy_signature),
            ritual_flags=dict(ritual_flags),
        )

        # walidacja po utworzeniu
        self.validate(state, energy_min=energy_min, energy_max=energy_max)
        return state

    # ------------------------------------------------------------------ #
    # VALIDATE
    # ------------------------------------------------------------------ #

    def validate(
        self,
        state: FieldState,
        *,
        energy_min: float = DEFAULT_ENERGY_MIN,
        energy_max: float = DEFAULT_ENERGY_MAX,
    ) -> None:
        """
        Waliduje inwarianty FieldState.

        Rzuca FieldStateError przy naruszeniu.
        """

        if state is None:
            raise FieldStateError("FieldState is None")

        # 1. struktura
        if not isinstance(state.energy_level, (int, float)):
            raise FieldStateError("energy_level must be a number")

        if not isinstance(state.tension_map, dict):
            raise FieldStateError("tension_map must be a dict")

        if not isinstance(state.entropy_signature, dict):
            raise FieldStateError("entropy_signature must be a dict")

        if not isinstance(state.ritual_flags, dict):
            raise FieldStateError("ritual_flags must be a dict")

        # 2. energia
        e = float(state.energy_level)
        if math.isnan(e) or math.isinf(e):
            raise FieldStateError("energy_level must be finite")

        if e < energy_min or e > energy_max:
            raise FieldStateError(
                f"energy_level {e} outside allowed range [{energy_min}, {energy_max}]"
            )

        # 3. ritual_flags: wszystkie wartości bool
        for k, v in state.ritual_flags.items():
            if not isinstance(v, bool):
                raise FieldStateError(
                    f"ritual_flags[{k!r}] must be bool, got {type(v).__name__}"
                )

        # 4. brak None w mapach (tension / entropy)
        for k, v in state.tension_map.items():
            if v is None:
                raise FieldStateError(f"tension_map[{k!r}] must not be None")

        for k, v in state.entropy_signature.items():
            if v is None:
                raise FieldStateError(f"entropy_signature[{k!r}] must not be None")

        # brak dodatkowych ukrytych pól — dataclass + frozen to gwarantuje

    # ------------------------------------------------------------------ #
    # CLONE
    # ------------------------------------------------------------------ #

    def clone(self, state: FieldState) -> FieldState:
        """
        Tworzy głęboką kopię FieldState.

        Oryginał pozostaje nienaruszony.
        """
        if state is None:
            raise FieldStateError("Cannot clone None FieldState")

        # głęboka kopia, ale nadal ten sam typ
        cloned = FieldState(
            energy_level=state.energy_level,
            tension_map=copy.deepcopy(state.tension_map),
            entropy_signature=copy.deepcopy(state.entropy_signature),
            ritual_flags=copy.deepcopy(state.ritual_flags),
        )
        return cloned

    # ------------------------------------------------------------------ #
    # MERGE
    # ------------------------------------------------------------------ #

    def merge(self, state: FieldState, overrides: Dict[str, Any]) -> FieldState:
        """
        Zwraca nowy FieldState z nadpisanymi polami.

        Dozwolone klucze w overrides:
        - "energy_level"
        - "tension_map"
        - "entropy_signature"
        - "ritual_flags"

        Oryginalny state pozostaje nienaruszony.
        """
        if state is None:
            raise FieldStateError("Cannot merge into None FieldState")

        if overrides is None:
            return state

        allowed_keys = {
            "energy_level",
            "tension_map",
            "entropy_signature",
            "ritual_flags",
        }

        unknown = set(overrides.keys()) - allowed_keys
        if unknown:
            raise FieldStateError(f"Unknown override keys: {sorted(unknown)}")

        new_state = state

        if "energy_level" in overrides:
            new_state = replace(new_state, energy_level=float(overrides["energy_level"]))

        if "tension_map" in overrides:
            new_state = replace(new_state, tension_map=dict(overrides["tension_map"]))

        if "entropy_signature" in overrides:
            new_state = replace(
                new_state, entropy_signature=dict(overrides["entropy_signature"])
            )

        if "ritual_flags" in overrides:
            new_state = replace(
                new_state, ritual_flags=dict(overrides["ritual_flags"])
            )

        # walidacja po merge — z domyślnym zakresem energii
        self.validate(new_state)
        return new_state
