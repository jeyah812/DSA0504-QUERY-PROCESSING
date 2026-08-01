import pandas as pd

df = pd.read_csv("data/departments.csv")

print("DEPARTMENTS TABLE\n")
print(df)

result = df["DEPARTMENT_ID"].drop_duplicates()

print("\nDistinct Department IDs\n")

for dept in result:
    print(dept)
