import csv

from datetime import datetime

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

    # Create an empty dictionary
    compound_dict = {}
        # Open the product.csv file and store its contents into the
        # grocery_order dictonary
    with open (filename, "rt") as csv_file:

            # Create a reader object from the csv module
            reader = csv.reader(csv_file)


            # Skip the first line of code with the headings and read
            # the other lines of texts.
            next(reader)

            # Read each row from the CSV file, one row at a time

            for row_list in reader:

                # For the current row, get the product, name and price
                product = row_list[0]
                name = row_list[1]
                price = row_list[2]

                # From the current row, retrieve the data
                # from the column that contains the key.
                key = row_list[key_column_index]

                # Store the data in the compound_dict.
                compound_dict[key] = row_list
        
    return compound_dict


def main():

    # Getting KeyError that does not exist in the product_dict.
    # under product_details = product_dict.get(product_id)
    try:
        product_dict = read_dictionary("products.csv", 0)
        current_date_and_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        total_items = 0
        subtotal = 0
        tax_rate = .06
        shop_name = "Inkom Emporium"

        # key_column_index = 0

        # print("\n")
        # print("All Products")
        # print(product_dict,"\n")
                
        print(f"\n{shop_name}\n")

        # Open request.csv file for reading in main
        with open('request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            
            # Skip the header
            next(reader)

            # Process each row in the request.csv file
            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                # Retrieve product details from products_dict
                # Potential KeyError zone
                product_details = product_dict.get(product_id)

                product_details = product_dict[product_id]
                product_name = product_details[1]
                product_price = float(product_details[2])
                    
                # Print product name, requested quantity, and product price if
                # there is no KeyError 
                print(f"{product_name}: {quantity} @ {product_price}")

                total_items += quantity
                subtotal += quantity * product_price
                
        sales_tax = tax_rate * subtotal
        total_price = subtotal + sales_tax
    

        print("\n")

        # Add the number quantity items ordered.
        print(f"Number of items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_price:.2f}\n")

        print(f"Thank you for shopping at the {shop_name}.")
        print(current_date_and_time, "\n")

    except FileNotFoundError as not_found_err:
        print("Error: missing file")    
    except KeyError as key_err:
        print(f"\nError: unknown product ID in the request.csv file {key_err}\n")

# Call main to start this program.
if __name__ == "__main__":
    main() 