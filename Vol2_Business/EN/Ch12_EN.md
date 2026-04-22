# Ch.12 — Risk · Insurance · Contingency v1.0 (B★ Standalone)

> **Policy**: B★ Standalone Standard | **Version**: v1.0 | **Confirmed**: 2026-04-22 | **Author**: Gilbert

---

## 🎯 Chapter Overview

This chapter identifies major risks that may arise during the B★ eCO₂ system's founding and commercialization process, and includes a **quantitative assessment · insurance strategy · contingency plan** for each risk.

---

## 📊 1. Risk Matrix Overview

| Risk ID | Category | Risk Detail | Probability (1~5) | Impact (1~5) | RPN (P×I) | Level |
|---|---|---|---|---|---|---|
| R-01 | Technology | sCO₂ surge/stall | 3 | 5 | **15** | High |
| R-02 | Technology | PCHE leak efficiency drop | 2 | 4 | **8** | Medium |
| R-03 | Market | AI DC pilot customer acquisition failure | 3 | 5 | **15** | High |
| R-04 | Market | Competitor (Vertiv/Stulz) market share defense | 2 | 4 | **8** | Medium |
| R-05 | Financial | Series A fundraising failure | 2 | 5 | **10** | High |
| R-06 | Financial | CAPEX overrun | 3 | 3 | **9** | Medium |
| R-07 | Regulatory | KGS AC117 certification delay | 3 | 4 | **12** | High |
| R-08 | Regulatory | CO₂ leak environmental regulation level change | 2 | 3 | **6** | Medium |
| R-09 | Operations | Key personnel turnover risk | 2 | 5 | **10** | High |
| R-10 | Operations | Line API / ATS remote control security vulnerability | 2 | 4 | **8** | Medium |

---

## 🔴 2. High-Risk Detailed Response Plans (RPN ≥ 10)

### R-01 | sCO₂ Surge/Stall Risk
- **Cause**: Rapid flow reduction upon compressor system spring zone entry
- **Plan**: Shut-off valve response speed < 50ms / Apply DRL defense logic / Maintain 10% cushion in 28,000~32,000 RPM stable zone
- **Contingency Budget**: ₩8M
- **KPI**: Surge occurrence rate 0/year (measured after 6 months)

### R-03 | AI DC Customer Acquisition Failure
- **Cause**: Order delay before PoC completion / possibility of alternative solution selection
- **Plan**: Set 3 pre-secured LOI targets → MOU conversion within 6 months / Co-location centers replaceable as 2nd target contingency
- **Contingency Budget**: ₩15M
- **KPI**: Pilot MOU 2+ within Y1

### R-05 | Series A Fundraising Failure
- **Cause**: Investor psychology dampened during global interest rate hike / concern about bias toward non-cooling markets
- **Plan**: Advance government R&D contract ($500K) + strategic LP recruitment / Pre-distribute IR deck One-Pager English version
- **Contingency Budget**: ₩5M
- **KPI**: 1+ LOI before Y1 Q3

### R-07 | KGS AC117 Certification Delay
- **Cause**: CO₂ refrigerant equipment special specification certification cost average 9~18 months
- **Plan**: Pre-consulting contract with dedicated certification agency (Korea Gas Safety Corporation) / Target test completion within 10 months of Unit 1 PoC deadline
- **Contingency Budget**: ₩12M
- **KPI**: KGS preliminary certification activity commenced within 2026 Q4

### R-09 | Key Personnel Turnover Risk
- **Cause**: Risk of internal sCO₂ expert departure during rapid growth
- **Plan**: Core 2 persons (Gilbert + Technical Lead) lock-up 3-year stock vesting / Internal technical documentation to convert knowledge into assets
- **Contingency Budget**: ₩0 (replaced by legal contract system)
- **KPI**: Core 2-person vesting contract signed within 2026 Q2

---

## 🟡 3. Medium-Risk Short-term Plans (RPN 6~9)

| Risk ID | Action Plan | Owner |
|---|---|---|
| R-02 | Dual-source contract with 2+ PCHE manufacturers | Gilbert |
| R-04 | Differentiation vs. Vertiv: Prepare COP 7.4 vs. competitor 4.2 comparison materials | Sales |
| R-06 | BOM locked price monthly monitoring + 10% cushion | Business |
| R-08 | Comparative review of CO₂ leak permissible regulation ahead of change | Regulatory |
| R-10 | Zero-trust VPN + API token 90-day expiry rotation | DevOps |

---

## 💰 4. Insurance Portfolio

| Insurance Type | Coverage | Annual Premium Budget | Priority |
|---|---|---|---|
| Product Liability (PL) | ₩500M limit per product defect | ₩3M/year | Estimated |
| Directors & Officers (D&O) | Executive decision regulatory risk | ₩2M/year | Critical |
| Facility Fire Insurance | Equipment replacement cost | ₩1.5M/year | Required |
| Cyber Insurance | API/Line system data breach | ₩1M/year | Recommended |
| **Total** | | **₩7.5M/year** | |

---

## 📅 5. Contingency Budget Summary

| Item | Budget |
|---|---|
| Technology contingency (R-01, 02) | ₩16M |
| Market·Sales contingency (R-03, 04) | ₩20M |
| Financial contingency (R-05, 06) | ₩10M |
| Regulatory contingency (R-07, 08) | ₩15M |
| Personnel contingency (R-09, 10) | ₩5M |
| **Total Contingency Reserve (~29% of CAPEX)** | **₩66M** |

---

> ⚠️ **Next Review**: 2026-07-22 (3 months) | Owner: Gilbert
