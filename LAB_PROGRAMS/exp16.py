import pandas as pd

# Read the CSV file
df = pd.read_csv("data/school.csv")

print("Original DataFrame:\n")
print(df)

# Group by school code
grouped = df.groupby("school_code")

print("\nType of GroupBy Object:")
print(type(grouped))

print("\nGrouped DataFrames:\n")

for school, group in grouped:
    print("School Code:", school)
    print(group)
    print()
