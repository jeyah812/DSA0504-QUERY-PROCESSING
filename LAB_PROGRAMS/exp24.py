import pandas as pd
import matplotlib.pyplot as plt

# Read the financial dataset
df = pd.read_csv("data/fdata.csv")

# Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"], format="%m-%d-%y")

# Display the dataset
print("Financial Data:")
print(df)

# Plot the financial data
plt.figure(figsize=(10, 5))

plt.plot(df["Date"], df["Open"], label="Open")
plt.plot(df["Date"], df["High"], label="High")
plt.plot(df["Date"], df["Low"], label="Low")
plt.plot(df["Date"], df["Close"], label="Close")

plt.xlabel("Date")
plt.ylabel("Price")
plt.title("Alphabet Inc. Stock Prices: October 3–7, 2016")
plt.legend()
plt.grid(True)

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
