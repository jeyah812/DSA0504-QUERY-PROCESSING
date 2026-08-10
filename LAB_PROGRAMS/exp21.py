import pandas as pd

# Read the CSV file
df = pd.read_csv("data/school1.csv")

print("Original DataFrame:\n")
print(df)

# Swap the cases of the name column
df["name"] = df["name"].str.swapcase()

print("\nDataFrame after swapping cases of name column:\n")
print(df)
