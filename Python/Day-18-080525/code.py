from datetime import datetime,date,time,timedelta
import pytz
#current date time

now = datetime.now()
print(now)
today = date.today()
print(today)

# specific time

dt = datetime(2023,12,31,23,59,59)
print(type(dt))
d = date(2023,12,31)
print(d)
print(time(23,59,59))

#with timezone
utc_now = datetime.now(pytz.UTC)
ny_tz = pytz.timezone('America/Chicago')
ny_time = datetime.now(ny_tz)
print(ny_time)

#formatting and parsing

now = datetime.now()
print(now)
timestamp = now.strftime('%d-%Y-%m %H:%M:%S')
print(timestamp)
print(now.strftime('%d-%Y-%m'))

#Date Arithmetic
# add / subtract time
today = date.today()
print(today)
tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1,weeks=7)
print(yesterday)

# date difference

delta = date(2025,5,8) - date(2023,12,31)  
print(delta.days)

print(abs(-123123))