import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/group_height_weight.csv")

plt.figure(figsize=(8,6))

for group in df["Group"].unique():
    data = df[df["Group"] == group]

    plt.scatter(
        data["Weight"],
        data["Height"],
        label=group
    )

plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Group Wise Weight vs Height Scatter Plot")

plt.legend()

plt.show()
