import datetime
from datetime import date
today_date=date.today()
print(today_date)
DOB=input("Enter your DOB:")
dob=datetime.datetime.strptime(DOB,'%d,%m,%Y')
print(dob)
day_difference=today_date-dob
print(day_difference)