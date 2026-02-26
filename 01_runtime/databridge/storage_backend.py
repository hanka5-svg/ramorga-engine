# storage_backend.py
# RAMORGA ENGINE — 01_runtime/databridge
# Minimalny backend zapisu snapshotów dla DataBridge

import json
from pathlib import Path


class FileStorageBackend:
    """
    Minimalny backend zapisu snapshotów.
    Zgodny z meta‑inwariantami pola:
    - brak optymalizacji
    - brak predykcji
    - brak filtracji treści
    - brak modyfikacji field_state
    """

    def __init__(self, base_dir: str = "snapshots"):
        self.base = Path(base_dir)
        self.base.mkdir(parents=True, exist_ok=True)

    def write(self, snapshot: dict) -> None:
        """
        Zapisuje snapshot jako plik JSON.
        Nazwa pliku deterministyczna: snapshot_N.json
        """
        if not isinstance(snapshot, dict):
            raise ValueError("Snapshot must be a dict")

        # znajdź kolejny numer pliku
        existing = list(self.base.glob("snapshot_*.json"))
        next_id = len(existing) + 1

        path = self.base / f"snapshot_{next_id}.json"

        with path.open("w", encoding="utf-8") as f:
            json.dump(snapshot, f, indent=2, ensure_ascii=False)
