# Example 2
# TypeError
"""
     The code in example 2 attempts to pass a string to the 
     round function. This causes the computer to raise a 
     TypeError because the round function cannot round a string to 
     an integer. It can round only a number to an integer
"""
def main():
    try:
        text = input("Please enter a number: ")
        integer = round(text)
        print(integer)

    except TypeError as type_err:
        print(type_err)

if __name__ == "__main__":
    main()