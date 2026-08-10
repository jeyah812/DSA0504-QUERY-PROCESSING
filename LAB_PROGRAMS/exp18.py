import pandas as pd

# Read the dataset
df = pd.read_csv("data/school_data.csv")

# Display the original DataFrame
print("Original DataFrame\n")
print(df)

# Group the DataFrame by School Code and Class
grouped = df.groupby(["school", "class"])

# Display each group
print("\n\nGrouped DataFrames\n")

for group_name, group_data in grouped:
    print("===================================")
    print("Group:", group_name)
    print(group_data)
    print()
