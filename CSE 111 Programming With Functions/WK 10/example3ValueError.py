# Example 3
#ValueError
"""
    The computer raises a ValueError when the code that calls 
    a function passes an argument with the correct
    data type but with an invalid value. A common event 
    that causes the computer to raise a ValueError is when 
    the int function or float function tries to convert a string 
    to a number but the string contains characters that 
    are not digits
"""

def main():
    try:
        number = float(input("Please enter a number: "))
        print(number)

    except ValueError as val_err:
        print(val_err)

if __name__ == "__main__":
    main()