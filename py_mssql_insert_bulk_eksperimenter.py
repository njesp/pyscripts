from timeit import default_timer as timer
import pyodbc
start = timer()
with open(r"c:\pwds\sqlserverpwd.txt") as f:
    passwd = f.readline()
conn = pyodbc.connect(driver='{ODBC Driver 17 for SQL Server}', server='njndb.database.windows.net', database='Test', uid = 'njesp', pwd = passwd)
cur = conn.cursor()
cur.arraysize = 100000
# True performer ca 70 gange bedre (målt mod Azure Database. Samme størrelsesorden mod on-premise db)
cur.fast_executemany = True
binds = []
for x in range(100):
    for y in range(1000):
        binds.append([x, y])
cur.executemany("insert into [test].[dbo].[t2] (a,b) values (?, ?)", binds)
cur.close()
conn.commit()
conn.close()
end = timer()
print('timing: ', (end - start))
#
