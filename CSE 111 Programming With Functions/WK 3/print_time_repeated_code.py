from datetime import datetime

#Function to print current date and time
def print_time (task_name):
    print(task_name)
    print(datetime.now())
    print()

    #print timestamps to see how long sections of the 
    #code take to run

fist_name = "Emmanuel"
print_time("printed first name")


for x in range (0,10):
    print(x)
print_time("completed for loop")