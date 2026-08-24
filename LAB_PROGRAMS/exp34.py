import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/scatter_bubbles.csv")

plt.figure(figsize=(8,6))

plt.scatter(
    df["X"],
    df["Y"],
    s=df["Size"],
    alpha=0.7
)

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bubble Scatter Plot")

plt.show()
