import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("../data/808_alpha_shift_dataset.csv")

# Features to analyze
epsilon = 1e-12
df["log10_Coupling_eV"] = np.log10(df["Coupling_eV"] + epsilon)
#df = df[df["log10_J_cdft"] > -4].copy()
X_cols = ["log10_Coupling_eV","FeFe_Dist_Ang", "NN_Dist_1_Ang", "Min_HeavyDist_Ang",
          "dz", "dx", "dy", "cos_theta",
          "cos_4phi", "sin_4phi", "cos_4psi", "sin_4psi",
          "d_lateral", "cos_4alpha", "sin_4alpha",
          "S12_sq", "log_absS12", "absS12"]
#print(len(df["log10_Coupling_eV"]))
# Optionally include target to see feature–target correlations too
# corr_cols = X_cols + ["log10_J_cdft"]
corr_cols = X_cols

# Subset and drop rows with NaNs in these columns
corr_df = df[corr_cols].dropna()

# Compute correlation matrix
corr_matrix = corr_df.corr()

print("Correlation matrix:\n", corr_matrix)

# Plot heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(corr_matrix,
            annot=True,
            fmt=".2f",
            cmap="coolwarm",
            cbar=True,
            square=True)

plt.title("Feature Correlation Matrix")
plt.tight_layout()

# Save heatmap
plt.savefig("../Figure/808_alphashift_log10_coupling_eV_feature_correlation.png",
            dpi=300,
            bbox_inches="tight")
plt.show()
