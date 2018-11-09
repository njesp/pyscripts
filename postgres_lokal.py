"""
Docstring
"""
import psycopg2
conn = psycopg2.connect("dbname=postgres user=niels password=niels host=localhost")
cur = conn.cursor()
# create table if not exists t2 (a integer, b integer)
for i in range(1000):
    for j in range(1000):
        cur.execute(r"insert into t2 (a,b) values (%(a)s, %(b)s)",
                    {"a": (i+1)*(j+1), "b": j})
cur.close()
conn.commit()
conn.close()
#
conn = psycopg2.connect("dbname=postgres user=niels password=niels host=localhost")
cur = conn.cursor()
cur.arraysize = 100
cur.execute('select a, b from t2')
while True:
    rows = cur.fetchmany()
    for i in rows:
        print(str(i[0]) + ' ' + str(i[1]))
    if len(rows) < cur.arraysize:
        break
conn.commit()
cur.close()
conn.close()
