from datetime import datetime
from datetime import timedelta

def display_current_datetime():
    global current_date 
    current_date = datetime.now()

    print(f"Current date and time: {current_date.strftime("%Y-%m-%d %H:%M:%S")}")

def calculate_future_date():
    added_date = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=added_date)

    print(f"Future date: {future_date.strftime("%Y-%m-%d %H:%M:%S")}")


display_current_datetime()
calculate_future_date()
