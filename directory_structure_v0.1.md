# RAMORGA-ENGINE DIRECTORY STRUCTURE v0.1

Struktura katalogów dla etapu:
- "tylko teoria"
- "tylko testy"
- zero implementacji

/ramorga-engine/
│
├── 02_modules/
│   ├── field_state/
│   │   ├── __init__.md
│   │   └── spec.md
│   ├── tension_loop/
│   │   ├── __init__.md
│   │   └── spec.md
│   ├── energy_regulator/
│   │   ├── __init__.md
│   │   └── spec.md
│   ├── ritual_detector/
│   │   ├── __init__.md
│   │   └── spec.md
│   ├── entropic_modulator/
│   │   ├── __init__.md
│   │   └── spec.md
│   ├── snapshot_manager/
│   │   ├── __init__.md
│   │   └── spec.md
│   ├── pipeline_v13/
│   │   ├── __init__.md
│   │   └── spec.md
│   └── pipeline_v14/   (opcjonalnie)
│       ├── __init__.md
│       └── spec.md
│
├── 07_tests/
│   ├── test_init.md
│   ├── test_regulation_step.md
│   ├── test_energy_stability.md
│   └── test_snapshot.md
│
└── docs/
    ├── README_FieldEngine.md
    ├── README_TensionLoop.md
    └── README_PipelineV13.md
