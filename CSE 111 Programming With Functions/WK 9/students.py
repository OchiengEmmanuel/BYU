# A Python program that uses a student’s I-Number to look up the student’s name

import csv


def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """

    # Create an empty dictionary that will
    # store the data from the CSV file.
    compound_dictionary = {}

        # Open the CSV file for reading and store a reference
    # to the opened file in a variable named csv_file.
    with open(filename, "rt") as csv_file:

        # Use the csv module to create a reader object
        # that will read from the opened CSV file.
        reader = csv.reader(csv_file)

        # Skip the first line of text in the file because it contains 
        # only headings, and read the other lines of the file into a dictionary.
        next(reader)

        # Read the rows in the CSV file one row at a time.
        # The reader object returns each row as a list.
        for row_list in reader:


            # If the current row is not blank, add the
            # data from the current to the dictionary.
            if len(row_list) != 0:

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data from the current
                # row into the dictionary.
                compound_dictionary[key] = row_list

    # Return the dictionary.
    return compound_dictionary


def main():
    filename = "students.csv"

    key_column_index = 0

    compound_dictionary = read_dictionary(filename, key_column_index)

    # Get an I-Number from the user
    i_number = input("Enter the I-Number of the student: ")

    # Remove dashes and white spaces from the I-Number entered by the user
    i_number = i_number.replace("-", "").replace(" ", "")

    # Check if the I-Number exists in the dictionary
    if i_number in compound_dictionary:

        # If the I-Number exists, get the corresponding student name
        # only from the dictionary without the i-number
        student_name = compound_dictionary[i_number][1]
        print(student_name)
    else:
        # If the I-Number doesn't exist.
        print("No such student")

# Call main to start this program.
if __name__ == "__main__":
    main()