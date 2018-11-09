"""
Docstring
"""
from timeit import default_timer as timer
import pandas as pd
import psycopg2
conn = psycopg2.connect(
    "dbname=postgres user=niels password=niels host=localhost")
cur = conn.cursor()
start = timer()
cur.execute(r"truncate table t2")
print(f"timing truncate: {timer() - start}")
start = timer()
# create table if not exists t2 (a integer, b integer)
for i in range(1000):
    for j in range(1000):
        cur.execute(r"insert into t2 (a,b) values (%(a)s, %(b)s)",
                    {"a": (i+1)*(j+1), "b": j})
cur.close()
conn.commit()
print(f"timing insert: {timer() - start}")
conn.close()
conn = psycopg2.connect(
    "dbname=postgres user=niels password=niels host=localhost")
start = timer()
df = pd.read_sql("select a, b from t2", conn)
print(f"timing read_sql: {timer() - start}")
start = timer()
print(df.shape[0])
print(f"timing df.shape[0]: {timer() - start}")
conn.close()
