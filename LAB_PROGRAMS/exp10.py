import pandas as pd
import numpy as np

# Create random dataframe
np.random.seed(10)

df = pd.DataFrame(
    np.random.randn(10,4),
    columns=["B","C","D","E"]
)

df.insert(0,"A",range(1,11))

print(df)

# Function for coloring
def color_numbers(value):
    if isinstance(value,(int,float)):
        if value < 0:
            return "color:red"
        else:
            return "color:black"
    return ""

styled = df.style.map(color_numbers)

# Save as HTML
styled.to_html("Q10_Output.html")

print("\nOpen Q10_Output.html in your browser.")
