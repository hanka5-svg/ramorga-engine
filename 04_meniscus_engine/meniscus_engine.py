class MeniscusEngine:

    def step(self, input_payload, field_state, metadata):
        if metadata.get("loopPhase") != "REGULATE":
            raise Exception("MeniscusEngine can only run in REGULATE phase")

        # Carnival Gate
        if not field_state["carnival_completed"]:
            raise Exception("CarnivalGateViolation")

        # Glitch passthrough (no modification)
        # Topology passthrough (no modification)
        # Memory invariants (no read/write)
        # Safety invariants (detector is in runtime)

        return field_state
