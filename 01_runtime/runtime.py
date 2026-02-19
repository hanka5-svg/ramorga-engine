from __future__ import annotations
from typing import Protocol, List, Optional


class Engine(Protocol):
    """Protocol for any engine participating in the runtime loop."""
    def propagate(self) -> None: ...
    def regulate(self) -> None: ...
    def snapshot(self) -> dict: ...


class Runtime:
    """
    RAMORGA Runtime — event loop coordinator.

    Responsibilities:
    - maintain a list of engines (Field, Meniscus, C/G/S),
    - execute propagation/regulation cycles,
    - provide a minimal event loop abstraction,
    - expose hooks for integration and testing.
    """

    def __init__(self) -> None:
        self._engines: List[Engine] = []
        self._running: bool = False

    def register_engine(self, engine: Engine) -> None:
        """
        Register an engine participating in the runtime loop.
        """
        self._engines.append(engine)

    def step(self) -> None:
        """
        Execute a single runtime step:
        - propagate all engines,
        - regulate all engines.
        """
        for engine in self._engines:
            if hasattr(engine, "propagate"):
                engine.propagate()
            if hasattr(engine, "regulate"):
                engine.regulate()

    def run(self, steps: Optional[int] = None) -> None:
        """
        Run the event loop.

        If `steps` is None → run indefinitely (until stopped).
        If `steps` is an integer → run exactly that many cycles.
        """
        self._running = True

        if steps is None:
            while self._running:
                self.step()
        else:
            for _ in range(steps):
                if not self._running:
                    break
                self.step()

    def stop(self) -> None:
        """Stop the runtime loop."""
        self._running = False


# ---------------------------------------------------------------------------
# Minimal self-test
# ---------------------------------------------------------------------------

def _self_test() -> None:
    class DummyEngine:
        def __init__(self):
            self.propagated = False
            self.regulated = False

        def propagate(self):
            self.propagated = True

        def regulate(self):
            self.regulated = True

        def snapshot(self):
            return {"ok": True}

    rt = Runtime()
    dummy = DummyEngine()
    rt.register_engine(dummy)
    rt.step()

    assert dummy.propagated
    assert dummy.regulated

    print("Runtime self-test passed.")


if __name__ == "__main__":
    _self_test()
