from datetime import datetime, timedelta

def display_current_datetime():
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_date



def calculate_future_date(days):
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days)
    formatted_future_date = future_date.strftime("%Y-%m-%d")
    return formatted_future_date


print((f"Current date and time: {display_current_datetime()}"))
days = int(input("Enter the number of days to add to the current date: "))
print((f"Future date: {calculate_future_date(days)}"))
