import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    np.random.randn(10,4),
    columns=["B","C","D","E"]
)

df.insert(0,"A",range(1,11))

# Convert values to NaN
df.iloc[0,2] = np.nan
df.iloc[3,3] = np.nan
df.iloc[4,1] = np.nan
df.iloc[9,4] = np.nan

print(df)

# Highlight NaN
def highlight_nan(value):
    if pd.isna(value):
        return "background-color:red; color:white;"
    return ""

styled = df.style.map(highlight_nan)

styled.to_html("Q11_Output.html")

print("\nOpen Q11_Output.html in your browser.")
