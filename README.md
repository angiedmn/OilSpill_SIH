
---

## Investigation Dashboard

OilTrace brings the detection, geospatial analysis, drift reconstruction,
AIS correlation, and evidence scoring stages into a unified investigation
interface.
### Incident Investigation
Interactive dashboard for exploring individual slicks, their area, origin and detection confidence, while viewing ranked vessel candidates and corresponding evidence scores.


<img width="1100" height="600" alt="OilTrace Incident Investigation Dashboard" src="https://github.com/user-attachments/assets/75fdcadb-d036-4666-9af5-c5f2dd161514" />

### Evidence Breakdown
Presents the evidence contributing to the ranking of potential vessel
candidates, enabling investigators to understand why a candidate is
flagged.

<img width="1100" height="600" alt="OilTrace Evidence Breakdown" src="https://github.com/user-attachments/assets/5dba5a86-352b-4d38-91f8-fbfc2d0764d0" />

### High-Risk Probability Zones
Visualises areas associated with higher estimated probability of spill
origin, supporting prioritisation during investigation.

<img width="1100" height="600" alt="OilTrace High Risk Probability Zones" src="https://github.com/user-attachments/assets/09c442f3-1724-42ba-a953-6486838cb4d7" />

### Predicted Spill Spread
Displays the predicted evolution and spatial spread of the slick based on
the drift modelling stage.

<img width="1100" height="600" alt="OilTrace Predicted Spill Spread" src="https://github.com/user-attachments/assets/3136a0e9-a23a-4fc7-883f-e9fe7cdb012e" />

### Sensitive Zone Detection
Highlights sensitive coastal or maritime zones located near the predicted
spill trajectory, supporting environmental risk assessment.

<img width="1100" height="600" alt="OilTrace Sensitive Zone Detection" src="https://github.com/user-attachments/assets/43aa4a19-8dbb-40cd-88ea-29c5e600d94d" />





## Current Progress

### Detection

* U-Net with a ResNet-18 backbone
* Deep-SAR Oil Spill Segmentation (refined) dataset
* Validation: **Dice 0.76, IoU 0.65**
* Binary segmentation masks with GeoJSON and JSON metadata outputs
* Confidence-based filtering and area thresholding to reduce false positives

### Geospatial Characterisation

* Converts detected slicks into real-world geometry
* Calculates centroid, area, perimeter, length, width, and orientation
* Validated against raw detection masks
* Outputs standardised GeoJSON and JSON for downstream modules

### Drift, AIS, Attribution & Dashboard

Currently in development.

---

## Demo Scenario

**Region:** Arabian Sea corridor off Mumbai
**Coordinates:** 72.50°E, 18.80°N
**SAR scenes processed:** 1,615
**Detected slicks:** 1,548
**Clean-water controls:** 67

The controlled scenario is used to demonstrate the complete investigative workflow and module integration.

---

## Tech Stack

| Layer               | Technologies                        |
| ------------------- | ----------------------------------- |
| Detection           | PyTorch, U-Net, OpenCV              |
| Geospatial          | Shapely, GeoPandas, Rasterio, GeoPy |
| Coordinates         | WGS84 / EPSG:4326                   |
| Time                | UTC ISO-8601                        |
| Data Exchange       | GeoJSON, JSON                       |
| Vessel Intelligence | AIS data                            |

---

## Team Structure

| Member | Module                         |
| ------ | ------------------------------ |
| M1     | Oil Spill Detection            |
| M2     | Geospatial Characterisation    |
| M3     | Ocean Drift Modelling          |
| M4     | AIS / Vessel Intelligence      |
| M5     | Evidence Scoring & Attribution |
| M6     | Investigation Dashboard        |

---

## Why It Matters

Operational systems such as EMSA's CleanSeaNet demonstrate that satellite, oceanographic, and AIS data can support real-world maritime pollution investigations.

OilTrace focuses on building a **transparent, explainable, and modular prototype** that connects these stages into a single investigative workflow using publicly accessible data.

The current prototype establishes the core architecture. Future development will focus on improving detection accuracy, expanding data coverage, strengthening drift and attribution models, and increasing system robustness.

---

## Disclaimer

OilTrace is a research and demonstration prototype. Vessel rankings represent **investigation candidates based on available evidence** and should not be interpreted as proof of responsibility or used as an automated legal or enforcement decision.
