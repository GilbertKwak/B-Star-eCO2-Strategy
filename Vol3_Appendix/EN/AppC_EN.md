# Appendix C: Glossary · Abbreviations · References

> **Document Info** | Version: v2.0 | Date: 2026-03-19 | Classification: Confidential

---

## C-1. Glossary

| Term | Definition |
|---|---|
| Supercritical CO₂ (sCO₂) | CO₂ above its critical point (31.1°C, 73.8 bar), exhibiting intermediate properties between gas and liquid |
| Electrified CO₂ (eCO₂) | B★-defined concept: CO₂ used as refrigerant and working fluid, with VFD and AI control to dynamically optimize electrical energy output |
| Reverse Rankine Cycle | Thermodynamic cycle converting heat energy to electricity; B★ eCO₂ uses CO₂ as the working fluid |
| PCHE | Printed Circuit Heat Exchanger — micro-channel exchanger formed by chemical etching; rated for >200 bar and >600°C |
| Pinch Point (ΔT_pp) | Location in a heat exchanger where the temperature difference is minimized; B★ design requirement: ΔT_pp ≤ 5°C |
| COP | Coefficient of Performance — net electrical output (kW) ÷ heat input (kW); B★ P1 design COP = 7.4 |
| TRL | Technology Readiness Level (NASA scale 1–9); TRL 8 = system proven in operational environment |
| VFD | Variable Frequency Drive (inverter) — varies compressor speed for part-load efficiency optimization |
| ESD | Emergency Shutdown — safety system; B★ SIL-2 rated, response time ≤100 ms |
| SIL | Safety Integrity Level — per IEC 61511; B★ applies SIL-2 |
| FMEA | Failure Mode and Effects Analysis — Risk = Frequency × Severity × Detectability |
| Demand Response (DR) | Grid flexibility service; B★ integrates with KEPCO AMI to adjust output during peak periods |
| K-ETS | Korea Emissions Trading Scheme — B★ CO₂ abatement qualifies for carbon credit recognition |
| WACC | Weighted Average Cost of Capital — B★ financial model discount rate: 10% |
| NPV | Net Present Value — B★ Base scenario 10-year NPV: ₩8.7B |
| IRR | Internal Rate of Return — B★ Base: 31.4% vs WACC 10% |
| PBP | Payback Period — B★ Base: 4.3 years |
| CAPEX | Capital Expenditure — B★ P1 unit cost: ₩228M (₩2,756/W) |
| O&M | Operation & Maintenance — B★ revenue: ₩8M/unit/yr from Year 2 |
| PCT | Patent Cooperation Treaty — B★ C-07, C-08, C-09 internationally filed |
| TAM | Total Addressable Market |
| CAGR | Compound Annual Growth Rate |
| MPC | Model Predictive Control — requires 43% more stabilization time vs B★ Adaptive AI control |
| PdM | Predictive Maintenance — B★ LSTM model RUL prediction accuracy ±5% |
| RUL | Remaining Useful Life — LSTM-based 30-day early warning |
| CDU | Coolant Distribution Unit — direct liquid cooling for DC server racks |
| WHR | Waste Heat Recovery — B★ primary application domain |
| SMR | Small Modular Reactor — B★ P2 (165 kW) application under review |
| GTM | Go-To-Market — market entry strategy |
| LOI | Letter of Intent — P-01 customer signed |
| MOU | Memorandum of Understanding — P-02 customer signed |
| EPC | Engineering, Procurement & Construction — turnkey contract model |
| SCADA | Supervisory Control and Data Acquisition |
| DMZ | Demilitarized Zone — IT/OT boundary security per IEC 62443 Zone 2–3 |

---

## C-2. Abbreviations

| Abbreviation | Full Form | Relevant Chapter |
|---|---|---|
| B★ | B-Star (company name) | All |
| eCO₂ | Electrified CO₂ | Ch.1, Ch.3 |
| sCO₂ | Supercritical CO₂ | Ch.1, Ch.2 |
| ORC | Organic Rankine Cycle | Ch.1, Ch.2 |
| PCHE | Printed Circuit Heat Exchanger | Ch.3, Ch.4 |
| VFD | Variable Frequency Drive | Ch.4, Ch.5 |
| COP | Coefficient of Performance | Ch.3, Ch.5 |
| TRL | Technology Readiness Level | Ch.1, Ch.2 |
| ESD | Emergency Shutdown | Ch.5, Ch.6 |
| SIL | Safety Integrity Level | Ch.6 |
| FMEA | Failure Mode & Effects Analysis | Ch.4, Ch.6 |
| KGS | Korea Gas Safety Corporation | Ch.6 |
| ATEX | ATmosphères EXplosibles (EU directive) | Ch.6 |
| DR | Demand Response | Ch.5 |
| AMI | Advanced Metering Infrastructure | Ch.5 |
| K-ETS | Korea Emissions Trading Scheme | Ch.5, Ch.8 |
| WACC | Weighted Average Cost of Capital | Ch.8 |
| NPV | Net Present Value | Ch.8 |
| IRR | Internal Rate of Return | Ch.8 |
| PBP | Payback Period | Ch.8 |
| CAPEX | Capital Expenditure | Ch.7, Ch.8 |
| BOM | Bill of Materials | Ch.7 |
| GTM | Go-To-Market | Ch.7 |
| PCT | Patent Cooperation Treaty | Ch.9 |
| IP | Intellectual Property | Ch.9 |
| TAM | Total Addressable Market | Ch.1, Ch.2 |
| CAGR | Compound Annual Growth Rate | Ch.1, Ch.2 |
| MPC | Model Predictive Control | Ch.5 |
| PdM | Predictive Maintenance | Ch.5 |
| RUL | Remaining Useful Life | Ch.5 |
| CDU | Coolant Distribution Unit | Ch.1, Ch.3 |
| WHR | Waste Heat Recovery | Ch.1 |
| SMR | Small Modular Reactor | Ch.1, Ch.2 |
| LOI | Letter of Intent | Ch.7 |
| EPC | Engineering, Procurement & Construction | Ch.7 |
| SCADA | Supervisory Control & Data Acquisition | Ch.5 |
| DCF | Discounted Cash Flow | Ch.8 |
| ESG | Environmental, Social, Governance | Ch.5, Ch.8 |
| AI | Artificial Intelligence | Ch.5, Ch.9 |
| LSTM | Long Short-Term Memory (AI model) | Ch.5 |
| DMZ | Demilitarized Zone | Ch.5 |
| IEC | International Electrotechnical Commission | Ch.5, Ch.6 |
| KS | Korean Industrial Standard | Ch.6 |

