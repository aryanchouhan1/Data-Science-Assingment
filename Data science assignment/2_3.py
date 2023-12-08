import pandas as pd

# Sample DataFrame with a categorical field
data = {'animal': ['cat', 'cat', 'dog', 'monkey', 'cat', 'dog']}

df = pd.DataFrame(data)
df_original = df.copy()

# Mapping categorical values to numerical categories
# Creating a mapping dictionary
mapping = {'cat': 1, 'dog': 2, 'monkey': 3}

# Replacing categorical values with numerical categories
df['animal'] = df['animal'].map(mapping)

print("Original DataFrame:")
print(df_original)

print("\nReexpressed DataFrame:")
print(df)