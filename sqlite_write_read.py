import sqlite3
conn = sqlite3.connect("c:/temp/sqlite_test.db")
conn.isolation_level = "DEFERRED"
cur = conn.cursor()
cur.execute("create table if not exists t2 (a integer, b integer)")
for i in range(1000):
    for j in range(1000):
        cur.execute("insert into t2 (a,b) values (:a, :b)",
                    {"a": (i+1)*(j+1), "b": j})
cur.close()
conn.commit()
conn.close()
#
conn = sqlite3.connect("c:/temp/sqlite_test.db")
conn.isolation_level = "DEFERRED"
cur = conn.cursor()
cur.arraysize = 1000
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
