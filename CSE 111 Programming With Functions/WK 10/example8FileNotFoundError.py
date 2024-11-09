# Example 8
# FileNotFoundError

"""
    If we write a call to the open function that attempts to open 
    a file for reading and that file doesn’t exist, the computer 
    will raise a FileNotFoundError. Example 8 contains code where 
    such an error might occur.
"""
def main():
    try:
        with open("products.vcs", "rt") as products_file:
            for row in products_file:
                print(row)

    except FileNotFoundError as not_found_err:
        print(not_found_err)

if __name__ == "__main__":
    main()