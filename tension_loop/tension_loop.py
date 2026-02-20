from .entropic_modulator import EntropicModulator, EntropicConfig


class TensionLoop:
    def __init__(self, field, entropic_config: EntropicConfig | None = None) -> None:
        self.field = field
        self.entropic = EntropicModulator(entropic_config)

    def step(self) -> dict:
        """
        One full tension step:
        - update field dynamics
        - regulate entropy
        """
        field_state = self.field.step()
        entropic_state = self.entropic.step(self.field)

        return {
            "field": field_state,
            "entropy": entropic_state,
        }
