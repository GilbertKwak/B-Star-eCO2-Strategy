# Appendix B: Core Data Tables

> **Document Info** | Version: v2.0 | Date: 2026-03-19 | Classification: Confidential
> This appendix provides the source data for all key figures cited throughout Ch.1–9.

---

## B-1. eCO₂ B★ System Design Parameters (P1 Baseline)

| Parameter | Symbol | Value | Unit | Source |
|---|---|---|---|---|
| Rated electrical output | W_net | 82.7 | kW | Ev.195 Physical Test |
| Heat source inlet temp | T_hot,in | 85 | °C | DC CDU baseline |
| Heat source outlet temp | T_hot,out | 45 | °C | PCHE design criterion |
| Low-temp sink | T_cold | 25 | °C | Ambient / cooling tower |
| Suction pressure | P_suc | 28 | bar | Compressor design point |
| Discharge pressure | P_dis | 107 | bar | High-pressure limit |
| Pressure ratio | PR | 3.82 | — | P_dis / P_suc |
| Mass flow rate | ṁ | 0.165 | kg/s | P1 design point |
| Compressor isentropic efficiency | η_c | 72 | % | Physical validation |
| Expander isentropic efficiency | η_e | 78 | % | Physical validation |
| PCHE pinch point | ΔT_pp | ≤5 | °C | Design requirement |
| Heat exchanger effectiveness | ε_PCHE | ≥90 | % | Design requirement |
| Design-point COP | COP_des | 7.4 | — | Ch.3 thermodynamic calc |
| Annual average COP | COP_ann | 7.1 | — | Ch.5 monthly simulation |
| Annual availability | Availability | 97.7 | % | Ch.5 base / 99.1% w/ PdM |
| Annual energy output | E_ann | 799,450 | kWh | 82.7kW × 8,760h × 97.7% |
| Refrigerant | — | R-744 (CO₂) | — | GWP=1, ODP=0 |
| Annual CO₂ abatement | — | 320 | tCO₂/yr | Korea avg. emission factor |

---

## B-2. Competitive Technology Performance Comparison

| Metric | B★ eCO₂ | sCO₂ (Competitor) | Standard ORC | Unit |
|---|---|---|---|---|
| Thermal efficiency | **85** | 78 | 72 | % |
| CAPEX/kW | **2,756** | 4,200 | 3,100 | ₩/W |
| TRL | **8** | 5~6 | 7~8 | — |
| GWP | **1** | 1 | 140~1,300 | — |
| Operating pressure | 28~107 | 70~250 | 5~40 | bar |
| Near-critical operation | Near-critical | Supercritical | Subcritical | — |
| Commercialization | **2026 Q3** | 2028+ | Available now | — |

---

## B-3. CAPEX Bill of Materials (P1, 82.7 kW)

| Component | Cost (₩M) | Share (%) | Key Supplier | Lead Time |
|---|---|---|---|---|
| Compressor OEM | 68 | 29.8 | Overseas OEM (localization review) | 16 wks |
| PCHE heat exchanger | 45 | 19.7 | HAN Corp. (domestic) | 12 wks |
| VFD inverter | 32 | 14.0 | LS Electric | 8 wks |
| Control system (PLC+SCADA) | 28 | 12.3 | B★ in-house | 6 wks |
| Piping, valves, instruments | 22 | 9.6 | Domestic partners | 6 wks |
| Civil & electrical works | 18 | 7.9 | EPC partner | 8 wks |
| Engineering & commissioning | 15 | 6.6 | B★ in-house | — |
| **Total** | **228** | **100** | — | — |
| **Unit cost (₩/W)** | **2,756** | — | — | — |

> Domestic content ratio: currently 68% → target 75% by 2027 (compressor localization saves ₩15M additional)

---

## B-4. Financial Model — Key Assumptions & Results

### B-4-1. Input Assumptions

| Item | Value | Notes |
|---|---|---|
| Analysis period | 10 years (2026–2035) | — |
| WACC | 10% | Equity 40% + Policy finance 35% + Bank 25% |
| Cost of equity | 15% | VC required return |
| Policy finance rate | 3.5% | Industrial transition fund |
| Bank loan rate | 5.5% | — |
| Pilot unit price | ₩280M/unit | 82.7 kW basis |
| Volume unit price | ₩260M/unit | 5+ units |
| Export unit price | ₩320M/unit | USD equivalent |
| O&M revenue | ₩8M/unit/yr | From Year 2 |
| Corporate tax rate | 22% | Korea standard |
| Depreciation | 5-year straight-line | — |

### B-4-2. Scenario Financial Results

| Scenario | Revenue Assumption | NPV (₩B) | IRR (%) | PBP (yr) | ROI (%) |
|---|---|---|---|---|---|
| Bear (-30%) | Price & volume -30% | 2.8 | 18.2 | 6.2 | 82 |
| **Base** | **Baseline assumptions** | **8.7** | **31.4** | **4.3** | **215** |
| Bull (+30%) | Price & volume +30% | 16.4 | 47.6 | 3.1 | 380 |

> Bear scenario: IRR (18.2%) > WACC (10%) → investment viability maintained

### B-4-3. Annual Cash Flow (Base Scenario, ₩M)

