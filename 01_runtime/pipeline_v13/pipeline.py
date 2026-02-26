# --- REGULATE PHASE ---
metadata["loopPhase"] = "REGULATE"

# MeniscusEngine
field_state = self.meniscus.step(input_payload, field_state, metadata)

# FieldEngine
field_state = self.field_engine.step(field_state)
