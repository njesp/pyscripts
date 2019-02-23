"""
Docstring
"""
import os
from timeit import default_timer as timer
import psycopg2
import psycopg2.extras
conn = psycopg2.connect(f"dbname=testdb user=postgres host=secretubox.westeurope.cloudapp.azure.com")
cur = conn.cursor()
cur.execute("create table if not exists t2 (a integer, b integer)")
cur.execute("truncate table t2")
d = []
for i in range(1000):
    for j in range(1000):
        d.append({'a': i, 'b': j})
start = timer()
psycopg2.extras.execute_batch(cur, r"insert into t2 (a,b) values (%(a)s, %(b)s)", d, page_size=1000)
cur.close()
conn.commit()
print(f"timing insert: {timer() - start}")
conn.close()
