# Ch.4 Compressor & PCHE Thermal Design

> **Document Info** | Version: v2.0 | Date: 2026-03-19 | Classification: Confidential

---

## 4.1 Compressor Design Parameters

| Parameter | Value | Unit |
|---|---|---|
| Type | Semi-hermetic centrifugal | — |
| Suction pressure | 28 | bar |
| Discharge pressure | 107 | bar |
| Pressure ratio (PR) | 3.82 | — |
| Mass flow rate | 0.165 | kg/s |
| Isentropic efficiency | 72 | % |
| Design speed | 24,000 | rpm |
| VFD control range | 50~100 | % |

## 4.2 Compressor Performance Map

The performance map defines the safe operating region between the Surge Line and Choke Line.

- **Design point**: 0.165 kg/s, PR=3.82, η=72%
- **Surge margin**: −20% flow from design point
- **Choke margin**: +25% flow from design point
- **Part-load**: VFD maintains η ≥68% down to 50% load

## 4.3 PCHE Detailed Thermal Design

### 4.3-1 NTU-ε Method Results

- NTU = 4.8
- ε = 91.2% (requirement ≥90% ✅)
- UA = 38.4 kW/°C
- Pinch point ΔT = 4.8°C (requirement ≤5°C ✅)

## 4.4 Part-Load Performance

| Load (%) | Flow (kg/s) | COP | Notes |
|---|---|---|---|
| 100 | 0.165 | 7.4 | Design point |
| 80 | 0.132 | 7.1 | VFD control |
| 60 | 0.099 | 6.6 | VFD control |
| 50 | 0.083 | 6.2 | Ev.197 validated |

## 4.5 FMEA Risk Matrix

| Failure Mode | Frequency | Severity | Detectability | RPN | Countermeasure |
|---|---|---|---|---|---|
| Compressor surge | 2 | 4 | 3 | 24 | VFD surge detection algorithm |
| PCHE fouling | 2 | 3 | 3 | 18 | Differential pressure monitoring |
| High-pressure exceedance | 1 | 5 | 2 | 10 | PRV + ESD dual protection |
| CO₂ leak | 2 | 4 | 2 | 16 | IR leak detector |

*Final review: GilbertKwak | 2026-03-19*
