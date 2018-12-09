"""
Docstring
"""
from timeit import default_timer as timer
import pandas as pd
import psycopg2
import os
import psycopg2.extras
with open(os.path.expanduser("~/pwds/postgrespwd.txt")) as f:
    pwd = f.readline()
conn = psycopg2.connect(
    f"dbname=testdb user=niels password={pwd} host=192.168.0.11")
cur = conn.cursor()

start = timer()
cur.execute(r"truncate table t2")
print(f"timing truncate: {timer() - start}")
# create table if not exists t2 (a integer, b integer)
df = pd.DataFrame()
d = []
for i in range(1000):
    for j in range(1000):
        #        df = df.append({'a': int(i), 'b': int(j)}, ignore_index=True)
        d.append({'a': i, 'b': j})
print('dataframe klar')
start = timer()
# Executemany er ikke god med postgres

psycopg2.extras.execute_batch(
    cur, r"insert into t2 (a,b) values (%(a)s, %(b)s)", d, page_size=1000)
cur.close()
conn.commit()
print(f"timing insert: {timer() - start}")
conn.close()
