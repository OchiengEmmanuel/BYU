def main():
    # Ask the user to input a list of fruits
    fruits_input = input("Enter a list of fruits (separated by commas): ")

    # Split the input string by commas to get individual fruit names
    fruits = fruits_input.split(",")

    # Trim whitespace from each fruit name
    fruits = [fruit.strip() for fruit in fruits]

    # Print the list of fruits entered by the user
    print("List of fruits entered by the user:")
    for fruit in fruits:
        print(fruit)

if __name__ == "__main__":
    main()
