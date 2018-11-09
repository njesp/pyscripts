"""
Performance ved insert er 80 gange bedre med denne
"""
import json
from timeit import default_timer as timer
import pandas as pd
import psycopg2
conn = psycopg2.connect(
    "dbname=postgres user=niels password=niels host=localhost")
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
query = """
insert into t2 (a,b)
select a, b from json_populate_recordset(null::t2, %s);
"""
cur.execute(query, (json.dumps(d),))
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
