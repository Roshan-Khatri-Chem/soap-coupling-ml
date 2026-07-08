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
Getting Started
Prerequisites
To run the SOAP feature engineering notebook and machine learning models, you need the following Python libraries installed:
pip install dscribe scikit-learn xgboost numpy pandas matplotlib jupyter

Feature Generation Flow
MD Geometry Parsing: Extracts snapshots from molecular dynamics configurations.
SOAP Generation (05-soap-feature.ipynb): Configures atomic environment parameters (cutoff distance, regularizing Gaussian width, and expansion orders) using the dscribe library to compute the structural power spectrum.
Model Training: Maps the generated high-dimensional SOAP vectors to target electronic coupling values using regression frameworks.

Contact & Citation
Roshan Khatri
Ph.D. Candidate, Computational Chemistry
Kent State University
Advisor: Prof. Barry D. Dunietz
