# snapshot_manager/impl.py
# Szkielet implementacji zgodny ze spec.md
# Brak logiki — tylko struktura i kontrakty.

from dataclasses import dataclass
from typing import Any, Dict


@dataclass
class Snapshot:
    """Struktura snapshotu — pełna serializacja FieldState."""
    data: Dict[str, Any]


class SnapshotManager:
    """Moduł odpowiedzialny za deterministyczną serializację i restore."""

    def __init__(self):
        pass

    def save(self, state: Any) -> Snapshot:
        """
        Serializuje pełny FieldState do struktury Snapshot.
        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("SnapshotManager.save() not implemented")

    def restore(self, snapshot: Snapshot) -> Any:
        """
        Odtwarza FieldState z Snapshot.
        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("SnapshotManager.restore() not implemented")
