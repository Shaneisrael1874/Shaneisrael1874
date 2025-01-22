#to calculate difference between two random dates
import datetime 
first_datestr=input("Enter first date:")
first_date=datetime.datetime.strptime(first_datestr,'%d-%m-%Y')
second_datestr=input("Enter second date:")
second_date=datetime.datetime.strptime(second_datestr,'%d-%m-%Y')
day_difference=first_date-second_date
print(day_difference)