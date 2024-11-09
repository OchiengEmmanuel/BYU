import random
import math

def display_menu():
    """Display the menu options."""
    print("Welcome to the Guessing Game!")
    print("1. Multiplication Tables Mode")
    print("2. Vocabulary Mode")
    print("3. Exit")

def generate_multiplication_problem():
    """Generate a random multiplication problem."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def check_multiplication_answer(num1, num2, guess):
    """Check the player's answer for a multiplication problem."""
    correct_answer = num1 * num2
    return guess == correct_answer

def generate_word():
    """Select a random word from a predefined list."""
    words = {
        "apple": "a round fruit with red or green skin and a whitish inside",
        "dog": "a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, and a barking, howling, or whining voice",
        "book": "a written or printed work consisting of pages glued or sewn together along one side and bound in covers",
    }
    return random.choice(list(words.keys())), words[word]

def check_word_answer(word, definition, guess):
    """Check the player's answer for a word definition."""
    return guess.lower() == definition.lower()

def play_game():
    """Control the main game loop."""
    score = 0
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            # Multiplication Tables Mode
            num1, num2 = generate_multiplication_problem()
            guess = int(input(f"What is {num1} times {num2}? "))
            if check_multiplication_answer(num1, num2, guess):
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        elif choice == '2':
            # Vocabulary Mode
            word, definition = generate_word()
            guess = input(f"What is the meaning of '{word}'? ")
            if check_word_answer(word, definition, guess):
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        elif choice == '3':
            print("Thanks for playing! Your score:", score)
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    play_game()
