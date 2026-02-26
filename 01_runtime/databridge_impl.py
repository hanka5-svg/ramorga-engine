# databridge_impl.py
# RAMORGA ENGINE — 01_runtime / DataBridge

class DataBridge:

    def __init__(self, storage_backend):
        self.storage = storage_backend

    def save(self, field_state, metadata):
        if metadata.get("loopPhase") != "CONTINUE":
            raise Exception("DataBridge can only save in CONTINUE phase")

        snapshot = {
            "field_state": field_state,
            "metadata": metadata,
        }

        self.storage.write(snapshot)
