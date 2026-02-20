# ritual_detector/impl.py
# Szkielet implementacji zgodny ze spec.md
# Brak logiki — tylko struktura i kontrakty.

from typing import Any, Dict, Optional


class RitualDetector:
    """
    Moduł odpowiedzialny za wykrywanie aktywacji rytuałów
    na podstawie FieldState oraz opcjonalnego EventInput.

    Wersja szkieletowa — implementacja zostanie dodana później.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------
    # Główna funkcja modułu
    # ---------------------------------------------------------

    def run(
        self,
        state: Any,
        event_input: Optional[Any],
        params: Dict[str, Any]
    ) -> Dict[str, bool]:
        """
        Analizuje stan pola i opcjonalne zdarzenia, zwracając ritual_flags.

        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("RitualDetector.run() not implemented")

    # ---------------------------------------------------------
    # Determinizm (test_mode)
    # ---------------------------------------------------------

    def enforce_determinism(self):
        """
        Wymusza deterministyczność modułu.
        Wersja szkieletowa — brak implementacji.
        """
        raise NotImplementedError("RitualDetector.enforce_determinism() not implemented")
