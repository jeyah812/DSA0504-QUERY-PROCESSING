import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/alphabet_stock_data.csv")

print("ALPHABET STOCK DATA\n")
print(df)

df["Date"] = pd.to_datetime(df["Date"])

plt.figure(figsize=(8,5))

plt.scatter(df["Date"], df["Close"])

plt.title("Alphabet Inc. Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.grid(True)

plt.show()
