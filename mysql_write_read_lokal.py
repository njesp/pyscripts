"""
Docstring
"""
from timeit import default_timer as timer
import mysql.connector
import pandas as pd
conn = mysql.connector.connect(
    user='niels', password='niels', host='localhost')
cur = conn.cursor()
# create table if not exists t2 (a integer, b integer)
start = timer()
cur.execute(r"truncate table test.t2")
print(f"timing truncate: {timer() - start}")
start = timer()
for i in range(1000):
    for j in range(1000):
        cur.execute(r"insert into test.t2 (a,b) values (%(a)s, %(b)s)",
                    {"a": (i+1)*(j+1), "b": j})
cur.close()
conn.commit()
print(f"timing insert: {timer() - start}")
conn.close()
#
conn = mysql.connector.connect(
    user='niels', password='niels', host='localhost')
start = timer()
df = pd.read_sql("select a, b from test.t2", conn)
print(f"timing read_sql: {timer() - start}")
start = timer()
print(df.shape[0])
print(f"timing df.shape[0]: {timer() - start}")
conn.close()
