import pandas as pd

# Read the dataset
df = pd.read_csv("data/employees.csv")

# Display the DataFrame
print("Employee Dataset\n")
print(df)

# Enter the substring to search
substring = input("Enter the substring to search: ")

# Find rows containing the substring
matching_index = df[df["Employee_Name"].str.contains(substring, case=False, na=False)].index

# Display matching rows
print("\nMatching Records:\n")
print(df.loc[matching_index])

# Display index values
print("\nIndex of Matching Rows:")
print(list(matching_index))
