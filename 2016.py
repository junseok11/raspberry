import sys
import datetime

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())

days = ['MON','TUE','WED','THU','FRI','SAT','SUN']
c = days[datetime.date(2016, a, b).weekday()]
print(c)