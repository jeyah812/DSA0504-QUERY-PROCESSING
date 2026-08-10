import pandas as pd

# Read CSV file
df = pd.read_csv("data/school.csv")

print("Original DataFrame:\n")
print(df)

# Group by school_code and calculate statistics
result = df.groupby("school_code")["age"].agg(["mean", "min", "max"])

print("\nMean, Minimum and Maximum Age by School Code:\n")
print(result)
