from timeit import default_timer as timer
import pyodbc
start = timer()
with open(r"c:\pwds\sqlserverpwd.txt") as f:
    passwd = f.readline()
conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='njndb.database.windows.net', database='Test', uid = 'njesp', pwd = passwd)
cur = conn.cursor()
cur.arraysize = 100000
cur.fast_executemany = False
binds = []
for x in range(10):
    for y in range(1000):
        binds.append([x, y])
cur.executemany("insert into [test].[dbo].[t2] (a,b) values (?, ?)", binds)
cur.close()
conn.commit()
conn.close()
end = timer()
print('timing: ', (end - start))
#
