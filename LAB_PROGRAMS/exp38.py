import pandas as pd

# Read CSV file
df = pd.read_csv("data/exam_data.csv")

# Custom index labels
labels = ['a','b','c','d','e',
          'f','g','h','i','j']

# Assign labels
df.index = labels

# Display DataFrame
print(df)
