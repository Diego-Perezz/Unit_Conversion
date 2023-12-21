# Filename: project_1.py

### ADD YOUR NAME, STUDENT ID AND SECTION NUMBER BELOW ###
# NAME: Diego Perez Rivera
# STUDENT ID: 802-22-1290
# SECTION: 072
############      DEFINE CONSTANTS BELOW      ############
from email.errors import MisplacedEnvelopeHeaderDefect
from http.client import NON_AUTHORITATIVE_INFORMATION
from unicodedata import numeric


KILOMETERS_PER_MILE = 1.60934
MILES_PER_KILOMETER = 0.621371
KILOGRAMS_PER_POUND = 0.453592
POUNDS_PER_KILOGRAM = 2.20462
MH_PER_KH = 1.60934

############       ADD YOUR CODE BELOW        ############


############ DO NOT MODIFY THE SECTION BELOW  ############


def print_program_menu(): #this function was created to print the menu
    print("\n--------")
    print( "Welcome to the unit conversion program. Please, choose an option:")
    print("1. Miles to kilometers")
    print("2. Kilometers to miles")
    print("3. Pounds to kilograms ")
    print("4. Kilograms to pounds")
    print("5. Miles/hour to kilometers/hour")
    print("6. Exit")



def main():
    done = False
    while not done:
        print_program_menu() #this functio print the menu, you don't need to change it
        userOption = input("Enter option: ")
        #Start writing your code below- don't modify the code lines of this base code
        if userOption.isdigit():  # This Verify that a number was input
            numericOption = int(userOption)    
         # Check if the selection is within permitted range. If it is valid proceed to do the correcponding conversion
            if numericOption == 1:
                number = float(input("Enter the miles to be converted: "))
                kilometers = number * KILOMETERS_PER_MILE
                print(number, "miles are equivalent to",(round(kilometers,2)),"kilometers")

            elif numericOption == 2:
                number = float(input("Enter the kilometers to be converted: "))
                miles = number * MILES_PER_KILOMETER
                print( number, "kilometers are equivalent to",(round(miles,2)),"miles")
            
            elif numericOption == 3:
                number = float(input("Enter the pounds to be converted: "))
                kilograms = number * KILOGRAMS_PER_POUND
                print( number, "pounds are equivalent to",(round(kilograms,2)),"kilograms")

            elif numericOption == 4:
                number = float(input("Enter the kilograms to be converted: "))
                pounds = number * POUNDS_PER_KILOGRAM
                print( number, "kilograms are equivalent to",(round(pounds,2)),"pounds")
            
            elif numericOption == 5:
                number = float(input("Enter the miles/hour to be converted: "))
                km_hr= number * MH_PER_KH
                print( number, "Miles/Hour are equivalent to",(round(km_hr,2)),"kilometers/hour")

            elif numericOption == 6:
                done = True
                print("You have exit the unit conversion program.")
            
            else:
                print("Thanks for using the unit conversion program!")


        else:
            # Option was invalid
             print("Invalid option\n")    









# This line makes python start the program from the main function
if __name__ == "__main__":
    main()






