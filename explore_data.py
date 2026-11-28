import pandas as pd

df = pd.read_csv("./data/train.csv", sep="\t", index_col=0)

print(df.head())
print(df.shape)
print(df.columns)
print(df.dtypes)

print(df["label"].value_counts(normalize=True) * 100)

print(df.isna())

df = df.dropna(subset=["comment" , "label"])

print(df.isna())

print(df.duplicated().sum())

print(df.duplicated(subset=["comment"]).sum())

