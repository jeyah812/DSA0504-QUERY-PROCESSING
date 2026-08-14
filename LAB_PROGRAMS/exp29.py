import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/language_popularity.csv")

colors = ['red',
          'black',
          'green',
          'blue',
          'yellow',
          'cyan']

plt.figure(figsize=(8,5))

plt.bar(df["Language"],
        df["Popularity"],
        color=colors)

plt.xlabel("Languages")
plt.ylabel("Popularity")
plt.title("Popularity of Programming Languages")

plt.show()
