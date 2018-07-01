import psycopg2
with open(r"c:\pwds\postgrespwd.txt") as f:
    pwd = f.readline()
conn = psycopg2.connect("dbname=postgres user=njn@njnpostgres password={} host=njnpostgres.postgres.database.azure.com".format(pwd))
cur = conn.cursor()
#create table if not exists t2 (a integer, b integer)
for i in range(10):
    for j in range(100):
        cur.execute(r"insert into t2 (a,b) values (%(a)s, %(b)s)",
                    {"a": (i+1)*(j+1), "b": j})
cur.close()
conn.commit()
conn.close()
#
conn = psycopg2.connect("dbname=postgres user=njn@njnpostgres password={} host=njnpostgres.postgres.database.azure.com".format(pwd))
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