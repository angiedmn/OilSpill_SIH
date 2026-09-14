# OilTrace — Explainable Maritime Pollution Forensics

<p align="center">

  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">

  <img src="https://img.shields.io/badge/PyTorch-Deep%20Learning-EE4C2C?style=for-the-badge&logo=pytorch&logoColor=white" alt="PyTorch">

  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV">

  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi&logoColor=white" alt="FastAPI">

  <img src="https://img.shields.io/badge/Leaflet-Interactive%20Maps-199900?style=for-the-badge&logo=leaflet&logoColor=white" alt="Leaflet">

  <img src="https://img.shields.io/badge/MongoDB-Atlas-47A248?style=for-the-badge&logo=mongodb&logoColor=white" alt="MongoDB">

  <img src="https://img.shields.io/badge/Supabase-Storage-3FCF8E?style=for-the-badge&logo=supabase&logoColor=white" alt="Supabase">

  <img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Pandas">

  <img src="https://img.shields.io/badge/NumPy-Numerical%20Computing-013243?style=for-the-badge&logo=numpy&logoColor=white" alt="NumPy">

</p>

<p align="center">

  <img src="https://img.shields.io/badge/OpenDrift-Ocean%20Drift%20Modelling-1565C0?style=for-the-badge" alt="OpenDrift">

  <img src="https://img.shields.io/badge/OpenOil-Oil%20Spill%20Modelling-1976D2?style=for-the-badge" alt="OpenOil">

  <img src="https://img.shields.io/badge/CMEMS-Oceanographic%20Data-005BBB?style=for-the-badge" alt="CMEMS">

  <img src="https://img.shields.io/badge/Sentinel--1-SAR-003399?style=for-the-badge" alt="Sentinel-1">

  <img src="https://img.shields.io/badge/AIS-Maritime%20Intelligence-263238?style=for-the-badge" alt="AIS">

</p>

---

## Overview

**OilTrace** is an explainable maritime pollution forensics system designed to support the investigation of suspected oil spills.

The system combines **satellite-based computer vision, geospatial analysis, oceanographic drift modelling, historical AIS intelligence, and evidence-based vessel ranking** into a unified investigation workflow.

Instead of stopping at oil-spill detection, OilTrace attempts to answer the complete investigative chain:

> **What is the spill? → Where is it? → Where could it have originated? → Where could it move next? → Which vessels were relevant? → Why is a vessel ranked highly?**

Built for **Smart India Hackathon 2026**, OilTrace is a working prototype demonstrating this end-to-end investigative pipeline on a controlled real-data scenario.

> **Important:** OilTrace is a decision-support and investigation-prioritisation system. A vessel ranking represents evidence correlation and does **not** establish legal guilt, causation, or confirmed discharge.

---

# Problem

Illegal or accidental oil discharges at sea are difficult to investigate because the visible slick is often displaced from its original release location.

Investigators may need to correlate multiple evidence sources:

- Satellite imagery
- Ocean currents
- Wind and meteorological forcing
- Historical vessel movements
- AIS gaps and trajectory behaviour
- Geographic and temporal relationships

Traditional workflows often require these evidence layers to be analysed separately.

OilTrace connects them into a single explainable pipeline.

---

# Proposed Solution

OilTrace follows a six-stage forensic workflow:

