"""
RAMORGA API — Warstwa interfejsowa
----------------------------------

Minimalna implementacja API, używana przez przykłady.
Łączy się z RamorgaRuntime i udostępnia prosty interfejs.
"""

from .runtime import RamorgaRuntime


class RamorgaAPI:
    def __init__(self):
        self.runtime = RamorgaRuntime()

    def update(self, key, value):
        """
        Przekazuje aktualizację do runtime.
        """
        self.runtime.update(key, value)

    def consolidate(self):
        """
        Konsoliduje pamięć runtime.
        """
        self.runtime.consolidate()

    def status(self):
        """
        Zwraca prosty status systemu.
        """
        return {
            "core": self.runtime.core.invariants,
            "adaptive": self.runtime.adaptive.state,
            "memory_entries": len(self.runtime.memory.entries),
        }
