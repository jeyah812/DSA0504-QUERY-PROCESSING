import pandas as pd

# Read the CSV file
df = pd.read_csv("data/exam_data1.csv")

# Select name and score columns
selected_columns = df[["name", "score"]]

# Display selected columns
print("Selected Columns:")
print(selected_columns)
