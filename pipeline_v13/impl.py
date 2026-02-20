diff --git a/pipeline_v13/impl.py b/pipeline_v13/impl.py
index 0000000..1111111 100644
--- a/pipeline_v13/impl.py
+++ b/pipeline_v13/impl.py
@@ -9,6 +9,10 @@ from typing import Any, Dict, Optional, Tuple

 from field_state.impl import FieldState, FieldStateManager, FieldStateError

+# NOWE: import modułu energy_regulator
+from energy_regulator.impl import EnergyRegulator, EnergyRegulatorParams
+

 class PipelineError(Exception):
     """Błąd sekwencji wykonawczej lub trybu pipeline."""
@@ -52,7 +56,12 @@ class PipelineV13:
     """

-    def __init__(self, fsm: FieldStateManager) -> None:
+    def __init__(
+        self,
+        fsm: FieldStateManager,
+        *,
+        energy_regulator: Optional[EnergyRegulator] = None,
+    ) -> None:
         if fsm is None:
             raise PipelineError("FieldStateManager is required")
         self.fsm = fsm
@@ -60,6 +69,10 @@ class PipelineV13:
 
         self.snapshot_manager = SnapshotManager()

+        # NOWE: zewnętrzny moduł energy_regulator (opcjonalny)
+        self.energy_regulator = energy_regulator
+

     # ------------------------------------------------------------------ #
     # API GŁÓWNE
@@ -207,12 +220,40 @@ class PipelineV13:
         """
         Wykonuje jeden krok regulacji:

-        tension_loop → energy_regulator → entropic_modulator → ritual_detector
+        tension_loop → energy_regulator (zewnętrzny lub fallback)
+        → entropic_modulator → ritual_detector
         """

         # 1. TENSION LOOP
         s1 = self._run_tension_loop(state, params.get("tension", {}))

-        s2 = self._run_energy_regulator(s1, params.get("energy", {}))
+        # 2. ENERGY REGULATOR — PODMIANA NA MODUŁ ZEWNĘTRZNY
+        energy_cfg = params.get("energy", {})
+
+        if self.energy_regulator is not None:
+            s2 = self.energy_regulator.run(
+                state=s1,
+                tension_map=s1.tension_map,
+                params=EnergyRegulatorParams(
+                    min_energy=energy_cfg.get("energy_min", self.fsm.DEFAULT_ENERGY_MIN),
+                    max_energy=energy_cfg.get("energy_max", self.fsm.DEFAULT_ENERGY_MAX),
+                    gain=energy_cfg.get("gain", 1.0),
+                ),
+            )
+        else:
+            # fallback: minimalna implementacja
+            s2 = self._run_energy_regulator(s1, energy_cfg)

         # 3. ENTROPY
         s3 = self._run_entropic_modulator(s2, params.get("entropy", {}))
