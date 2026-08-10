import pandas as pd

# Read the CSV file
df = pd.read_csv("data/orders.csv")

# Display the DataFrame
print("Original DataFrame:")
print(df)

# Detect missing values
print("\nMissing Values (True/False):")
print(df.isnull())
