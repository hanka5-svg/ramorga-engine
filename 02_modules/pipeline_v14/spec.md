# pipeline_v14/spec.md

## Rola modułu
Moduł odpowiedzialny za:
- rozszerzenie pipeline_v13 o integrację z warstwami C/G/S/Meniscus,
- obsługę sprzężeń między warstwami a polem,
- testowanie wielowarstwowej regulacji.

## Wejścia
- `FieldState`
- warstwy: `C_layer`, `G_layer`, `S_layer`, `Meniscus_layer`
- parametry regulacyjne rozszerzone

## Wyjścia
- `FieldState` (rozszerzony)
- `MultiLayerSnapshot`
- dodatkowe flagi stabilności międzywarstwowej

## Zależności
- pipeline_v13 (logika bazowa)
- warstwy C/G/S/M (z ramorga-architecture / innych modułów)

## Testy (powiązanie)
- (do zaplanowania po domknięciu PipelineV13)
