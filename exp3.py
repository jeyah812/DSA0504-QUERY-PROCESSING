import pandas as pd

df = pd.read_csv("jobs.csv")

print("JOBS TABLE\n")
print(df)

sorted_df = df.sort_values(by="JOB_TITLE", ascending=False)

print("\nJobs in Descending Order of Job Title\n")
print(sorted_df)
