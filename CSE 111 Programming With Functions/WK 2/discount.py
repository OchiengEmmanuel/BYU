
from datetime import datetime

discount = 0
sales_tax = .06

current_date_and_time = datetime.now()

day_of_week = current_date_and_time.weekday()
# Get the subtotal of items from the user.

#print (f"{day_of_week}")

subtotal = float(input("Please enter the subtotal: "))

if subtotal >= 50 and day_of_week == 2 or day_of_week == 3:
     discount = 0.10 * subtotal 
     sales_tax = 0.06 * subtotal
     total_amount_due = subtotal - discount + sales_tax
     print (f"Enjoy amazing discount discount of {round((subtotal - total_amount_due),2)}!! Welcome again!!")
elif subtotal <50:
     print (f"Welcome between Tuesday and Wednesday to enjoy amazing discount!")