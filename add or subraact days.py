import datetime
from datetime import timedelta
date_ = input("Enter a date (dd-mm-yyyy): ")
date1 = datetime.datetime.strptime(date_, '%d-%m-%Y')
a = int(input("Enter the number of days to be added: "))
new_date_add = date1 + timedelta(days=a)
print("After adding:", new_date_add)
b = int(input("Enter the number of days to be subtracted: "))
new_date_subtract = date1 - timedelta(days=b)
print("After subtracting:", new_date_subtract)