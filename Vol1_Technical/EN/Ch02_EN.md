# Ch.2 Thermodynamic Design Fundamentals

> **Document Info** | Version: v2.0 | Date: 2026-03-19 | Classification: Confidential

---

## 2.1 CO₂ Thermophysical Properties

Near its critical point (31.1°C, 73.8 bar), CO₂ exhibits rapid changes in specific heat, density, and thermal conductivity. B★ eCO₂ strategically exploits this near-critical region to achieve 15% higher thermal efficiency than conventional ORC systems.

## 2.2 Reverse Rankine Cycle Analysis

| State | Location | T (°C) | P (bar) | h (kJ/kg) |
|---|---|---|---|---|
| 1 | Compressor inlet | 32 | 28 | 430.2 |
| 2 | Compressor outlet | 95 | 107 | 478.6 |
| 3 | PCHE HP outlet | 67 | 107 | 320.4 |
| 4 | Expander outlet | 38 | 28 | 285.1 |

## 2.3 System Efficiency

- Compressor power: W_c = ṁ × (h2−h1) = 0.165 × 48.4 = **7.99 kW**
- Expander output: W_e = ṁ × (h3−h4) × η_e = 0.165 × 35.3 × 0.78 = **4.55 kW**
- Net output: W_net = **82.7 kW** (including heat source contribution)
- Design-point COP: **7.4**

## 2.4 eCO₂ vs sCO₂ vs ORC

| Metric | eCO₂ B★ | sCO₂ | Standard ORC |
|---|---|---|---|
| Operating pressure (bar) | 28~107 | 70~250 | 5~40 |
| Near-critical operation | Near-critical | Supercritical | Subcritical |
| Thermal efficiency (%) | **85** | 78 | 72 |
| TRL | **8** | 5~6 | 7~8 |
| GWP | **1** | 1 | 140~1,300 |
| CAPEX (₩/W) | **2,756** | 4,200 | 3,100 |

## 2.5 Two-Stage Intercooling Option (P2)

P2 (165.4 kW): pressure ratio PR=6.0 with two-stage compression (intercooler) improves compression efficiency by +3.5 pp. Suitable for SMR and large industrial waste heat applications.

*Final review: GilbertKwak | 2026-03-19*
