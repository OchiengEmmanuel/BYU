#Function can accept multiple parameters

def get_inial(name, force_uppercase):
    if force_uppercase:
        initial = name[0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input("Enter your first name ")
first_name_initial = get_inial(first_name, True)

print("Your initial is: " + first_name_initial)