import pandas as pd
import numpy as np

np.random.seed(10)

df = pd.DataFrame(
    np.random.randn(10,4),
    columns=["B","C","D","E"]
)

df.insert(0,"A",range(1,11))

print(df)

styled = df.style.set_properties(**{
    "background-color": "black",
    "color": "yellow"
})

styled.to_html("Q12_Output.html")

print("\nOpen Q12_Output.html in your browser.")
