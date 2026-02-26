📘 DOCUMENTATION_INDEX.md
Kompletny indeks dokumentacji RAMORGA ENGINE

Dokument stanowi centralny punkt nawigacji po repozytorium RAMORGA ENGINE.
Łączy wszystkie moduły, opisuje ich role i wskazuje właściwe pliki źródłowe.

1. Struktura repozytorium
ramorga-engine/
│
├── 01_runtime/
│   ├── runtime_overview.md
│   ├── glitch_hook.md
│   ├── carnival_gate_hook.md
│   ├── crime_planning_detector.md
│   ├── topology_metrics.md
│   ├── memory_audit_hook.md
│   ├── pipeline_integration/
│   │      ├── hooks_pipeline_v13.md
│   │      ├── pipeline_v13_meniscus_integration.md
│   │      └── test_hooks_and_pipeline_v13.py
│   └── databridge/
│          ├── databridge.md
│          ├── databridge_impl.py
│          ├── databridge_contract.md
│          ├── storage_backend.py
│          └── databridge_tests.py
│
├── 02_field_engine/
│   ├── field_engine.md
│   └── field_engine.py
│
├── 04_meniscus_engine/
│   ├── README.md
│   ├── meniscus_engine.py
│   ├── meniscus_contract.md
│   ├── meniscus_invariants.md
│   └── meniscus_tests.py
│
├── pipeline_v13/
│   ├── impl.py
│   └── test_pipeline_v13.py
│
├── 01_runtime/field_state/
│   ├── state_invariants.md
│   ├── field_state_manager.py
│   └── test_FIELD_STATE_invariants.py
│
└── 07_tests/
    ├── integration/
    ├── ci_blockers/
    └── unit/

 ===
 2. Dokumentacja runtime
🔹 Loop RAMORGI
Plik:  
01_runtime/runtime_overview.md

Opisuje trzy fazy wykonania:

OBSERVE

REGULATE

CONTINUE

oraz ich relacje z pipeline_v13, MeniscusEngine i DataBridge.

🔹 Hooki runtime
Każdy hook ma własny plik:

glitch_hook.md

carnival_gate_hook.md

crime_planning_detector.md

memory_audit_hook.md

topology_metrics.md

🔹 Integracja runtime → pipeline
Folder:  
01_runtime/pipeline_integration/

Zawiera:

hooks_pipeline_v13.md

pipeline_v13_meniscus_integration.md

testy integracyjne

3. Dokumentacja FieldState i FieldStateManager
🔹 Inwarianty stanu
01_runtime/field_state/state_invariants.md

🔹 Implementacja
01_runtime/field_state/field_state_manager.py

🔹 Testy CI-blockers
01_runtime/field_state/test_FIELD_STATE_invariants.py

4. Dokumentacja MeniscusEngine
🔹 Kontrakt
04_meniscus_engine/meniscus_contract.md

🔹 Inwarianty
04_meniscus_engine/meniscus_invariants.md

🔹 Implementacja
04_meniscus_engine/meniscus_engine.py

🔹 Testy
04_meniscus_engine/meniscus_tests.py

5. Dokumentacja FieldEngine
🔹 Opis
02_field_engine/field_engine.md

🔹 Implementacja
02_field_engine/field_engine.py

6. Dokumentacja DataBridge
🔹 Opis
01_runtime/databridge/databridge.md

🔹 Kontrakt
01_runtime/databridge/databridge_contract.md

🔹 Implementacja
01_runtime/databridge/databridge_impl.py

🔹 Backend zapisu
01_runtime/databridge/storage_backend.py

🔹 Testy
01_runtime/databridge/databridge_tests.py

7. Dokumentacja pipeline_v13
🔹 Implementacja
pipeline_v13/impl.py

🔹 Testy
pipeline_v13/test_pipeline_v13.py

8. Testy globalne
🔹 CI-blockers
07_tests/ci_blockers/

🔹 Integracyjne
07_tests/integration/

🔹 Jednostkowe
07_tests/unit/

9. Zasady linkowania między modułami
    
Każdy moduł powinien linkować do:
swojego kontraktu,
swoich inwariantów,
swojej implementacji,
swoich testów,
dokumentacji runtime_overview (jeśli dotyczy).

Przykład linkowania (w każdym README modułu):
Powiązane dokumenty:
- [Kontrakt MeniscusEngine](meniscus_contract.md)
- [Inwarianty MeniscusEngine](meniscus_invariants.md)
- [Integracja z pipeline_v13](../01_runtime/pipeline_integration/pipeline_v13_meniscus_integration.md)
- [Testy MeniscusEngine](meniscus_tests.py)

10. Zasady spójności dokumentacji
Każdy moduł ma jeden plik README opisujący jego rolę.

Każdy moduł ma kontrakt (contract.md).

Każdy moduł ma inwarianty (invariants.md).

Każdy moduł ma testy (unit + integration + CI-blockers).

Każdy moduł linkuje do runtime_overview.md.

Każdy moduł linkuje do pipeline_v13, jeśli jest w pętli wykonawczej.

Każdy moduł ma spójne nazwy plików.

11. Status dokumentacji
Dokumentacja repo jest kompletna, spójna i zgodna z:

meta‑inwariantami pola,
Loop RAMORGI,
ATML,
MBP HAI 2.0 + patch,
continuity model,
transition architecture.

Repo jest gotowe do dalszej rozbudowy i audytu.
