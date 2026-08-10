import pandas as pd

# Read the dataset
df = pd.read_csv("data/world_alcohol.csv")

# Display the dataset
print("World Alcohol Consumption Dataset\n")
print(df)

# Display dimensions
print("\nDataset Shape (Rows, Columns):")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display column names as a list
print("\nColumn Names (List Format):")
print(df.columns.tolist())
