from __future__ import annotations
from typing import Any, Dict, Optional


class FieldState:
    """
    FieldState
    ----------
    Minimal container for field-level data used by FieldEngine.

    This structure mirrors the architecture defined in:
    - ramorga-architecture/02_field_engine/02.90-symbiosis-health-metric.md
    - ramorga-architecture/02_field_engine/META_LOOP.md

    Responsibilities:
    - store raw field input,
    - store SHM-computed metrics,
    - store META_LOOP feedback,
    - update state based on physics backend (FieldEnginePhysics).
    """

    def __init__(
        self,
        raw: Optional[Any] = None,
        shm_state: Optional[Dict[str, Any]] = None,
        loop_feedback: Optional[Dict[str, Any]] = None,
    ) -> None:
        self.raw = raw
        self.shm_state = shm_state or {}
        self.loop_feedback = loop_feedback or {}

    # ------------------------------------------------------------------

    def update_from_positions(self, positions: Dict[str, Any]) -> None:
        """
        Update the field state using node positions from FieldEnginePhysics.

        This method is intentionally minimal — the architecture layer
        defines how positions influence SHM and META_LOOP.
        """
        self.raw = positions

    # ------------------------------------------------------------------

    def snapshot(self) -> Dict[str, Any]:
        """
        Return a serializable snapshot of the current field state.
        Useful for debugging, observability and tests.
        """
        return {
            "raw": self.raw,
            "shm_state": self.shm_state,
            "loop_feedback": self.loop_feedback,
        }

    # ------------------------------------------------------------------

    def __repr__(self) -> str:
        return (
            f"FieldState(raw={self.raw}, "
            f"shm_state={self.shm_state}, "
            f"loop_feedback={self.loop_feedback})"
        )
