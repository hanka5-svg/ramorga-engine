"""
Minimalny runtime Ramorga używany przez przykłady.

To jest prosta, samodzielna implementacja, która:
- inicjalizuje prosty stan,
- udostępnia update/consolidate,
- ma minimalne struktury core/adaptive/memory używane przez api.py.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List


@dataclass
class Core:
    invariants: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Adaptive:
    state: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Memory:
    entries: List[Any] = field(default_factory=list)


class RamorgaRuntime:
    def __init__(self):
        # Prosty, czytelny stan runtime
        self.core = Core(invariants={"pipeline": "PipelineV12"})
        self.adaptive = Adaptive()
        self.memory = Memory()
        # Możesz dodać tu inicjalizację loggera, konfiguracji itp.
        print(f"RAMORGA runtime initialized ({self.core.invariants.get('pipeline')})")

    def update(self, key: str, value: Any):
        """
        Aktualizuje adaptacyjny stan i dodaje wpis do pamięci.
        """
        # Aktualizacja adaptacyjnego stanu
        self.adaptive.state[key] = value
        # Dodanie do pamięci (prosty model)
        self.memory.entries.append({key: value})

    def consolidate(self):
        """
        Prosty przykład konsolidacji pamięci: usuwa duplikaty ostatnich wpisów.
        """
        seen = set()
        new_entries = []
        for e in self.memory.entries:
            # Zamieniamy na tuple by móc hashować
            t = tuple(sorted(e.items()))
            if t not in seen:
                seen.add(t)
                new_entries.append(e)
        self.memory.entries = new_entries

    # Opcjonalne: metoda process jeśli runtime ma wykonywać kroki
    def process_step(self, user_input: str) -> Dict[str, Any]:
        """
        Wykonuje pojedynczy krok przetwarzania na podstawie user_input.
        Zwraca prosty wynik używany przez przykłady.
        """
        # Przykładowe zachowanie: echo + zapis do stanu
        self.update("last_input", user_input)
        return {
            "echo": user_input,
            "adaptive_state": dict(self.adaptive.state),
            "memory_entries": len(self.memory.entries),
        }
