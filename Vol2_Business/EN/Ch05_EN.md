# Ch.5 System Integration & Control Strategy

> **Document Info** | Version: v2.0 | Date: 2026-03-19 | Classification: Confidential

---

## 5.1 Five-Layer Integration Architecture

| Layer | Function | Protocol | Response Time | Security Zone |
|---|---|---|---|---|
| L1 Field Devices | Sensors & actuators | Modbus RTU | 1ms | Zone 0 |
| L2 PLC/Local Control | Sequence & ESD | Modbus TCP | 10ms | Zone 1 |
| L3 SCADA/HMI | Monitoring & alarms | OPC-UA | 100ms | Zone 2 |
| L4 MES/ERP | Production & energy mgmt | REST API | 1s | Zone 3 |
| L5 Cloud AI | Predictive maint. & DR | gRPC/MQTT | 10s | Zone 4 |

## 5.2 Control Strategy Comparison

| Control Method | Settling Time | Overshoot | Step Response | Implementation |
|---|---|---|---|---|
| Standard PID | 8.0s | 18% | Slow | Current |
| MPC | 5.0s | 8% | Medium | 2026 Q3 |
| B★ Adaptive AI | **3.5s** | **3%** | **Fast** | 2026 Q4 |

## 5.3 Annual Energy Performance (P1 basis)

| Season | Avg COP | Uptime (%) | Generation (kWh) |
|---|---|---|---|
| Q1 (Winter) | 6.7 | 97.2 | 59,470 |
| Q2 (Spring) | 7.1 | 98.1 | 61,286 |
| Q3 (Summer) | 7.4 | 97.8 | 62,993 |
| Q4 (Autumn) | 7.0 | 97.8 | 61,800 |
| **Annual** | **7.1** | **97.7%** | **245,549** |

## 5.4 ESD Emergency Shutdown (SIL-2)

5 trigger conditions: ①HP exceedance (>115 bar) ②LP deficiency (<22 bar) ③CO₂ leak (>1%LEL) ④Compressor overheat (>110°C) ⑤Vibration anomaly (>15 mm/s)
Response time: <100ms (IEC 61511 SIL-2 compliant)

## 5.5 Cybersecurity (IEC 62443)

- Zone 0~1: Air-gap or unidirectional data diode
- Zone 2~3 boundary: DMZ firewall + Deep Packet Inspection
- Zone 4: Zero Trust architecture + mTLS
- Annual penetration testing (KISA-certified vendor)

## 5.6 DR & Energy Trading Integration

- KEPCO AMI linkage: Load adjustment based on real-time TOU pricing
- KPX DR registration: ₩27.7M/year revenue
- K-ETS carbon credit: 320 tCO₂/yr → ₩4.8M/yr

## 5.7 AI Predictive Maintenance & Digital Twin

- LSTM model: RUL prediction accuracy ±5%
- 30-day early warning: PCHE pinch-point degradation detection
- Digital Twin sync cycle: 15-minute real-data update
- With AI PdM: uptime 97.7% → 99.1%

*Final review: GilbertKwak | 2026-03-19*
