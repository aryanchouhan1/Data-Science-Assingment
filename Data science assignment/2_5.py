import numpy as np


def identify_outliers_zscore(data, threshold=2):
    z_scores = np.abs((data - np.mean(data)) / np.std(data))
    outliers = np.where(z_scores > threshold)
    return outliers


# Example usage
data = np.array([1, 2, 3, 4, 500, 10])
outliers_zscore = identify_outliers_zscore(data)
print("Outliers indices (Z-Score):", data[outliers_zscore])
