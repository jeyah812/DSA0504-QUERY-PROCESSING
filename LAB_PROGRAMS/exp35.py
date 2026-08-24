import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/student_marks.csv")

plt.figure(figsize=(8,6))

plt.scatter(
    df["Marks_Range"],
    df["Math_Marks"],
    color='red',
    label='Math Marks'
)

plt.scatter(
    df["Marks_Range"],
    df["Science_Marks"],
    color='green',
    label='Science Marks'
)

plt.xlabel("Marks Range")
plt.ylabel("Marks Scored")

plt.title("Comparison of Mathematics and Science Marks")

plt.legend()

plt.grid(True)

plt.show()
