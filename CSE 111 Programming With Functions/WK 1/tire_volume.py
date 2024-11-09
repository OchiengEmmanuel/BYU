        #Assignment
"""
Write a Python program named tire_volume.py that reads from the keyboard the 
three numbers for a tire and computes and outputs the volume of space inside that tire.

"""
#Import the math module to enable me use the math.pi
import math

#Get tire information from the user; width, aspect ratio, and the diameter.

w =float(input("Enter the width of the tire in mm (ex 205): "))
a =float(input("Enter the aspect ratio of the tire (ex 60): "))
d =float(input("Enter the diameter of the wheel in inches (ex 15): "))


# Compute the volume of the tire based on user inputs.

v = (math.pi * w**2 * a*(w * a + 2540*d))/10000000000


#Print the value to the user to 2 decimal places using round function
        #Option 1
# print(f"The approximate volume is {round(v,2)} liters")

        #Option 2
#Code to round up the volume to 2 decimal places before print
v = round(v,2)

print(f"The approximate volume is {v} liters")

user_decision = input("Do you want to buy? Enter yes/no: ")

if user_decision.lower() in ['yes', 'y']:
    telephone = input("Enter your phone number ")
    print(f"Our sales team will be in touch via your telephoe number {telephone}")
    print("Thank you")
elif user_decision.lower() in ['no', 'n']:
    print("Feel free to contact us again in the future")
else:
    print("Invalid input. Please enter either 'yes' or 'no'.")

# Import the datetime class from the datetime
# module so that it can be used in this program.
from datetime import datetime

# Call the now() method to get the current
# date and time as a datetime object from
# the computer's operating system.
current_date_and_time = datetime.now()

with open("volume.txt", "at") as volume_file:
        print(f"{current_date_and_time:%Y-%m-%d}, {int(w)}, {int(a)}, {int(d)}, {v}" , file=volume_file)
        print(f"{current_date_and_time:%Y-%m-%d}, {int(w)}, {int(a)}, {int(d)}, {v}")
#        contents = volume_file.readlines()
#        print(contents)

