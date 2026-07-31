import pandas as pd

df = pd.read_csv("job_history.csv")

print("JOB HISTORY TABLE")
print(df)

count = df.groupby("EMPLOYEE_ID").size()

result = count[count >= 2]

print("\nEmployees who have done two or more jobs:\n")

for emp in result.index:
    print(emp)
