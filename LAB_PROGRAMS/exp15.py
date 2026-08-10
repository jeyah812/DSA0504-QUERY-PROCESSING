import pandas as pd

# Read the dataset
df = pd.read_csv("data/orders1.csv")

print("Original DataFrame:\n")
print(df)

# Keep rows with at least 2 NaN values
result = df[df.isnull().sum(axis=1) >= 2]

print("\nRows with at least 2 NaN values:\n")
print(result)
