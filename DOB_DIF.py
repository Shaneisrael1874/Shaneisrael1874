yob=int(input("Enter your birth year:"))
mob=int(input("Enter your birth month in number:"))
dob=int(input("Enter only your birth date:"))
from datetime import date
today_date=date.today()
y=today_date.year-yob
m=today_date.month-mob
d=today_date.day-dob
print("Your age is",y,"years",m,"month",d,"days")