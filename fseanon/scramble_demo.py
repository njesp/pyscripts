"""
Demo
"""
import numpy as np
import pandas as pd
import fsescrambler as fs

k = fs.genkey()
print("key: " + k)
# Initier scrambler
e = fs.FseScramble(key=k.encode(), length=10)

df = pd.read_sas('c:/dropbox/dokumenter/niels/it/testdata1.sas7bdat', encoding='utf-8')
# Sæt pnr med foranstillede nuller
df['pnr'] = df['i'].astype(np.int64).astype(str).str.zfill(10)
df['pnr_scrambled'] = df['pnr'].apply(e.encrypt)
df['pnr_unscrambled'] = df['pnr_scrambled'].apply(e.decrypt)
# sorter resultat
df = df.sample(frac=1).reset_index(drop=True)
df.to_csv('c:/temp/out.csv', sep=';', index=False)

# gem oversættelsestabel, stort potentiale i database-ficering
# plink, hvordan får vi fat i et testdatasæt, hvordan sikrer vi det skalerer
# e det en fase 2
# hvordan får vi finansieret af KOR.