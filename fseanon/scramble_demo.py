"""
Demo Scramble
"""
import pandas as pd
import fsescrambler as fs

e = fs.FseScramble(key=b"02sxdssxxxxxxxxfkkallxcffssdfg", length=10)

for chunk in pd.read_csv(
    "c:/temp/xx.csv", header=None, dtype=str, sep=";", chunksize=49
):
    for r in chunk.iterrows():
        x = r[1]
        print(e.encrypt(x[0]) + " ; " + e.decrypt(e.encrypt(x[0])) + " ; " + x[0])


# print(e.encrypt("abcde"))
# print(e.decrypt("acbacc"))
