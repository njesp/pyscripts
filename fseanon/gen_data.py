import pandas as pd
from Cryptodome.Random import random

df = pd.DataFrame()
df["pnr"] = [f"{random.randint(1, 1000000000):010d}" for i in range(100)]
df["value1"] = "xzz" + df["pnr"] + "zzx"
df["value2"] = "3$" + df["pnr"] + ":-xm"
df.to_csv("c:/temp/xx.csv", sep=";", header=False, index=False)
for chunk in pd.read_csv(
    "c:/temp/xx.csv", header=None, dtype=str, sep=";", chunksize=49
):
    for r in chunk.iterrows():
        print(r)