```text
Satellite SAR Imagery
        │
        ▼
┌──────────────────────────┐
│ M1 — AI Detection        │
│ U-Net + ResNet18         │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ M2 — Spill               │
│ Characterisation         │
│ Geometry + GeoJSON       │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ M3 — Physics Drift       │
│ OpenDrift + OpenOil      │
│ CMEMS currents + winds   │
└────────────┬─────────────┘
             │
             ├──────────────► Forward Forecast
             │
             ▼
┌──────────────────────────┐
│ M4 — AIS Intelligence    │
│ Spatial + Temporal       │
│ Filtering + Trajectory   │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ M5 — Evidence            │
│ Attribution & Ranking    │
└────────────┬─────────────┘
             │
             ▼
┌──────────────────────────┐
│ M6 — Investigation       │
│ Dashboard                │
└──────────────────────────┘
M1 — Satellite Oil-Spill Detection

The first stage detects suspected oil slicks from SAR imagery.

Pipeline
SAR Image
   ↓
Preprocessing
   ↓
U-Net Segmentation
   ↓
Oil Probability Map
   ↓
Thresholding
   ↓
Binary Spill Mask
Technology
PyTorch
U-Net
ResNet18 encoder
OpenCV
Albumentations
Output
{
  "image_id": "palsar_0",
  "detected": true,
  "confidence": 0.86,
  "mask_path": "...",
  "bbox": [...]
}

The segmentation mask becomes the geographic input for the next stage.

M2 — Spill Characterisation & Geospatial Analysis

This module converts the detected pixel-level spill mask into geographic information.

Input
M1 Spill Mask
+
Geographic Extent / Georeferencing
+
Observation Timestamp
Processing
Binary Mask
     ↓
Contour Extraction
     ↓
Pixel → Geographic Coordinates
     ↓
Shapely Polygon
     ↓
Geometric Analysis
Calculated Properties
Spill centroid
Area
Perimeter
Length
Width
Bounding box
Orientation
GeoJSON geometry
Example
{
  "centroid": [72.68922, 18.85225],
  "area_km2": 15.96,
  "perimeter_km": 20.55,
  "length_km": 9.47,
  "width_km": 2.52,
  "geometry": {...}
}

The resulting georeferenced spill polygon is passed to the physics drift engine.

M3 — Ocean Drift Reconstruction & Forecasting

OilTrace uses physics-based particle modelling to reconstruct the possible movement of the detected slick.

Technology
OpenDrift
OpenOil
CMEMS oceanographic data
Ocean currents
Wind forcing
NumPy
NetCDF-based environmental data
Backward Hindcast

The detected spill polygon is used to seed particles.

Observed Spill Polygon
        ↓
Particle Seeding
        ↓
Ocean Currents + Wind
        ↓
Backward Hindcast
        ↓
Probable Origin Region
        ↓
Estimated Source-Time Window
Forward Forecast

The same modelling framework is used to estimate the future movement of the slick.

Current Spill
      ↓
Current + Wind Forcing
      ↓
Forward Particle Simulation
      ↓
Predicted Drift Path
      ↓
Potential Future Impact Areas
Output
Probable origin centroid
Probable origin bounding box
Estimated source time
Hindcast trajectory
Forecast trajectory
AIS query region and time window

The drift model provides a probable origin region and trajectory rather than claiming an exact release point.

M4 — AIS Vessel Intelligence

M4 correlates the probable origin region and source-time window with historical AIS data.

Pipeline
Historical AIS
      ↓
Data Cleaning
      ↓
Spatial Filtering
      ↓
Temporal Filtering
      ↓
Candidate Vessel Selection
      ↓
Trajectory Reconstruction
      ↓
AIS Behaviour & Gap Analysis
Analysed Features
MMSI
IMO
Vessel name
Vessel type
Latitude / longitude
SOG
COG
Heading
Observation count
First / last observation
AIS gaps
Maximum AIS gap
Speed statistics
Trajectory characteristics
Vessel dimensions and metadata where available
Why Filtering Matters

Instead of comparing the spill against every vessel in the dataset:

All AIS Traffic
       ↓
Origin Region Filter
       ↓
Source-Time Filter
       ↓
Relevant Vessel Candidates

This reduces irrelevant maritime traffic before evidence scoring.

M5 — Explainable Evidence Attribution

M5 ranks candidate vessels using multiple independent evidence dimensions.

Evidence Model
Evidence	Weight
Spatial proximity	30%
Temporal consistency	25%
Trajectory consistency	20%
Drift consistency	15%
Vessel / AIS evidence	10%
Concept
Candidate Vessel
       │
       ├── Spatial Evidence
       ├── Temporal Evidence
       ├── Trajectory Evidence
       ├── Drift Consistency
       └── AIS / Vessel Evidence
                │
                ▼
        Weighted Evidence Score
                │
                ▼
        Ranked Candidate List
                │
                ▼
        Human-readable Explanation

The system therefore does not simply return:

"Nearest vessel = culprit"

Instead, it provides an evidence-backed ranking explaining why a candidate received its score.

Example
Rank #1
Vessel: MT MUMBAI EXPRESS_99

Overall Evidence Score: 97.65
Confidence: HIGH

Spatial consistency:   97.94
Temporal consistency:  95.36
Trajectory consistency:98.45
Drift consistency:     98.27
AIS/Vessel evidence:   100.00

Scores indicate investigative priority and evidence correlation. They do not constitute legal attribution.

M6 — Investigation Dashboard

OilTrace brings the detection, geospatial analysis, drift reconstruction, AIS correlation, and evidence scoring stages into a unified investigation interface.

Investigation Dashboard

OilTrace brings the detection, geospatial analysis, drift reconstruction,
AIS correlation, and evidence scoring stages into a unified investigation
interface.

Incident Investigation

Interactive dashboard for exploring individual slicks, their area, origin and detection confidence, while viewing ranked vessel candidates and corresponding evidence scores.

<img width="1100" height="600" alt="OilTrace Incident Investigation Dashboard" src="https://github.com/user-attachments/assets/75fdcadb-d036-4669-9af5-c5f2dd161514" />
Evidence Breakdown

Presents the evidence contributing to the ranking of potential vessel
candidates, enabling investigators to understand why a candidate is
flagged.

<img width="1100" height="600" alt="OilTrace Evidence Breakdown" src="https://github.com/user-attachments/assets/5dba5a86-352b-4d38-91f8-fbfc2d0764d0" />
High-Risk Probability Zones

Visualises areas associated with higher estimated probability of spill
origin, supporting prioritisation during investigation.

<img width="1100" height="600" alt="OilTrace High Risk Probability Zones" src="https://github.com/user-attachments/assets/09c442f3-1724-42ba-a953-6486838cb4d7" />
Predicted Spill Spread

Displays the predicted evolution and spatial spread of the slick based on
the drift modelling stage.

<img width="1100" height="600" alt="OilTrace Predicted Spill Spread" src="https://github.com/user-attachments/assets/3136a0e9-a23a-4fc7-883f-e9fe7cdb012e" />
Sensitive Zone Detection

Highlights sensitive coastal or maritime zones located near the predicted
spill trajectory, supporting environmental risk assessment.

<img width="1100" height="600" alt="OilTrace Sensitive Zone Detection" src="https://github.com/user-attachments/assets/43aa4a19-8dbb-40cd-88ea-29c5e600d94d" />
Technology Stack
Artificial Intelligence & Computer Vision










U-Net
ResNet18
Segmentation Models PyTorch
Albumentations
Geospatial








Shapely
GeoJSON
PyProj
Geographic coordinate transformations
Oceanography & Physics






OpenDrift
OpenOil
Copernicus Marine Service (CMEMS)
Ocean current forcing
Wind forcing
Particle-based drift simulation
Hindcasting
Forecasting
Maritime Intelligence




Historical AIS
Spatial filtering
Temporal filtering
Vessel trajectory reconstruction
AIS gap analysis
Vessel behavioural indicators
Backend




FastAPI
REST APIs
JSON-based module communication
Frontend








Leaflet
JavaScript
HTML5
CSS3
Storage




MongoDB Atlas
Supabase Storage
JSON
GeoJSON
CSV
Data Sources

OilTrace is designed around openly accessible and modular data sources.

🛰️ Sentinel-1 SAR

Used for detecting suspected oil slicks from radar imagery.

🌊 Copernicus Marine Service

Used for oceanographic forcing including:

Ocean currents
Wind / meteorological forcing
Forecast and reanalysis products where available
🚢 AIS Data

Used for:

Vessel traffic reconstruction
Spatial correlation
Temporal correlation
Trajectory analysis
Vessel candidate generation
🌍 Additional Data Sources

The architecture can be extended to incorporate:

ISRO MOSDAC resources
Global Fishing Watch
NOAA maritime datasets
Additional Sentinel-1 oil-spill datasets
Regional marine and meteorological datasets
Data Flow
                    DATA INGESTION
                         │
          ┌──────────────┼──────────────┐
          ↓              ↓              ↓
      Sentinel-1       CMEMS           AIS
          │              │              │
          ↓              ↓              │
    ┌──────────┐         │              │
    │    M1    │         │              │
    │Detection │         │              │
    └────┬─────┘         │              │
         ↓               │              │
    ┌──────────┐         │              │
    │    M2    │         │              │
    │Geometry  │         │              │
    └────┬─────┘         │              │
         ↓               ↓              │
    ┌─────────────────────────┐          │
    │          M3             │          │
    │  OpenDrift + OpenOil    │          │
    │  Hindcast + Forecast    │          │
    └───────────┬─────────────┘          │
                │                        │
                │ Origin + Time Window  │
                └────────────────────────┤
                                         ↓
                                  ┌──────────────┐
                                  │      M4      │
                                  │ AIS Analysis │
                                  └──────┬───────┘
                                         ↓
                                  ┌──────────────┐
                                  │      M5      │
                                  │  Evidence    │
                                  │   Scoring    │
                                  └──────┬───────┘
                                         ↓
                                  ┌──────────────┐
                                  │      M6      │
                                  │ Investigation│
                                  │   Dashboard  │
                                  └──────────────┘
Module Handoff
Module	Input	Output	Key Question
M1	SAR imagery	Spill mask + confidence	What is the spill?
M2	Spill mask + georeferencing	GeoJSON + geometry	Where exactly is it?
M3	Spill polygon + timestamp + CMEMS	Origin + hindcast + forecast	Where did it come from and where could it go?
M4	Origin/time + historical AIS	Candidate vessels + trajectories	Who was there?
M5	AIS evidence + drift evidence	Ranked vessels + explanations	Why is this candidate relevant?
M6	All module outputs	Investigation dashboard	How can an investigator understand it?
Repository Structure
OilTrace/
│
├── modules/
│   │
│   ├── detection/
│   │   ├── pipeline.py
│   │   ├── train.py
│   │   ├── evaluate.py
│   │   └── scripts/
│   │
│   ├── geospatial/
│   │   ├── spill_characterisation.py
│   │   ├── process_real_detections.py
│   │   └── process_mongo_detections.py
│   │
│   ├── drift/
│   │   ├── pipeline.py
│   │   ├── metocean.py
│   │   └── ...
│   │
│   ├── AIS/
│   │   └── src/
│   │       ├── cleaning.py
│   │       ├── spatial_filter.py
│   │       ├── trajectory.py
│   │       ├── features.py
│   │       ├── gap_analysis.py
│   │       ├── candidate_gap_analysis.py
│   │       └── evidence.py
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
├── data/
│
└── README.md
Key Outputs
Detection
outputs/spill/all_detections.json

Contains:

image ID
detection status
confidence
mask path
bounding box
Geospatial Characterisation
outputs/geospatial/spill_metadata.json

Contains:

centroid
area
perimeter
length
width
bounding box
GeoJSON geometry
Drift
outputs/drift/drift_simulation_result.json

Contains:

simulation information
origin estimation
estimated spill time
hindcast
forecast
AIS query parameters
AIS Evidence
outputs/AIS/m4_evidence.json

Contains:

candidate vessel
spatial evidence
temporal evidence
trajectory
behaviour
AIS gaps
evidence notes
Attribution
outputs/scoring/ranked_vessels.json

Contains:

vessel ranking
overall score
component scores
confidence
explanation
Explainability

OilTrace is designed around explainable evidence fusion.

Instead of producing an opaque prediction, the system exposes the evidence contributing to a candidate ranking.

For every candidate vessel, investigators can inspect:

Spatial relationship
        +
Temporal relationship
        +
Trajectory consistency
        +
Drift consistency
        +
AIS / vessel evidence
        ↓
Overall Evidence Score
        ↓
Human-readable Explanation

This allows the system to function as an investigation prioritisation tool rather than a black-box accusation engine.

Current Prototype Scope

The current implementation demonstrates the complete pipeline on a controlled real-data scenario.

The computationally expensive drift stage is currently applied to a selected subset of detected slicks, allowing the prototype to demonstrate the complete investigative workflow without requiring full-scale operational processing.

The system is therefore intended as a working research/prototype system, not a production maritime surveillance platform.

Challenges & Mitigations
SAR Look-alikes

Calm-water areas, biogenic slicks, wakes and other phenomena can resemble oil in SAR imagery.

Mitigation
Training with oil-spill and look-alike samples
Segmentation confidence
Geometric filtering
Human investigator review
AIS Gaps and Spoofing

AIS can contain missing observations, transmission gaps, coverage limitations or manipulated information.

Mitigation
AIS gap analysis
Historical trajectory reconstruction
Multi-source evidence
Satellite-based confirmation
Evidence confidence indicators
Drift Uncertainty

Ocean currents and wind introduce uncertainty into the reconstructed source location and future trajectory.

Mitigation
Particle-based simulation
Origin regions instead of single-point attribution
Forward and backward modelling
Uncertainty-aware visualisation
Definitive Attribution

Correlation between a vessel and a spill does not establish legal causation.

Mitigation

OilTrace provides:

Ranked investigation candidates, not legal accusations.

Final attribution remains subject to investigation and independent evidence.

Future Scope

OilTrace can be extended from a research prototype into a broader maritime environmental intelligence platform.

1. Near-Real-Time Monitoring

Integrate automated ingestion pipelines for:

New Sentinel-1 acquisitions
AIS streams
Updated oceanographic forecasts
Meteorological data

This would reduce manual data preparation and enable faster incident triage.

2. Improved Spill-Age Estimation

Currently, source timing is estimated through drift modelling and the selected hindcast window.

Future versions can evaluate multiple release-time hypotheses:

6h → 9h → 12h → 15h → 18h → 24h
              ↓
      Drift consistency
              ↓
   Plausible release window

Future research could additionally incorporate:

Multi-temporal satellite observations
Oil weathering models
Spectral information
Environmental conditions
Physical/chemical oil properties

to improve release-age estimation.

3. Advanced Behavioural Anomaly Detection

AIS analysis can be extended with explicit behavioural anomaly models using:

Speed deviations
Heading changes
Route deviations
Unusual stops
AIS transmission gaps
Historical vessel behaviour
Vessel-specific behavioural baselines

Potential future approaches include:

Statistical anomaly detection
Isolation Forest
Autoencoders
Sequence models
Graph-based vessel behaviour modelling
4. Probabilistic Attribution

Future versions can replace fixed weighted scoring with probabilistic evidence fusion.

Potential approaches:

Bayesian inference
Probabilistic graphical models
Calibrated ranking models
Evidence confidence propagation

This would allow uncertainty from the satellite, drift and AIS stages to propagate through the complete pipeline.

5. Multi-Sensor Satellite Fusion

Integrate additional remote-sensing sources such as:

Sentinel-2 optical imagery
SAR from additional satellites
Hyperspectral imagery
Thermal observations

Multi-sensor fusion can help distinguish oil slicks from SAR look-alikes and improve spill characterisation.

6. Automated Sensitive-Zone Risk Assessment

The existing dashboard can be extended to incorporate authoritative spatial datasets for:

Marine protected areas
Fisheries
Aquaculture
Coral reefs
Mangroves
Coastal infrastructure
Ports
Ecologically sensitive regions

The system could then calculate:

Predicted Spill Trajectory
          +
Sensitive Marine Assets
          ↓
Potential Impact Assessment
7. Nationwide Coastal Monitoring

The architecture can eventually support automated monitoring across larger geographic regions.

Regional Monitoring
        ↓
Multiple Spill Events
        ↓
Central Incident Database
        ↓
National Maritime Monitoring
8. Continuous Model Improvement

Validated investigation outcomes can be fed back into the detection and ranking pipeline to improve:

SAR segmentation
Look-alike discrimination
Drift calibration
Vessel behaviour modelling
Evidence scoring

The goal is continuous model improvement from validated incidents, rather than unverified automated learning.

9. Automated Evidence Reports

Future versions could generate standardized investigation reports containing:

Satellite evidence
Spill geometry
Detection confidence
Origin probability region
Drift trajectories
AIS vessel history
Evidence score
Timeline
Supporting maps

This would make the output easier to share with investigators and response agencies.

Potential Impact
🚨 Law Enforcement

Helps investigators narrow large volumes of maritime traffic into evidence-backed candidate lists.

🌊 Environmental Response

Supports understanding of predicted slick movement and potential impact areas.

🐟 Fisheries & Aquaculture

Can help identify areas potentially exposed to future spill movement.

🏝️ Coastal Protection

Supports prioritisation of sensitive coastal and marine regions.

🛰️ Maritime Surveillance

Combines satellite observations with vessel intelligence and oceanographic modelling.

📊 Decision Support

Transforms multiple heterogeneous datasets into an explainable investigation workflow.

Why OilTrace?

Existing technologies and research already provide individual capabilities such as satellite oil-spill detection, vessel tracking and ocean drift modelling.

OilTrace focuses on connecting these capabilities into a unified workflow:

AI Detection
     ↓
Geospatial Characterisation
     ↓
Physics-Based Source Reconstruction
     ↓
AIS Intelligence
     ↓
Explainable Evidence Fusion
     ↓
Investigation Dashboard
Core USP

Existing technologies provide individual evidence layers; OilTrace connects those layers into an explainable end-to-end forensic workflow.

Key Differentiators
End-to-end investigation pipeline
AI + Physics + AIS integration
Bidirectional drift intelligence
Spatial + temporal vessel correlation
AIS trajectory and gap analysis
Multi-factor explainable evidence scoring
Human-readable candidate explanations
Integrated investigation dashboard
Future spill-risk and sensitive-zone visualisation
Limitations

OilTrace is a research prototype and has several limitations:

SAR imagery can contain oil-spill look-alikes.
AIS data can be incomplete or inaccurate.
Oceanographic drift models contain uncertainty.
Public AIS availability can vary by region and provider.
Source-time estimation is model-dependent.
Candidate ranking does not prove causation.
Operational deployment would require validated data pipelines, calibration and domain-expert evaluation.

These limitations are explicitly considered in the system design.

Disclaimer

OilTrace is intended for research, environmental monitoring and investigative decision support.

A high-ranked vessel represents a potential investigation candidate based on correlated evidence. It does not establish that the vessel caused or committed an oil discharge.

Final attribution requires independent investigation, authoritative data and appropriate legal and scientific validation.

Smart India Hackathon 2026

Developed as a prototype for Smart India Hackathon 2026.

Theme

Maritime Pollution Forensics / Oil Spill Detection and Attribution

Approach

Detect → Characterise → Reconstruct → Correlate → Rank → Investigate

Team

Developed by:

[Your Team Name]

Contributors
M1 — Satellite Detection & Computer Vision
M2 — Spill Characterisation & Geospatial Analysis
M3 — Ocean Drift Modelling
M4 — AIS Intelligence
M5 — Evidence Scoring & Attribution
M6 — Dashboard & Integration
Acknowledgements

OilTrace builds upon open-source technologies and publicly available scientific data including:

Sentinel-1
Copernicus Marine Service
OpenDrift
OpenOil
PyTorch
OpenCV
FastAPI
Leaflet
MongoDB
Supabase
License

This project is intended for research and educational purposes.

Add your chosen license here, for example:

MIT License
<p align="center">
🛰️ AI + 🌊 Physics + 🚢 AIS
From Spill Detection to Explainable Maritime Forensics

OilTrace — Detect. Reconstruct. Correlate. Investigate.

</p> ```
