from datetime import datetime, timedelta

print("\n")
#Ask user for the birthday in the format DD/MMM/YYY
birthday = input("Enter your birth day (dd/mm/yyyy)? ")

# Use strptime to determine the format
birthday_date = datetime.strptime(birthday, '%d/%m/%Y')


print("Birthday: " + str(birthday_date),"\n")

time_frame = int(input("Enter how many days back to retrieve: "))
days_back = timedelta(days=time_frame)

birthday_past = birthday_date - days_back

print(f"{time_frame} days ago that was " +str(birthday_past))

print("\n")
