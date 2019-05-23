"""
Parse IIS Logs
"""
import os
import re
import pandas as pd

IIS_REGEX = (r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\d+\.\d+\.\d+\.\d+) (\w+) (.+) (\d+)'
             r' - (\d+\.\d+\.\d+\.\d+) ([^ ]+) ([^ ]+) (\d+) (\d+) (\d+) (\d+).*')
PATH1 = "/home/niels/valglogs/srvelection1"
PATH2 = "/home/niels/valglogs/srvelection2"
#
df = pd.DataFrame()
p = re.compile(IIS_REGEX)
l = []
for path in (PATH1, PATH2):
    for file in os.listdir(path):
        with open((os.path.join(path, file)), 'r') as f:
            for line in f:
                m = p.match(line)
                if m:
                    l.append({"date": m.group(1), "time" : m.group(2), "s-ip": m.group(3), "cs-method": m.group(4),
                              "squery": m.group(5), "s-port": m.group(6),
                              "c-ip": m.group(7), "user-agent":  m.group(8),
                              "referer":  m.group(9), "sc-status": m.group(10), "sc-substatus": m.group(11),
                              "sc-win32-status": m.group(12), "time-taken": m.group(13)})
                elif line[0] != "#":
                    #print(line)
                    pass
df = pd.DataFrame(l)
df2 = df.query("squery == '/favicon.ico -'")
print(df2["squery"])
