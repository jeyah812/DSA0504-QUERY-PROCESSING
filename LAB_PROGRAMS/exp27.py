import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/language_popularity.csv")

print(df)

plt.figure(figsize=(8,5))

plt.bar(df["Language"], df["Popularity"])

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")

plt.show()
