import datetime

dates = datetime.datetime.today()
print dates
print dates.day
a = dates.ctime()
print a
c = str(dates.year)+'/'+str(dates.month)+'/'+str(dates.day)
print c