| Year | Revenue | COGS | EBITDA | After-tax NCF | Cumulative NPV |
|---|---|---|---|---|---|
| Y0 (2026) | 0 | 0 | -150 | -150 | -150 |
| Y1 (2027) | 280 | 228 | -98 | -534 | -648 |
| Y2 (2028) | 840 | 598 | 198 | 154 | -522 |
| Y3 (2029) | 1,680 | 1,082 | 542 | 421 | -139 |
| Y4 (2030) | 2,520 | 1,566 | 886 | 691 | 490 |
| Y5 (2031) | 3,080 | 1,876 | 1,140 | 889 | 1,296 |
| Y6–10 | Scaling | Scaling | Scaling | Scaling | **13,500** |

---

## B-5. Commercialization Pipeline (as of 2026-03)

| ID | Customer Type | Scale | Stage | Expected Contract | Value (₩M) |
|---|---|---|---|---|---|
| P-01 | Domestic hyperscale DC | 82.7kW ×3 | LOI signed | 2026 Q3 | 840 |
| P-02 | Semiconductor Fab A | 82.7kW ×2 | MOU signed | 2026 Q4 | 560 |
| P-03 | Smart factory B | 82.7kW ×1 | Tech review | 2027 Q1 | 280 |
| P-04 | Domestic SMR developer | 165kW ×2 | Pre-feasibility | 2027 Q2 | 1,200 |
| P-05 | Singapore DC | 82.7kW ×4 | Proposal prep | 2027 Q3 | 1,280 |
| P-06~17 | Pipeline | Multiple | Prospecting | 2027–2028 | 18,640 |
| **Total** | — | — | — | — | **22,800** |

---

## B-6. IP & Patent Portfolio

| Patent ID | Title | Type | Jurisdictions | TRL | Strength | Status |
|---|---|---|---|---|---|---|
| C-01 | eCO₂ Reverse Rankine Cycle | Foundation | KR+US | 8 | 9.2 | Granted |
| C-02 | PCHE Channel Optimization | Materials | KR | 7 | 8.1 | Granted |
| C-03 | Pressure Ratio Control Algorithm | Control | KR | 8 | 8.5 | Granted |
| C-04 | Refrigerant Piping Vibration Reduction | Defensive | KR | 7 | 7.8 | Granted |
| C-05 | Partial-load VFD Optimization | Control | KR | 8 | 8.3 | Granted |
| C-06 | CO₂ Leak Detection System | Safety | KR | 7 | 7.5 | Granted |
| **C-07** | **AI Adaptive Control** | **PCT Core** | **KR/US/EU/JP/CN** | **8** | **9.5** | **Int'l Filed** |
| **C-08** | **Digital Twin Predictive Maintenance** | **PCT Core** | **KR/US/EU/JP/CN** | **7** | **9.0** | **Int'l Filed** |
| **C-09** | **DR & Energy Trading Integration** | **PCT Core** | **KR/US/EU/JP** | **7** | **8.8** | **Int'l Filed** |
| C-10 | Compressor Surge Prevention | Defensive | KR | 6 | 7.2 | Pending |
| C-11 | PCHE Fouling Self-diagnosis | Defensive | KR | 6 | 7.0 | Pending |
| C-12 | High-pressure ESD Sequence | Safety | KR | 7 | 7.6 | Pending |

---

## B-7. Supply Chain Risk Matrix

| Component | Supplier | Lead Time | Risk Score | Mitigation | Timeline |
|---|---|---|---|---|---|
| Inconel 718 | ATI (US), VDM (DE) | 20 wks | **4.5** | Dual-source confirmed | 2026 Q3 |
| Compressor OEM | Single overseas | 16 wks | **4.2** | Domestic alt. review (Mando) | 2026 Q4 |
| Rare earth magnets (VFD) | China-dependent | 12 wks | 3.8 | Non-China sourcing | 2027 Q1 |
| PCHE material (SS316L) | HAN Corp. | 12 wks | 3.2 | Pre-stock buffer | Immediate |
| Semiconductor chip (PLC) | Siemens/LS | 10 wks | 2.9 | Dual-source maintained | Ongoing |
| VFD inverter | LS Electric | 8 wks | 2.1 | Domestic single → stable | Ongoing |

---

## B-8. Annual Carbon & ESG Performance Forecast

| Year | Cumulative Units | Annual CO₂ Saved (tCO₂) | Cumulative Saved (tCO₂) | Carbon Credit Value (₩M) | ESG Rating Target |
|---|---|---|---|---|---|
| 2026 | 3 | 960 | 960 | 14.4 | B |
| 2027 | 8 | 2,560 | 3,520 | 38.4 | B+ |
| 2028 | 17 | 5,440 | 8,960 | 81.6 | A |
| 2029 | 28 | 8,960 | 17,920 | 134.4 | A+ |
| 2030 | 42 | 13,440 | 31,360 | 201.6 | AA |

> Carbon credit price: ₩15,000/tCO₂ (K-ETS 2026 reference)
> CO₂ abatement basis: 320 tCO₂/yr/unit

---

*This appendix is based on Ch.1–9 body text and Ev.195 physical test results (2025).*
*Final review: GilbertKwak | 2026-03-19*
