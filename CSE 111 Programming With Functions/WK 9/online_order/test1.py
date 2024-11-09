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
    compound_dict = {}

    with open(filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # Skip header row
        for row_list in reader:
            key = row_list[key_column_index]
            compound_dict[key] = row_list

    return compound_dict

def main():
    try:
        product_dict = read_dictionary("products.csv", 0)
        current_date_and_time = datetime.now().strftime("%a %b %d %H:%M:%S %Y")
        total_items = 0
        subtotal = 0
        tax_rate = 0.06
        total_price = 0

        with open('request.csv', 'rt') as request_file:
            reader = csv.reader(request_file)
            next(reader)  # Skip header row
            
            print("Ordered Items:")

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])
                try:
                    product_details = product_dict[product_id]
                    product_name = product_details[1]
                    product_price = float(product_details[2])
                    print(f"{product_name}: {quantity} @ {product_price}")
                    total_items += quantity
                    subtotal += quantity * product_price
                except KeyError as key_err:
                    print(f"Error: unknown product ID '{product_id}' in the request.csv file")

            sales_tax = tax_rate * subtotal
            total_price = subtotal + sales_tax

        print("\n")
        print(f"Number of items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total_price:.2f}\n")
        print("Thank you for shopping.")
        print(f"Ordered on {current_date_and_time}")

    except FileNotFoundError as not_found_err:
        print(f"Error: {not_found_err}")

if __name__ == "__main__":
    main()
