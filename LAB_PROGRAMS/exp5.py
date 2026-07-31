import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("alphabet_stock_data.csv")

print("ALPHABET STOCK DATA\n")
print(df)

plt.figure(figsize=(8,5))

plt.bar(df["Date"], df["Close"])

plt.title("Alphabet Inc. Stock Prices")
plt.xlabel("Date")
plt.ylabel("Closing Price")

plt.show()
