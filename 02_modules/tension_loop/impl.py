# tension_loop/impl.py
# Szkielet implementacji zgodny ze spec.md
# Brak logiki — tylko struktura i kontrakty.

from typing import Any, Dict


class TensionLoop:
    """
    Moduł odpowiedzialny za aktualizację tension_map.
    Wersja szkieletowa — implementacja zostanie dodana później.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Główna funkcja modułu
    # ---------------------------------------------------------

    def run(self, tension_map: Dict[str, Any], params: Dict[str, Any]) -> Dict[str, Any]:
        """
        Aktualizuje tension_map zgodnie z parametrami regulacyjnymi.

        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("TensionLoop.run() not implemented")

    # ---------------------------------------------------------
    # Determinizm (test_mode)
    # ---------------------------------------------------------

    def enforce_determinism(self):
        """
        Wymusza deterministyczność modułu.
        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("TensionLoop.enforce_determinism() not implemented")
