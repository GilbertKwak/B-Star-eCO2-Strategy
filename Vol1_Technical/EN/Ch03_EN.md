# Ch.3 Heat Source Design & PCHE System

> **Document Info** | Version: v2.0 | Date: 2026-03-19 | Classification: Confidential

---

## 3.1 Heat Source Classification & Design Criteria

| Heat Source | Temperature (°C) | Flow Rate (kg/s) | Suitable Model | Application |
|---|---|---|---|---|
| DC CDU outlet water | 75~95 | 3.0~8.0 | P1 | Hyperscale DC |
| Semiconductor process waste heat | 60~110 | 2.0~6.0 | P1/P2 | Fab cleanroom |
| SMR coolant waste heat | 100~120 | 5.0~15.0 | P2 | Nuclear CHP |
| Industrial boiler exhaust | 80~150 | 1.0~4.0 | P1 | Smart factory |

## 3.2 PCHE Thermal Design

PCHE (Printed Circuit Heat Exchanger) forms micro-channels (diameter 0.5–2 mm) by chemical etching of SS316L or Inconel 718 plates. Designed via NTU-ε method to achieve pinch point ΔT ≤ 5°C.

### 3.2-1 Design Parameters

| Parameter | Value | Unit |
|---|---|---|
| Heat exchanger effectiveness (ε) | ≥90 | % |
| Pinch point (ΔT_pp) | ≤5 | °C |
| Design pressure | 130 | bar |
| Operating pressure | 107 | bar |
| HP-side material | Inconel 718 | — |
| LP-side material | SS316L | — |
| Channel diameter | 0.8 | mm |
| Heat flux per unit area | 15~25 | MW/m² |

## 3.3 T-Q Diagram (GPU CDU 85°C baseline)

Heat source (GPU coolant): 85°C → 45°C heat rejection
CO₂ working fluid: 32°C (inlet) → 67°C (PCHE HP outlet)
Pinch point: Heat source 45°C / CO₂ 40°C → ΔT = 5°C ✅

## 3.4 Procurement

- **PCHE Manufacturer**: HAN Corp. (domestic, 12-week lead time)
- **Qualification standard**: ASME Sec. VIII Div.1 + KS B 6275
- **Material certification**: Mill Certificate — Inconel 718 (ATI/VDM dual sourcing)

*Final review: GilbertKwak | 2026-03-19*
