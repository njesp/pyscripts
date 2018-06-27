import mysql.connector
with open(r"c:\temp\mysqlpwd.txt") as f:
    pwd = f.readline()
conn = mysql.connector.connect(user='njnmysqladm@njnmysqlsrver', password=pwd, host='njnmysqlsrver.mysql.database.azure.com')
#create table if not exists t2 (a integer, b integer)                               
cur = conn.cursor()
cur.execute("create table if not exists test.t2 (a integer, b integer)")
for i in range(10):
    for j in range(100):
        cur.execute(r"insert into test.t2 (a,b) values (%(a)s, %(b)s)",
                    {"a": (i+1)*(j+1), "b": j})
cur.close()
conn.commit()
conn.close()
#
conn = mysql.connector.connect(user='njnmysqladm@njnmysqlsrver', password=pwd, host='njnmysqlsrver.mysql.database.azure.com')
cur = conn.cursor()
cur.execute('select a, b from test.t2')
while True:
    rows = cur.fetchmany(size=30)
    for i in rows:
        print(str(i[0]) + ' ' + str(i[1]))
    if len(rows) < cur.arraysize:
        break
conn.commit()
cur.close()
conn.close()
