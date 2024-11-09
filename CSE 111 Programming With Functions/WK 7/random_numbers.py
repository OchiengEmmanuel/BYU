from random_numbers import append_random_numbers
# from random_numbers import append_random_words
import pytest


def main():

    numbers = [16.2, 75.1, 52.3]
    
    print(numbers)

    # Call append_random_numbers function with one argument
    numbers = append_random_numbers(numbers_list= 13)

    print("Numbers after adding a random number:", numbers)

def append_random_numbers(numbers_list, quantity = 1):

    numbers_list = [12, 27.8 , 13, 104.2, 69.2, 0, 12]


# Call main to start this program.
if __name__ == "__main__":
    main()