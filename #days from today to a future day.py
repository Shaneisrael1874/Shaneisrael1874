import datetime
from datetime import date
today_date=date.today()
future_datestr=input("Enter a date in the future:")
future_date=datetime.datetime.strptime(future_datestr,'%d-%m-%Y').date()
day_difference=future_date-today_date
print(day_difference)