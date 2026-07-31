import pandas as pd

df = pd.read_csv("sales_data.csv")

print("SALES DATA\n")
print(df)

pivot = pd.pivot_table(
    df,
    index="Item",
    values="Sale_amt",
    aggfunc=["max", "min"]
)

print("\nMaximum and Minimum Sale Value of Items\n")
print(pivot)
