"""
RAMORGA — Homeostatic Runtime Module
------------------------------------

Ten moduł udostępnia klasy RamorgaRuntime i RamorgaAPI
jako część pakietu ramorga.

Struktura zgodna z PipelineV12:
- stabilny rdzeń,
- warstwa adaptacyjna,
- API jako interfejs systemowy.
"""

from .runtime import RamorgaRuntime
from .api import RamorgaAPI

__all__ = [
    "RamorgaRuntime",
    "RamorgaAPI",
]
