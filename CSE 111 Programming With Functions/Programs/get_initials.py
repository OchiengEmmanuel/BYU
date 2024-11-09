#Function to return the first initial of the name from the user
def get_inial(name):
    initial = name[0:1].upper()
    return initial

#Ask for someone's names then return the initials
first_name = input("Enter your first name ")
#first_name_initial = first_name[0:1].lower()
first_name_initial = get_inial(first_name)


middle_name = input("Enter your last name ")
#middle_name_initial = middle_name[0:1]
middle_name_initial = get_inial(middle_name)


last_name = input("Enter your last name " )
#last_name_initial = last_name[0:1]
last_name_initial = get_inial(last_name)


print(first_name_initial,middle_name_initial,last_name_initial)