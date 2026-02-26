from pipeline_v13.impl import PipelineV13

def test_databridge_saves_in_continue(field_state, metadata_continue, tmp_path):
    pipeline = PipelineV13()
    # podmieniamy backend na testowy
    class TestStorage:
        def __init__(self):
            self.saved = []

        def write(self, snapshot):
            self.saved.append(snapshot)

    storage = TestStorage()
    pipeline.data_bridge.storage = storage

    pipeline.step("input", field_state, metadata_continue)

    assert len(storage.saved) == 1
    assert "field_state" in storage.saved[0]
