########################### BRIGHAM YOUNG UNIVERSITY- IDAHO
########################### EMMANUEL ODUOR OCHIENG 
########################### 7TH APRIL, 2024 
########################### PURPOSE OF THE ASSINGMENT: Help children master multiplication table problem by randomly
##########################                             chosing numbers between 1 and 20.
########################### SOURCES USED: 
"""
https://realpython.com/numpy-random-number-generator/
Links to an external site.

https://www.shecodes.io/athena/39028-how-to-make-a-simple-guessing-game-in-python
Links to an external site.

https://www.studysmarter.co.uk/explanations/computer-science/computer-programming/python-infinite-loop/
Links to an external site.

https://www.youtube.com/watch?v=zuL3_IZtM24
Links to an external site.

https://www.geeksforgeeks.org/python-range-function/
Links to an external site.

https://www.nobledesktop.com/learn/coding/multiplication-tables-in-python
Links to an external site.

https://www.educative.io/answers/how-to-create-a-multiplication-table-for-any-number-in-python
Links to an external site.
    """

import random

def eo_display_menu():
    #Display the menu options.
    print("\nWelcome to Guessing Game!")
    print("We will play Multiplication Tables.\n")
    print("1. Multiplication Tables Mode")
    print("2. Exit")

def eo_generate_multiplication_problem():
    """Generate a random multiplication problem.

    Returns:
        Tuple[int, int]: A tuple containing two random integers between 1 and 20
    """
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    return num1, num2

def eo_check_multiplication_answer(num1, num2, guess):
    #Check the player's answer for a multiplication problem.
    """Check the player's answer for a multiplication problem.
    Args:
        num1 (int): The first number in the multiplication problem.
        num2 (int): The second number in the multiplication problem.
        guess (int): The player's guess for the product of num1 and num2.

    Returns:
        bool: True if the guess is correct, otherwise False.
    """
    correct_answer = num1 * num2
    return guess == correct_answer

def eo_main():
    #Control the main game loop.

    eo_display_menu()


    """ Play the game.
    Control the main game loop."""
    score = 0
    
    while True:
        
        choice = input("\nEnter 1 to continue, or 2 to terminate: ")
        if choice == '1':
            # Multiplication Tables Mode
            print("\nHint: We will test random number between 1 and 20\n")
            num1, num2 = eo_generate_multiplication_problem()

        #   Exception Handling: 
            try:

                guess = int(input(f"What is {num1} times {num2}? "))
            
            except ValueError:
                print("\nInvalid input. Enter a valid integer.")
                print("Let's try again")
                print("_________________________________________________")

                continue
            
            if eo_check_multiplication_answer(num1, num2, guess):
                print("Correct! Well done! \n")
                print("_________________________________________________")
                score += 1
            else:
                print("Incorrect.\n")
                print("Coreect asnwesr is", num1*num2)
                print("\nLet's try again")

        elif choice == '2':
            print(f"Thanks for playing! {score} games won.\n")
            break
        else:
            print("\nInvalid choice. Please try again.\n")

if __name__ == "__main__":
    eo_main()
