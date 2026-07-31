import pandas as pd

df = pd.read_csv("sales_data1.csv")

pivot = pd.pivot_table(
    df,
    index=["Region","Manager","SalesMan"],
    values="Sale_amt",
    aggfunc="sum"
)

print(pivot)
