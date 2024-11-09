import datetime

def calculate_discount(subtotal):
    day_of_week = datetime.datetime.today().strftime('%A')
    
    discount = 0
    if subtotal >= 50 and (day_of_week == 'Tuesday' or day_of_week == 'Wednesday'):
        discount = 0.10 * subtotal
    
    sales_tax = 0.06 * subtotal
    total_amount_due = subtotal - discount + sales_tax

    return discount, sales_tax, total_amount_due

def main():
    try:
        subtotal = float(input("Enter the customer's subtotal: $"))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    discount, sales_tax, total_amount_due = calculate_discount(subtotal)

    print("\nSummary:")
    print(f"Discount amount: ${discount:.2f}")
    print(f"Sales tax amount: ${sales_tax:.2f}")
    print(f"Total amount due: ${total_amount_due:.2f}")

if __name__ == "__main__":
    main()
