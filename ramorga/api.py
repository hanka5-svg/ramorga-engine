"""
RAMORGA API — Warstwa interfejsowa
----------------------------------

Minimalna implementacja API, używana przez przykłady.
Łączy się z RamorgaRuntime i udostępnia prosty interfejs.
"""

from .runtime import RamorgaRuntime


class RamorgaAPI:
    def __init__(self, runtime=None):
        if runtime is None:
            self.runtime = RamorgaRuntime()
        else:
            self.runtime = runtime

    def update(self, key, value):
        self.runtime.update(key, value)

    def consolidate(self):
        self.runtime.consolidate()

    def status(self):
        return {
            "core": self.runtime.core.invariants,
            "adaptive": self.runtime.adaptive.state,
            "memory_entries": len(self.runtime.memory.entries),
        }

    def process(self, payload: dict):
        """
        Deleguje przetwarzanie do runtime.process_step.
        Przyjmuje słownik {"input": "..."} i zwraca wynik procesu.
        """
        user_input = payload.get("input")
        if user_input is None:
            return {"error": "missing input"}
        return self.runtime.process_step(user_input)
