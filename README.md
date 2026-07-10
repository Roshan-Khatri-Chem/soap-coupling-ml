```markdown
# Multi-Scale Electronic Coupling Prediction using SOAP and Physics-Informed Machine Learning

This repository contains machine learning workflows developed to predict electronic coupling matrix elements in molecular assemblies (e.g., metal-porphyrin dimers) from both ideal rigid structures and structurally distorted configurations sampled from molecular dynamics (MD) trajectories.

---

## Project Architecture & Methodology

Predicting electronic coupling across broad geometric spaces requires different structural representations depending on the degree of molecular distortion:

* **SOAP Descriptor Pipeline (Rigid + Distorted Geometries):** Utilizes the Smooth Overlap of Atomic Positions (SOAP) framework to generate robust, local environments capable of capturing complex, multi-scale geometric fluctuations. This framework successfully handles both ideal rigid dimers and highly distorted configurations extracted from MD snapshots.
* **Standard Descriptor Models (Rigid-Limit Only):** Features baseline evaluations using traditional geometric descriptors trained on Kernel Ridge Regression (KRR), Random Forest (RF), and XGBoost frameworks, optimized primarily for rigid structural scans.

---

## Repository Layout

```text
.
├── README.md                     # This file
├── requirements.txt              # Pip dependencies (packages to install)
├── notebooks/                    # 5 sequential teaching notebooks (start here)
│   ├── README.md                 # Overview of notebook objectives
│   ├── 01_distribution_plot.ipynb
│   ├── 02_classification_model.ipynb
│   ├── 03_krr_regression_model.ipynb
│   ├── 04_soap_feature.ipynb
│   └── 05_NN_distance_test_model.ipynb
├── src/                          # Underlying Python scripts and parsing tools
│   ├── feature_correlation_plot.py # Script generating feature correlation matrices
│   └── Qchem_to_xyz.ipynb        # Utility converting raw Q-Chem outputs to structural .xyz coordinates
├── data/                         # Central training and evaluation datasets
│   └── 808_alpha_shift_dataset.csv # ★ Master dataset file (contains geometric and electronic features)
├── geometries/                   # Atomic coordinate repository
│   └── *.xyz                     # 808 systematic-scan dimer xyz structural files
├── SOAP_feature/                 # SOAP-specific features and descriptors
│   ├── *.pkl                     # Trained model files (separated by low/high electronic coupling thresholds)
│   ├── soap_feature_parity_plot.png # Feature correlation and parity performance plots
│   └── results_summary.txt       # Train, validation, and test partition performance logs
└── results/                      # Production Kernel Ridge Regression (KRR) data
    ├── *.pkl                     # Serialized KRR trained model weight artifacts
    ├── *.png                     # Model predictive parity and analysis visualization plots
    └── *.csv                     # Tabulated model error residuals and prediction arrays
```
*(★ = The master dataset file required to train or evaluate any local model variant.)*

---

## Performance Summary

### 1. SOAP Feature KRR Model
```text
==================================================
   KRR DIMER MODEL TRAINING REPORT: SOAP FEATURES
==================================================
Optimal Hyperparameters: {'alpha': 0.0001, 'gamma': 1e-05}

Dataset Phase            | R² Score   | RMSE       | MAE
--------------------------------------------------
Train                    | 0.9604     | 0.1472     | 0.0948
Validation (CV Mean)     | 0.6884     | 0.4137     | 0.2686
Test (Hold-Out)          | 0.6101     | 0.4667     | 0.2915
==================================================
```

### 2. Physical 6-Descriptor KRR Model
```text
==================================================
  KRR DIMER MODEL TRAINING REPORT (6 DESCRIPTORS)
==================================================
Dataset Phase            | R² Score   | MAE
--------------------------------------------------
Train                    | 0.8469     | 0.1869
Validation (CV Mean)     | 0.7662     | 0.2240
Test (Hold-Out)          | 0.7546     | 0.2380
==================================================
```
*Note: The 6-descriptor model shows excellent generalization with minimal performance drop-off between validation and hold-out testing phases.*

---

## Prerequisites

To run the SOAP feature engineering notebooks and machine learning workflows, install the required libraries:

```bash
pip install dscribe scikit-learn xgboost numpy pandas matplotlib jupyter
```

---

## Feature Generation Flow

1. **MD Geometry Parsing:** Extracts snapshots from molecular dynamics configurations.
2. **SOAP Generation (`04_soap_feature.ipynb`):** Configures atomic environment parameters (cutoff distance, regularizing Gaussian width, and expansion orders) using the `dscribe` library to compute the structural power spectrum.
3. **Model Training:** Maps the generated high-dimensional SOAP vectors to target electronic coupling values using regression frameworks.

---

## Contact & Citations

**Roshan Khatri** Ph.D. Candidate, Computational Chemistry  
Kent State University  
Email: rkhatri2@kent.edu  
Advisor: Prof. Barry D. Dunietz  
```
