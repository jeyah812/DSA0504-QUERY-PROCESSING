import pandas as pd

# Read the dataset
df = pd.read_csv("data/orders.csv")

print("Original DataFrame:")
print(df)

# Replace missing values
df.fillna({
    'ord_no': 0,
    'ord_date': 'Unknown',
    'customer_id': 0,
    'salesman_id': 0
}, inplace=True)

print("\nDataFrame after replacing missing values:")
print(df)
