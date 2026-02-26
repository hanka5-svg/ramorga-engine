# meniscus_engine.py
# RAMORGA ENGINE — 04_meniscus_engine

class MeniscusEngine:

    def __init__(self):
        pass

    def step(self, input_payload, field_state, metadata):
        phase = metadata.get("loopPhase")

        if phase != "REGULATE":
            raise Exception("MeniscusEngine can only run in REGULATE phase")

        # 1. Carnival Gate
        if not field_state["carnival_completed"]:
            raise Exception("CarnivalGateViolation")

        # 2. Glitch passthrough
        # (MeniscusEngine does not modify glitch)

        # 3. Topology invariants
        # (MeniscusEngine does not modify routing_share or routing_counter)

        # 4. Safety invariants
        # (MeniscusEngine does not detect crime — detector is in runtime)

        # 5. Memory invariants
        # (MeniscusEngine does not read/write memory)

        # 6. Return unmodified state (homeostatic pass-through)
        return field_state
