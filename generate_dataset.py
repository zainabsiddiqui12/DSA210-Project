import pandas as pd

df = pd.read_csv("data/youtube_consistency_dataset.csv")
print(df.head())
print(df.describe(include="all"))
