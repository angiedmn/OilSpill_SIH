# OilTrace — Explainable Maritime Pollution Forensics

OilTrace is an end-to-end maritime pollution investigation prototype that combines **Satellite SAR imagery, Geospatial Analysis, Ocean Drift Modelling, AIS vessel intelligence, and Explainable Evidence Scoring** to investigate the probable origin of oil spills.

Built for **Smart India Hackathon 2026**, OilTrace demonstrates how multiple evidence sources can be connected into a unified forensic workflow.

> **AI + Physics + AIS — one forensic pipeline.**

---
<p align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![OpenDrift](https://img.shields.io/badge/OpenDrift-1565C0?style=for-the-badge)
![OpenOil](https://img.shields.io/badge/OpenOil-1976D2?style=for-the-badge)
![CMEMS](https://img.shields.io/badge/CMEMS-005BBB?style=for-the-badge)
![AIS](https://img.shields.io/badge/AIS-Maritime%20Data-263238?style=for-the-badge)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Leaflet](https://img.shields.io/badge/Leaflet-199900?style=for-the-badge&logo=leaflet&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)
![Supabase](https://img.shields.io/badge/Supabase-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white)

</p>

## 🔎 Project Overview

Illegal oil discharges at sea are difficult to investigate because an observed slick may have drifted significantly from its original release location. AIS data can also contain gaps, irregularities, or incomplete vessel information.

OilTrace addresses this by connecting:

**Satellite Detection → Spill Characterisation → Drift Reconstruction → AIS Correlation → Evidence Scoring → Investigation Dashboard**

The system produces **ranked investigation candidates with explainable evidence**, rather than making an automated accusation.

---

# 🏗️ Three-Layer Architecture

OilTrace is organised into three major architectural layers.

### Layer 1 — Detection & Characterisation

Identifies and measures the detected oil slick.

- Sentinel-1 / SAR imagery
- U-Net + ResNet-18 segmentation
- Binary oil-spill masks
- GeoJSON generation
- Centroid and bounding box
- Area, perimeter, length, width and orientation

**Output:** Structured spill geometry and metadata.

---

### Layer 2 — Reconstruction & Intelligence

Reconstructs the possible movement and identifies vessels associated with the probable origin.

- Ocean current and wind data
- OpenDrift / OpenOil simulation
- Forward and backward drift modelling
- Probable origin estimation
- AIS spatial and temporal correlation
- Vessel trajectory reconstruction
- AIS gap and movement analysis

**Output:** Probable origin zones and vessel evidence.

---

### Layer 3 — Attribution & Investigation

Combines evidence into an interpretable investigation result.

- Spatial evidence
- Temporal evidence
- Trajectory evidence
- Drift consistency
- AIS quality
- Weighted evidence scoring
- Ranked vessel candidates
- Interactive investigation dashboard

**Output:** Explainable candidate ranking for investigators.

---

# 🔄 End-to-End Pipeline

```text
┌─────────────────────┐
│   SAR Satellite     │
│      Imagery        │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ M1: Spill Detection │
│   U-Net + ResNet18  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ M2: Geospatial      │
│ Characterisation    │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ M3: Ocean Drift     │
│ Hindcast / Forecast │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ M4: AIS Intelligence│
│ Vessel Correlation  │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ M5: Evidence Scoring│
│ & Attribution       │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│ M6: Investigation   │
│     Dashboard       │
└─────────────────────┘
```

# 📁 Project Structure
```
OilTrace/
│
├── modules/
│   ├── detection/
│   │   ├── pipeline.py
│   │   └── ...
│   │
│   ├── geospatial/
│   │   ├── spill_characterisation.py
│   │   ├── process_real_detections.py
│   │   └── ...
│   │
│   ├── drift/
│   │   ├── pipeline.py
│   │   ├── metocean.py
│   │   └── ...
│   │
│   ├── AIS/
│   │   ├── src/
│   │   │   ├── cleaning.py
│   │   │   ├── spatial_filter.py
│   │   │   ├── trajectory.py
│   │   │   ├── gap_analysis.py
│   │   │   ├── features.py
│   │   │   └── evidence.py
│   │   └── run_m4_pipeline.py
│   │
│   └── attribution/
│       ├── scoring.py
│       ├── evidence.py
│       └── loaders.py
│
├── dashboard/
│   ├── backend/
│   │   └── main.py
│   │
│   └── frontend/
│       └── index.html
│
├── outputs/
│   ├── spill/
│   ├── geospatial/
│   ├── drift/
│   ├── AIS/
│   └── scoring/
│
├── run_m3_pipeline.py
├── requirements.txt
└── README.md
```
# 🖥️ Investigation Dashboard

OilTrace brings the detection, geospatial analysis, drift reconstruction,
AIS correlation, and evidence scoring stages into a unified investigation
interface.

Incident Investigation

Interactive dashboard for exploring individual slicks, their area, origin and detection confidence, while viewing ranked vessel candidates and corresponding evidence scores.

<img width="1100" height="600" alt="OilTrace Incident Investigation Dashboard" src="https://github.com/user-attachments/assets/75fdcadb-d036-4666-9af5-c5f2dd161514" />
Evidence Breakdown

Presents the evidence contributing to the ranking of potential vessel candidates, enabling investigators to understand why a candidate is flagged.

<img width="1100" height="600" alt="OilTrace Evidence Breakdown" src="https://github.com/user-attachments/assets/5dba5a86-352b-4d38-91f8-fbfc2d0764d0" />
High-Risk Probability Zones

Visualises areas associated with higher estimated probability of spill origin, supporting prioritisation during investigation.

<img width="1100" height="600" alt="OilTrace High Risk Probability Zones" src="https://github.com/user-attachments/assets/09c442f3-1724-42ba-a953-6486838cb4d7" />
Predicted Spill Spread

Displays the predicted evolution and spatial spread of the slick based on the drift modelling stage.

<img width="1100" height="600" alt="OilTrace Predicted Spill Spread" src="https://github.com/user-attachments/assets/3136a0e9-a23a-4fc7-883f-e9fe7cdb012e" />
Sensitive Zone Detection

Highlights sensitive coastal or maritime zones located near the predicted spill trajectory, supporting environmental risk assessment.

<img width="1100" height="600" alt="OilTrace Sensitive Zone Detection" src="https://github.com/user-attachments/assets/43aa4a19-8dbb-40cd-88ea-29c5e600d94d" />

# ⭐ Key Differentiators

1. End-to-End Forensic Workflow
Connects satellite detection, drift reconstruction, AIS intelligence and evidence scoring in one pipeline.

2. Bidirectional Drift Analysis
Uses both hindcast to investigate probable origin and forecast to estimate future slick movement.

3. Explainable Evidence
Candidates are ranked using interpretable evidence components instead of a black-box accusation.

4. Investigation-First Design
The system is designed around the investigator's workflow — from detecting a slick to understanding which vessels require further investigation.

5. Modular Architecture
Each stage produces structured outputs that can be independently improved or replaced.


# 🚀 Future Scope

Near-real-time satellite and AIS ingestion
Improved spill release-time / age estimation
Advanced behavioural anomaly detection
Multi-sensor SAR + optical fusion
Probabilistic vessel attribution
Expanded coastal and ecological risk assessment
Automated investigation reports
Large-scale maritime monitoring


#👨‍💻 Built for Smart India Hackathon 2026
OilTrace — Explainable Maritime Pollution Forensics
From detection to investigation — connecting AI, physics and maritime intelligence.
