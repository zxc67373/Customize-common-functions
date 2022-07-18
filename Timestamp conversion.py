import time
from datetime import date
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(1656297223)))

d  = date(2022,7,10)
print(time.mktime(time.strptime(str(d), "%Y-%m-%d ")))
