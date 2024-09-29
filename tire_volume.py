# CSE111 - Aaron Topping
# Assignment Tire Pressure Monitor
# Submitted Sep 15th, 2024

import math
from datetime import datetime

def CalcVolume ( width , aspect , diameter ):
    
    return ( math.pi * (width ** 2) * aspect * (width * aspect + (2540 * diameter) ) ) / 10000000000

print()
def Request_Tire_Values():
    width = float (input ('Enter the width of the tire in mm (ex 205): ') )
    aspect = float (input ('Enter the aspect ratio of the tire (ex 60): ') )
    diameter = float ( input ('Enter the diameter of the wheel in inches (ex 15): ') )
    volume = CalcVolume(width,aspect,diameter)

    return width, aspect, diameter , volume

# PROVE ASSIGNMENT APPENDED 
date = datetime.today()

# Text file tpo import
file_name = "volume.txt"
errorText = 'Error. Please enter in a Y for YES or N for No'

# Exceeding the Requirements - Pricing dictionary
# Prices from www.tiresplus.com
price_table = {
        205: {
            50: {
                15: [158.99, 'TOYO TIRES'],
                16: [121.99, 'TOYO TIRES'],
                17: [138.99, 'TOYO TIRES']
            },
            60: {
                15: [65.99, 'SURE DRIVE'],
                16: [115.99, 'TOYO TIRES'],
                18: [218.99, 'BRIDGESTONE']
            }
        }
    }

# Returns the tire price, and tire brand, and cost for set of 4, assuming it exists, otherwise reports Price is unknown
def GetTirePrice ( wid , asp , dia ):
    if wid in price_table and asp in price_table[wid] and dia in price_table[wid][asp]:
        return (f'Price: {price_table[wid][asp][dia][0]} ({price_table[wid][asp][dia][1]})') , (int(price_table[wid][asp][dia][0]) * 4)
    else:
        return None , None

# Logic to append to file, or create and then append if doesn't exist
def AppendFile ( fileName , textToAppend ):
    with open( fileName , 'a') as file:
        file.write(f'{textToAppend}\n') # Adding a line break for aesthetics
        print(f'{file_name} updated.\n')

# Build the text to append to the file
def BuildReport( width , aspect , diameter , volume ):
    return f'{date:%Y-%m-%d}: {width:.0f}, {aspect:.0f}, {diameter:.0f}, {volume:.2f}'

# To assist with the user input, this informs the user of what tires are available.
def View_Available_Tires():
    count = 1
    for wid , asp in price_table.items():
        for ratio, diam in asp.items():
            for diameter, priceDetails in diam.items():
                print('Prices are from www.tiresplus.com')
                print ( f'#{count}: Width - {wid}, AspectRatio - {ratio}, Diameter - {diameter} || Price - {priceDetails[0]}/ea, Brand - {priceDetails[1]}')
                count += 1

# Runs the entire program at load - Logic handling user inputs and looped questions
def RunProgram():

    recheck = True
    phone = ""
    
    while recheck:
        width, aspect, diameter , volume = Request_Tire_Values()
        print(f'The approximate volume is {volume:.2f} liters')
        print()

        price , setOfFour = GetTirePrice ( width , aspect , diameter )

        if price is not None:
            print(f'Tire is available - {price}')
            while True:
                toBuy = input(f'Would you like to buy a set of 4 tires for ${setOfFour:.2f}? (Y/N) ').lower()
                if toBuy == 'y':
                    phone = input('Please enter your telephone nuymber: ')
                    recheck = False
                    break


                elif toBuy == 'n':
                    while True:
                        user_response = input('Search For Another Tire? (Y/N) ').lower()
                        if user_response == 'y':
                            break
                        elif user_response == 'n':
                            recheck = False
                            break
                        else:
                            print(errorText)
                    break
                else:
                    print(errorText)

        else:

            # Give user option to see all avcailable tires
            while True:
                user_response = input('Tire Unavailable. Would you like to see available tires? (Y/N) ').lower()
                if user_response == 'y':
                    print()
                    View_Available_Tires()
                    print()
                    break
                elif user_response == 'n':
                    break
                else:
                    print(errorText)
            
            # End Program
            while True:
                user_response = input('Search For Another Tire? (Y/N) ').lower()
                if user_response == 'y':
                    break
                elif user_response == 'n':
                    recheck = False
                    break
                else:
                    print(errorText)
    
    print()
    finalReport = BuildReport( width, aspect, diameter , volume )

    if len(phone) > 0:
        finalReport = f'{finalReport}, Phone - {phone}'

    AppendFile ( file_name , finalReport )
    

RunProgram()
