from datetime import   date,time,datetime
from time import strftime

now = datetime.now()

print(now,strftime("%Y-%m-%d %H:%M:%S"))
print(now.strftime("%d/%m/%Y %I:%M:%S"))
print(now.strftime("%d %b %y %I:%M:%S"))
print(now.strftime("%d %B %Y %I:%M:%S"))
print(now.strftime("%A %d %B %I:%M:%S"))
