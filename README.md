# Multi-Scale Electronic Coupling Prediction using SOAP and Machine Learning

This repository contains machine learning workflows developed to predict electronic coupling matrix elements in molecular assemblies (e.g., metal-porphyrin dimers) from both ideal rigid structures and structurally distorted configurations sampled from molecular dynamics (MD) trajectories.

## Project Architecture & Methodology

Predicting electronic coupling across broad geometric spaces requires different structural representations depending on the degree of molecular distortion:

1. **SOAP Descriptor Pipeline (Rigid + Distorted Geometries):** 
   Utilizes Smooth Overlap of Atomic Positions (SOAP) to generate robust, local environments capable of capturing complex, multi-scale geometric fluctuations. This framework successfully handles both ideal rigid dimers and highly distorted configurations extracted from MD snapshots.
2. **Standard Descriptor Models (Rigid-Limit Only):**
   Features baseline evaluations using traditional geometric descriptors trained on Kernel Ridge Regression (KRR), Random Forest (RF), and XGBoost frameworks, optimized primarily for rigid structural scans.

---

## Repository Structure

```text
├── soap-feature/               # Local environments and atomic coordinate data
├── 05-soap-feature.ipynb       # Jupyter Notebook detailing SOAP generation and mapping
├── models/                     # [Optional folder for your KRR, RF, and XGBoost training scripts]
└── README.md                   # Project documentation
