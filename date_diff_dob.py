#to find the no of days from one's DOB
import datetime 
from datetime import date
DOB=input("Enter your DOB:")
today_date=date.today()
dob=datetime.datetime.strptime(DOB,'%d-%m-%Y').date()
date_difference=today_date-dob
print(date_difference)                              