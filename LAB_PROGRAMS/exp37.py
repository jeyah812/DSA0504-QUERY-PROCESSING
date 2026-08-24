import pandas as pd

# Read CSV file
df = pd.read_csv("data/dataframe_dict.csv")

# Display DataFrame
print("DataFrame:\n")
print(df)

# Display Shape
print("\nShape of DataFrame:")
print(df.shape)
