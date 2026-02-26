def test_pipeline_calls_meniscus_before_field(field_state, metadata_regulate):
    pipeline = PipelineV13()
    pipeline.meniscus = MeniscusEngine()
    pipeline.field_engine = FieldEngine()

    out = pipeline.step("input", field_state, metadata_regulate)

    assert out is not None
