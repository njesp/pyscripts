# Installer Microsoft ODBC Driver 17 for SQL Server
# Installer pyodbc (Microsoft preferred SQL Server Driver for Python): pip install pyodbc
# Alternativt pip install c:\temp\pyodbc-4.0.23-cp36-cp36m-win_amd64.whl
import pyodbc
with open(r"c:\temp\sqlserverpwd.txt") as f:
    passwd = f.readline()
conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='njndb.database.windows.net', database='Test', uid = 'njesp', pwd = passwd)
cur = conn.cursor()
#create dbo.t2 (a integer, b integer)
for i in range(10):
    for j in range(100):
        cur.execute(r"insert into dbo.t2 (a,b) values (?, ?)", (i+1)*(j+1), j)
cur.close()
conn.commit()
conn.close()
#
conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='njndb.database.windows.net', database='Test', uid = 'njesp', pwd = passwd)
cur = conn.cursor()
cur.arraysize = 100
cur.execute('select a, b from dbo.t2')
while True:
    rows = cur.fetchmany()
    for i in rows:
        print(str(i[0]) + ' ' + str(i[1]))
    if len(rows) < cur.arraysize:
        break
conn.commit()
cur.close()
conn.close()
