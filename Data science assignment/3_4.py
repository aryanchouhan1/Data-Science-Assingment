import pandas as pd
import numpy as np

# Create a sample dataframe
np.random.seed(400)
data = pd.DataFrame({
    'variable': np.random.randn(1000),
    'response': np.random.choice([0, 1], size=1000, replace=True)
})


# Function to perform binning based on response rates
def binning_by_response_rate(data, variable, response, num_bins=5):
    # Create bins based on percentiles
    data['bins'] = pd.qcut(data[variable], q=np.linspace(0, 1, num_bins + 1), duplicates='drop')

    # Calculate response rates within each bin
    r_rates = data.groupby('bins', observed=False)[response].mean().reset_index()

    return r_rates


# Perform binning
response_rates = binning_by_response_rate(data, 'variable', 'response', num_bins=5)

# Print the result
print(response_rates)