---

## C-3. References

### C-3-1. Academic Papers

| # | Author(s) | Title | Journal | Year |
|---|---|---|---|---|
| [1] | Kim, J. et al. | Thermodynamic analysis of transcritical CO₂ power cycle for low-grade waste heat recovery | Applied Energy | 2023 |
| [2] | Chen, L. et al. | Performance optimization of printed circuit heat exchanger for sCO₂ Brayton cycle | Energy Conversion & Management | 2024 |
| [3] | Park, S. et al. | AI-based adaptive control for variable-speed CO₂ compressor in data center cooling | Int'l Journal of Refrigeration | 2024 |
| [4] | Lee, H. et al. | Economic feasibility of waste heat recovery from hyperscale data centers using CO₂ power cycles | Energy Policy | 2025 |
| [5] | Dostal, V. | A Supercritical Carbon Dioxide Cycle for Next Generation Nuclear Reactors | MIT PhD Thesis | 2004 |
| [6] | Monje, B. et al. | Designing centrifugal compressors for supercritical CO₂ | ASME Turbo Expo | 2022 |
| [7] | Kim, Y. et al. | Digital twin framework for predictive maintenance of CO₂ heat pump systems | Reliability Engineering & System Safety | 2025 |

### C-3-2. Standards & Regulations

| # | Standard No. | Title | Issuing Body |
|---|---|---|---|
| [8] | KGS AC117 | Facility, technical and inspection criteria for CO₂ refrigeration & heat pump equipment | Korea Gas Safety Corp. |
| [9] | IEC 61511 | Functional Safety: Safety Instrumented Systems for the Process Industry | IEC |
| [10] | IEC 62443 | Industrial Automation and Control Systems Security | IEC |
| [11] | ATEX 2014/34/EU | Equipment in Potentially Explosive Atmospheres | EU |
| [12] | ASHRAE 15-2022 | Safety Standard for Refrigeration Systems | ASHRAE |
| [13] | KS B 6275 | Heat Exchanger Performance Test Method | KATS |
| [14] | ISO 13709 | Centrifugal Pumps for Petroleum & Gas Industries | ISO |

### C-3-3. Market & Industry Reports

| # | Organization | Title | Year |
|---|---|---|---|
| [15] | IEA | Data Centres and Data Transmission Networks | 2025 |
| [16] | McKinsey & Company | The Coming AI Infrastructure Supercycle | 2025 |
| [17] | BloombergNEF | New Energy Outlook 2025: Power Sector Transformation | 2025 |
| [18] | KEPCO Research Institute | Korea Power Demand Forecast 2026–2035 | 2025 |
| [19] | KAERI | SMR Commercialization Roadmap 2030 | 2025 |
| [20] | Grand View Research | CO₂ Heat Pump Market Size & Forecast 2024–2030 | 2024 |
| [21] | Ministry of Trade, Industry and Energy (Korea) | 2030 Energy Efficiency Innovation Strategy | 2024 |
| [22] | Ministry of Environment (Korea) | 4th Emissions Trading Scheme Master Plan (2026–2030) | 2025 |

### C-3-4. Internal Validation Evidence

| # | Doc ID | Description | Date |
|---|---|---|---|
| [Ev.195] | B★-TEST-2025-195 | P1 (82.7 kW) physical test report — Taiwan partner facility | 2025-11 |
| [Ev.196] | B★-TEST-2025-196 | PCHE pinch point ΔT≤5°C thermal performance validation | 2025-11 |
| [Ev.197] | B★-TEST-2025-197 | VFD part-load (50%) COP 6.2 measured data | 2025-12 |
| [Ev.198] | B★-CTRL-2026-001 | AI adaptive control stabilization time 3.5s lab validation | 2026-01 |
| [Ev.199] | B★-SAFE-2026-010 | ESD SIL-2 response time <100ms test certificate | 2026-02 |

---

## C-4. Unit Conversion Table

| Quantity | SI Unit | Conversion | Notes |
|---|---|---|---|
| Pressure | bar | 1 bar = 100 kPa = 0.987 atm | Design basis: bar |
| Temperature | °C | K = °C + 273.15 | — |
| Mass flow | kg/s | 1 kg/s = 3,600 kg/h | — |
| Heat / Power | kW | 1 kW = 3,412 BTU/h | — |
| Energy | kWh | 1 kWh = 3.6 MJ | — |
| Carbon | tCO₂ | 1 tCO₂ = 1,000 kg CO₂ | K-ETS trading unit |
| FX rate (ref.) | ₩/$ | 1 USD = ₩1,350 | Mar 2026 basis |
| FX rate (ref.) | ₩/€ | 1 EUR = ₩1,480 | Mar 2026 basis |

---

*This appendix is based on Ch.1–9 body text and Ev.195–199 physical validation data.*
*Final review: GilbertKwak | 2026-03-19*
