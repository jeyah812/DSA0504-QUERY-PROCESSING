import pandas as pd

# Read the CSV file
df = pd.read_csv("data/exam_data1.csv")

# Display the first three rows
print("First three rows of the DataFrame:")
print(df.head(3))
