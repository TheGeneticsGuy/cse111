# Author:           Aaron Topping
# Class:            CSE 111
# Prove Milestone:  Grocery Store
# Description:      Takes data from CSV files to build easily accessible dictionary and prints values of items in CSV list
# EXCEEDING REQUIREMENTS:
#   * States how many days until the Jan 1st, 2025 New Year's Sale at bottom of the receipt
#   * Gives a Return By Date
#   * Calculates the number of BOGO items 50% off. In addition, instead of it just being
#       3 items = 1 BOGO, well, 4 items should be 2 of them 50% off, so this calculates
#       how many will be BOGO and how many will be full price. 7 items = 4 full, 3 BOGO 50% off
#       In addition, while not included in the requests.csv, you can add a list of items to the
#       BOGO sale and they will be included

import csv
from datetime import datetime, date, timedelta # For finding time delta between dates, days between, and timestamp
import math # For calculating number of discounted BOGO items

MY_GROCERY_STORE = 'Aaron\'s Grocery Store'
FILE_NAME = 'products.csv'
BOGO_ITEMS = [ 'D083' ]

def get_time():
    """Build the formatted string of the current date and time
    Return: Formatted timestamp
    """
    # Call the now() method to get the current
    # date and time as a datetime object from
    # the computer's operating system.
    current_date_and_time = datetime.now()
    # Use an f-string to print the current
    # day of the week and the current time.
    return (f"{current_date_and_time:%A %b %d %I:%M:%S%p %Y}")     # Ex: Monday Oct 21 03:04:00 PM 2024

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
    products_dict = {}
    try:
        with open(filename, "rt") as csv_file:
            products = csv.reader(csv_file)
            next(products)  # Skip header

            # Building the Dictionary
            for row in products:
                products_dict[row[key_column_index]] = [row[0] , row[1] , row[2] ]      # product_num, name, price
    except FileNotFoundError :
        print()
        print(f'Error: Missing File\nNo such file or directory: \'{filename}\'')

    return products_dict

def get_receipt( product_dict , requested_items ):
    """Build the string of the receipt reflecting all the purchased items, taxes, and total, as well as useful info
    Parameters
        product_dict: The table that includes all product details
        requested_items: Table that includes the requested item by ID and quantity
    Return: The receipt as a string
    """

    receipt = MY_GROCERY_STORE
    num_items = 0
    total_cost = 0
    tax_rate = 0.06
    days_to_return = 30
    sale_items = {}

    # Adding list of Items
    for row in requested_items:

        try:
            item = product_dict[row[0]]
            if not row[0] in BOGO_ITEMS:
                total_cost += float(item[2]) * int(row[1])
                receipt += f'\n{item[1]}: {row[1]} @\t{item[2]}'
                num_items += int(row[1])
            else:   # EXCEEDING REQUIREMENT
                if not row[0] in sale_items:
                    sale_items[row[0]] = [ int(row[1]) , float(item[2]) , item[1] ]    # num items , price , name
                else:
                    sale_items[row[0]][0] += int(row[1])

                num_items += int(row[1])

        except:
            print()
            print(f'Error: unknown product ID in the \'{FILE_NAME}\' file')
            print(f'Unknown product ID: {row[0]}')
            print()

    # Calculating Sale BOGO items
    if len(sale_items) > 0:

        for product in sale_items:

            num_bogo = math.floor( sale_items[product][0] / 2 )
            total_cost += sale_items[product][1] * ( sale_items[product][0] - num_bogo )
            total_cost += ( sale_items[product][1] * 0.50 ) * ( num_bogo )
            receipt += f'\n{sale_items[product][2]}: {( sale_items[product][0] - num_bogo )} @\t{sale_items[product][1]}'
            # BOGO 50% OFF DISCOUNT
            receipt += f'\n    BOGO 50% Off: {num_bogo} @\t{(sale_items[product][1] * 0.50 ):.2f}'

    # Num Items
    receipt += f'\nNumber of Items: {num_items}'

    # Add Subtotal
    receipt += f'\n\nSubtotal:\t{total_cost:.2f}'

    # Add Taxes
    tax = round(total_cost * tax_rate , 2)
    receipt += f'\nSales Tax:\t{tax}'

    # Final Total
    total_cost += tax
    receipt += f'\nTotal:\t\t{total_cost:.2f}'

    # RETURN DATE
    receipt += f'\n\nYou have {days_to_return} days to return ({get_return_date(days_to_return)})'

    # New Year's Sale! - EXCEEDING REQ
    receipt += f'\n\nSave the Date!\nThe New Year\'s Day Sale Begins in {get_days_til_sale()} days'

    # Final message
    receipt += f'\n\nThank you for shopping at {MY_GROCERY_STORE}\n{get_time()}'

    return receipt

### EXCEEDING REQUIREMENTS

# EXCEEDING REQUIREMENTS 1
def get_days_til_sale():

    """Returns the number of days between today's date and the date of the future sale
    Return: The num days as an integer
    """
    num_days = date(2025,1,1) - date.today() # January 1st, 2025
    return num_days.days

# EXCEEDING REQUIREMENTS 2
def get_return_date( days_to_return=30 ):
    '''Returns the future return date based on the number of days until the return
        Parameters: days_to_return  - This allows flexibility in changing return date to be more than just
            default 30 days
        Return: string formatted timestamp of return date
    '''
    today_date = date.today()
    return_date = today_date + timedelta(days=days_to_return)
    return return_date.strftime('%m-%d-%Y')

def main():

    product_dict = read_dictionary(FILE_NAME , 0)
    print()

    if product_dict:
        with open("request.csv", "rt") as csv_file:
            requested_items = csv.reader(csv_file)
            next(requested_items) # Skip header

            print(get_receipt( product_dict , requested_items ))
            print()

if __name__ == "__main__":
    main()