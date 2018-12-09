import psycopg2
import os
with open(os.path.expanduser("~/pwds/postgrespwd.txt")) as f:
    pwd = f.readline()
conn = psycopg2.connect(
    f"dbname=testdb user=niels password={pwd} host=192.168.0.11")
#cur = conn.cursor()
#cur.execute("create table if not exists t2 (a integer, b integer)")
# for i in range(1000):
#    for j in range(1000):
#        cur.execute(r"insert into t2 (a,b) values (%(a)s, %(b)s)",
#                    {"a": (i+1)*(j+1), "b": j})
# cur.close()
# conn.commit()
# conn.close()


def iterdata(cursor, arraysize=1000):
    while True:
        res = cursor.fetchmany(arraysize)
        if not res:
            break
        for r in res:
            yield r


cur = conn.cursor()
cur.execute('select txt from public.aisdata order by sys_id')

for d in iterdata(cur):
    print(d)

cur.close()
conn.commit()
conn.close()
