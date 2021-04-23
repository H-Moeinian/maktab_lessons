# import time
# print(time.time())
# from datetime import date, time, datetime, timedelta
# import pytz
#
#
# # set time zone
# print(pytz.all_timezones_set)  # shows all available time zones
# tz = pytz.timezone('Asia/Tehran')
# print(datetime.now(tz = tz))
#
# d1=date(2021,3,21)
# t1=time(22,10,10)
# dt1=datetime(year=2021,month=2,day=10,hour=12,minute=5,second=12)
# print(d1)
# print(t1)
# print()
# print(date.today())
# print(datetime.now())
# print(datetime.combine(d1,t1))

#convert a string to a datetime object
# str_format = '14:22:36 2021_02_02'
# frmt = '%H:%M:%S %Y_%m_%d'
# dt2 = datetime.strptime(str_format,frmt)
# print(dt2)

#convert a datetime object to a string with a specific format
# print(dt1.strftime(frmt))

#timedelta
#int(now - timedelta(days=5, hours=-4))

#persian calendar: jdatetime, https://pypi.org/project/jdatetime/

# json
#import json
# result = {str(x):x**2 for x in range(20)}
# with open('1.json','w') as write_file:
#     json.dump(result,write_file,ensure_ascii=False)
# json_sample = json.dumps(result,ensure_ascii=False)  #serialization
# print(type(json_sample))

# with open('1.json','r') as read_file:   #deserialization
#     data = json.load(read_file)
#     print(type(data))
#     for key, val in data.items():
#         print(key, val)
# json_sample = json.loads('{"1":1,"2":2}')
# print(json_sample)

import jdatetime
import json
#creating a calendar
first_day = jdatetime.date(1400, 1, 1)
convert_first_day = first_day.togregorian()
print(first_day)
print(convert_first_day)
next_year = jdatetime.date(first_day.year+1,first_day.month,first_day.day)
print(next_year)
calendar = []
for i in range(366):
    day = first_day + jdatetime.timedelta(days=i)
    gregorian_day = day.togregorian()
    date={'jalali':str(day), 'gregorian':str(gregorian_day)}
    calendar.append(date)
with open('calendar.json','w') as json_file:
    json.dump(calendar,json_file)
