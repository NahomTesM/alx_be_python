from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    global current_date 
    current_date = datetime.now()

    print(current_date)

def calculate_future_date():
    added_date = int(input("enter a number of days: "))
    future_date = current_date + timedelta(days=added_date)

    print(future_date.date())


display_current_datetime()
calculate_future_date()
