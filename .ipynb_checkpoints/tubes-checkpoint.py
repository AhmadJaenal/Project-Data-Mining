import pandas as pd

df = pd.read_csv("Sleep_health_and_lifestyle_dataset.csv")
pd.set_option("display.max_rows", df.shape[0] + 1)

print(df)
