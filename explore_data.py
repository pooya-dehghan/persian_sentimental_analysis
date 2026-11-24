import pandas as pd

df = pd.read_csv("./data/train.csv", sep="\t", index_col=0)

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)