# Appendix B — Core Data Tables v1.0 (B★ Standalone)

> **Policy**: B★ Standalone Standard | **Version**: v1.0 | **Confirmed**: 2026-04-22 | **Author**: Gilbert

---

## B-1. sCO₂ System Performance Parameters

| Parameter | Design Value | Verified Value (TRL 5) | Unit |
|---|---|---|---|
| Compressor inlet pressure | 7.5 | 7.48 | MPa |
| Compressor outlet pressure | 20.0 | 19.87 | MPa |
| Pressure ratio | 2.67 | 2.65 | — |
| Inlet temperature | 32 | 32.1 | °C |
| Outlet temperature (high-pressure side) | 120 | 118.6 | °C |
| Cooling output (P1 standard) | 82.7 | 80.4 | kW |
| Power consumption | 11.18 | 11.42 | kW |
| **COP (design)** | **7.4** | **7.04** | — |
| Mass flow rate | 0.85 | 0.83 | kg/s |
| Compressor rotational speed | 30,000 | 29,850 | RPM |

---

## B-2. PCHE Heat Exchanger Specifications

| Item | Specification | Notes |
|---|---|---|
| Type | Printed Circuit Heat Exchanger | Brazed bonding |
| Material | SUS316L | CO₂ corrosion resistance |
| Channel diameter | 1.5 mm | Etching process |
| Heat transfer area | 12.4 m² | P1 standard |
| Thermal efficiency (η) | ≥ 85% | Design target |
| Maximum allowable pressure | 25 MPa | Safety factor 1.25 |
| Operating temperature range | -10 ~ 150 °C | — |
| Leak detection accuracy | 98% | IoT sensor standard |

---

## B-3. System Energy Balance (P1 Standard, Normal Operation)

| Item | Value | Unit |
|---|---|---|
| Cooling load (DC servers) | 82.7 | kW |
| Compressor power consumption | 11.18 | kW |
| Auxiliary equipment (pumps·fans) | 1.2 | kW |
| **Total power consumption** | **12.38** | kW |
| **Effective COP** | **6.68** | — |
| Annual power savings (vs. water cooling) | 186,000 | kWh/year |
| Annual CO₂ reduction (power basis) | 85 | tCO₂e/year |
| Annual cooling water savings | 4,200 | m³/year |

---

## B-4. Financial Key Metrics Summary

| Metric | Y1 (2026) | Y2 (2027) | Y3 (2028) |
|---|---|---|---|
| Revenue | ₩2.1B | ₩8.4B | ₩21.0B |
| Gross Margin | 55% | 55% | 55% |
| EBITDA | ▲₩1.14B | ₩0.42B | ₩4.25B |
| Net Income | ▲₩1.28B | ₩0.18B | ₩3.71B |
| Cumulative Customers | 2 | 6 | 18 |
| IRR (investor, 5-year) | — | — | 42.4% |
| NPV (WACC 12%) | — | — | $81.7M |
| Payback Period | — | — | 3.2 yrs |

---

## B-5. Risk RPN Matrix Summary

| Risk ID | Detail | RPN | Level |
|---|---|---|---|
| R-01 | sCO₂ surge/stall | 15 | 🔴 High |
| R-03 | AI DC customer acquisition failure | 15 | 🔴 High |
| R-07 | KGS AC117 certification delay | 12 | 🔴 High |
| R-05 | Series A fundraising failure | 10 | 🔴 High |
| R-09 | Key personnel turnover | 10 | 🔴 High |
| R-06 | CAPEX overrun | 9 | 🟡 Medium |
| R-02 | PCHE leak efficiency drop | 8 | 🟡 Medium |
| R-04 | Competitor market share defense | 8 | 🟡 Medium |
| R-10 | API/ATS security vulnerability | 8 | 🟡 Medium |
| R-08 | CO₂ environmental regulation change | 6 | 🟡 Medium |

---

## B-6. KPI Dashboard Consolidated

| KPI | Y1 Target | Y2 Target | Y3 Target |
|---|---|---|---|
| COP | ≥ 7.0 | ≥ 7.2 | ≥ 7.4 |
| Pilot Customers | 2 | 6 | 18 |
| Revenue | ₩2.1B | ₩8.4B | ₩21.0B |
| CO₂ Reduction (tCO₂e/year) | 680 | 2,040 | 6,120 |
| TRL Level | 6 | 8 | 9 |
| Patents Filed | 1 | 3 | 5 |
| Headcount (FTE) | 5 | 12 | 22 |

---

> ⚠️ **Next Review**: 2026-07-22 | Owner: Gilbert
