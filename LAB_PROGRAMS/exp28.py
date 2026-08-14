

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/language_popularity.csv")

plt.figure(figsize=(8,5))

plt.barh(df["Language"],
         df["Popularity"],
         color="green")

plt.xlabel("Popularity")
plt.ylabel("Languages")
plt.title("Popularity of Programming Languages")

plt.show()
