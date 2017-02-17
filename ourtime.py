import time
st = time.gmtime()
print(st) # UTC time

sst = time.localtime()
print(sst) # location time

import datetime
t = datetime.datetime(2015,8,18,10,30)
print(t)
t_first = datetime.datetime(2013,10,14)
t_next = datetime.datetime(2017,2,13,22,53)
delta0 = datetime.timedelta(weeks = 100)
delta1 = datetime.timedelta(days = 100)
delta2 = datetime.timedelta(hours = 100)
delta3 = datetime.timedelta(seconds = 100)
print(t_next - t)
print(t_next - t_first)
print(t + delta0)
print(t - delta1)
print(t + delta2)
print(t + delta3)
