import datetime

def date_converter(date):
    date_object = datetime.datetime.strptime(date, '%Y-%m-%d')
    return date_object.strftime('%A')


print(date_converter('2024-03-15'))  
