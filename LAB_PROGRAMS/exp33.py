import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/scatter_empty.csv")

plt.figure(figsize=(7,5))

plt.scatter(
    df["X"],
    df["Y"],
    facecolors='none',
    edgecolors='green'
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Scatter Plot with Empty Circles")

plt.show()
