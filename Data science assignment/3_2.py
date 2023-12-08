import pandas as pd

# Sample data
data = {'nationality': ['Indian', 'foreigner', 'Indian', 'Indian', 'foreigner'],
        'Hindu': ['Yes', 'No', 'No', 'Yes', 'Yes']}

df = pd.DataFrame(data)

# Create a contingency table using the crosstab function
contingency_table = pd.crosstab(df['nationality'], df['Hindu'])

# Display the contingency table
print(contingency_table)
