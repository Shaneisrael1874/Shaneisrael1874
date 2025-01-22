import calendar
import datetime 
month=int(input("Enter month:"))
year=int(input("Enter the year:"))
first_day=datetime.datetime(year,month,1)
last_day=datetime.datetime(year,month,calendar.monthrange(year,month)[1])
print("The first day of the month is:",first_day.strftime('%A'))
print("The last day of the month is:",last_day.strftime('%A'))

