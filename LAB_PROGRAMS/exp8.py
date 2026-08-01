import pandas as pd

# Read CSV file
df = pd.read_csv("data/sales_data1.csv")

print("Original Data")
print(df)

# Pivot Table
pivot = pd.pivot_table(
    df,
    index="Item",
    values="Units",
    aggfunc="sum"
)

print("\nItem-wise Units Sold")
print(pivot)
