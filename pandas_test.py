import pandas as pd
df = pd.read_csv("customers.txt", header=None)
df.columns = ["Name", "City", "Amount"]
print(df.isnull().sum())
print(df[df.duplicated()])
print(df["Amount"].max())
print(df[df["Amount"] > 200])
print(df[df["Amount"].isnull()])
print(df[df["City"] == "Chennai"])
print(len(df))