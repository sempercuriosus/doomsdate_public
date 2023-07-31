# <author> @SemperCuriosus -EH
# <created on> 07-Jun-2023

from datetime import date
import random
import sys
import argparse
parser = argparse.ArgumentParser(description='Enter a date and get the day of the week or get a date and guess the day!', add_help=True)
parser.add_argument('-d', '--date', type=str, nargs=1, help="Enter the date in dd-mm-yyyy format.")
parser.add_argument('-g', '--game', nargs='*', help="Gives a date to test your skills.")
args = parser.parse_args()

class Doomsday:
    def __init__(self):
        # --------------------------------------------------------
        # --------------------------------------------------------
        # print("Initialize Doomsdate Class")
        self.date: str = ''
        self.year: int = 0
        self.month: int = 0
        self.day: int = 0
        self.century_anchor_day: int = 0
        self.anchor_day: int = 0 
        self.anchor_day_name: str = '' 
        self.day_of_week_number: int = 0 
        self.is_leap_year: bool = False

    def get_doomsday(date, doomsday):
        # --------------------------------------------------------
        # This is an entry into the remaining calculations, assignments, etc. to be done.
        # --------------------------------------------------------
        # setting the class property to be the date provided
        doomsday.date = date
        # checks if the date provided is valid
        Doomsday.is_date_valid(doomsday)
        #   get the century's anchor date
        Doomsday.get_century_anchor(doomsday)
        # check if the year is a leap year
        Doomsday.is_leap_year(doomsday)
        # algorithm to calculate a given year's anchor day
        Doomsday.odd_plus_11(doomsday)
        # combine the centurty and year anchors, divide by 7 to keep the number in the range of the week
        Doomsday.add_century_anchor(doomsday)
        # convert the anchor int to the anchor day 
        Doomsday.set_anchor_day_name(doomsday)
        # return day of week
        Doomsday.find_day_of_week(doomsday)

    def is_date_valid(doomsday): 
        # --------------------------------------------------------
        # checks if the date provided is not as expected, checking for the slash, dot formats
        # --------------------------------------------------------
        date = doomsday.date
        delimiter = '-' #defaulting to this to avoid a second check.
        
        if (date != None and date != ''):
            if (date.__contains__('/')):
                delimiter = '/'
            elif (date.__contains__('.')):
                delimiter = '.'
            else:
                pass
            try:
                # split the date at the delimiter
                date = date.split(delimiter)
                
                Doomsday.assign_date(doomsday, date)
            except:
                print(f'The date was not assigned.')

    def assign_date(doomsday, date):
        # --------------------------------------------------------
        # assigning the date parts if within the ranges set.
        # --------------------------------------------------------
        # print("Parse and Validating the date input...")
        try:
            # check day
            if (int(date[0]) >= 1 and int(date[0]) <= 31):
                doomsday.day = int(date[0]) 
            # check month
            if (int(date[1]) >= 1 and int(date[1]) <= 12):
                doomsday.month = int(date[1])
            # check year
            if (int(date[2]) >= 1600 and int(date[2]) <= 2199):
                doomsday.year = int(date[2])

            date(doomsday.year, doomsday.month, doomsday.day)
        except:
            print('Date was not valid')
            sys.exit(1)

    def get_century_anchor(doomsday):
        # --------------------------------------------------------
        # Determines the given year's anchor, by range.
        # --------------------------------------------------------
        year = doomsday.year
        
        if (year >= 1600 and year <= 1699):
            doomsday.century_anchor_day = 2
        elif(year >= 1700 and year <= 1799 ):
            doomsday.century_anchor_day = 0
        elif(year >= 1800 and year <= 1899 ):
            doomsday.century_anchor_day = 5
        elif(year >= 1900 and year <= 1999 ):
            doomsday.century_anchor_day = 3
        elif(year >= 2000 and year <= 2099 ):
            doomsday.century_anchor_day = 2
        elif(year >= 2100 and year <= 2199 ):
            doomsday.century_anchor_day = 0
        else:
            print(f"[ {year} ] fell outside the range 1600 to 2100")
        
        print(f'Century Anchor Day is : [ {Doomsday.convert_number_to_day(doomsday.century_anchor_day)} ]')

    def convert_number_to_day(day):
        # --------------------------------------------------------
        # Takes an int and returns a day of the week 
        # --------------------------------------------------------

        try:
            if (day == 0):
                anchor_day_name = 'Sunday'
            elif(day == 1):
                anchor_day_name = 'Monday'
            elif(day == 2):
                anchor_day_name = 'Tuesday'
            elif(day == 3):
                anchor_day_name = 'Wednesday'
            elif(day == 4):
                anchor_day_name = 'Thursday'
            elif(day == 5):
                anchor_day_name = 'Friday'
            elif(day == 6):
                anchor_day_name = 'Saturday'
            else:
                print(f'Day of week integer [ {day} ] was out of range')
                
            return anchor_day_name
        
        except Exception as e:
            print(str(e))

    def odd_plus_11(doomsday):
        # --------------------------------------------------------
        # algorithm to calculate a given year's anchor day
        # --------------------------------------------------------
        try:
            anchor_temp = int(str(doomsday.year)[-2:])
        except:
            print('Last two digit from the year could not be set.')

        try:
            print() # adding a blank line
            # If the value is odd then add 11
            if (anchor_temp % 2 == 1):
                anchor_temp += 11
                print(f'Odd add 11 : [ {str(anchor_temp)} ]')
            # If the value is even then do nothing
            
            # divide by 2     
            anchor_temp = int((anchor_temp / 2))
            print(f'Dividing by 2 : [ {str(anchor_temp)} ]')

            # If the value is odd then add 11
            if (anchor_temp % 2 == 1):
                anchor_temp += 11
                print(f'Odd add 11 : [ {str(anchor_temp)} ]')

            # If the value is even do nothing

            anchor_temp = (7 - (anchor_temp % 7))
            print(f'Result : [ {str(anchor_temp)} ]')
            print()

            # assign the anchor 
            doomsday.anchor_day = anchor_temp
        except:
            pass

    def add_century_anchor(doomsday):
        # --------------------------------------------------------
        # combine the centurty and year anchors, divide by 7 to keep the number in the range of the week
        # --------------------------------------------------------
        doomsday.anchor_day = ((doomsday.century_anchor_day + doomsday.anchor_day) % 7)

    def set_anchor_day_name(doomsday):
        # --------------------------------------------------------
        # convert the anchor int to the anchor day 
        # --------------------------------------------------------
        anchor_day_name = Doomsday.convert_number_to_day(doomsday.anchor_day)
        print (f'[ {doomsday.year} ]\'s anchor day is : [ {anchor_day_name} ]')

    def is_leap_year(doomsday):
        # --------------------------------------------------------
        # Determines if the given year is a leap year
        # --------------------------------------------------------
        try:
            if((doomsday.year % 4) == 0):
                doomsday.is_leap_year = True
        except:
            print(f'Could not calculate the Leap Year value. [ {doomsday.year} ]')

    def find_day_of_week(doomsday):
        # --------------------------------------------------------
        # Gets the given month's "special day" from which the doomsday can be calculated
        # --------------------------------------------------------
        if (doomsday.month == 1):
            if (doomsday.is_leap_year == True):
                special_day = 31
            else:
                special_day = 32
        elif(doomsday.month == 2):
            if (doomsday.is_leap_year == True):
                special_day = 29
            else:
                special_day = 28
        elif(doomsday.month == 3):
            special_day = 14
        elif(doomsday.month == 4):
            special_day = 4
        elif(doomsday.month == 5):
            special_day = 9
        elif(doomsday.month == 6):
            special_day = 6
        elif(doomsday.month == 7):
            special_day = 11
        elif(doomsday.month == 8):
            special_day = 8
        elif(doomsday.month == 9):
            special_day = 5
        elif(doomsday.month == 10):
            special_day = 10
        elif(doomsday.month == 11):
            special_day = 7
        elif(doomsday.month == 12):
            special_day = 12
        else:
            print('There was an issue finding the month\'s doomsday')
        
        # Doomsdate.get_day_of_week(doomsday.anchor_day, doomsday.day)
        Doomsday.date_diff(doomsday, special_day)

    def date_diff(doomsday_obj, special_day):
        # --------------------------------------------------------
        # Calculates the final day of the week, giving the user their answer.
        # --------------------------------------------------------
        
        try:
            # Get the properties
            day = doomsday_obj.day
            month = doomsday_obj.month
            year = doomsday_obj.year
            anchor = doomsday_obj.anchor_day
        except:
            print('Could not assign the Doomsday properties to calculate with.')

        try:
            # Check the start date is valid
            start_date = date(year, month, day)
        except:
            print(f'{start_date} is not valid.')

        try:
            # Check the end date is valid
            end_date = date(year, month, special_day)
        except:
            print(f'{end_date} is not valid.')

        try:
            date_diff_result = (((start_date.day-end_date.day) + anchor) % 7)
            answer = Doomsday.convert_number_to_day(date_diff_result)
            
            # format the output
            print()
            print('----------------------------------------------------------------------')
            print(f'The date [ {doomsday_obj.date} ] was on the day : [ {answer} ]')
            print('----------------------------------------------------------------------')
            print()            
        except:
            pass

def __main__():
    # --------------------------------------------------------
    # Main to handle flow of the app
    # --------------------------------------------------------
    welcome_message = """
    Doomsday Algorithm 
        A calculator and game - Based on works by John Conway and Lewis Carrol.
    """
    input_message = """-- [ Menu: ] --
    - Game 
        - Press the 'g' and then 'Enter'
    - Date Check 
        - Press the 'd' and then 'Enter'
    """
    continue_message = """--[ Do you want to continue?  ]--
    Press [ \'Enter\' ] to continue 
        - OR - 
    Press [ \'q\' ] then [ \'Enter\' ] to quit."""
    user_input = ''
    user_continue_answer = ''
    continue_run = True

    print()
    print(welcome_message)

    while(continue_run != False):        

        # checking if there were command lines passed in
        if (len(sys.argv) > 1):
            # checking the command value passed in
            if (args.date != None):
                # print(f'arguments : [ {args.date} ]')
                ask_user_for_date()
            elif (args.game != None):
                # print(f'arguments : [ {args.game} ]')
                quiz_mode()
            else:
                print("Command argument was not found.")
        else:
            print(input_message)

            # ask user for option
            user_input = input()

            if(user_input.lower() == 'g'):
                quiz_mode()
            elif (user_input.lower() == 'd'):
                ask_user_for_date()
            else:
                print(f'The option [ {user_input} ] was not found.')

        #
        print()
        print(continue_message)
        # another one?
        user_continue_answer = input()
        #
        if (user_continue_answer == "q"):
            continue_run = False
    print('-------------------------------------------------------------')
    print(" - Complete - ")

def ask_user_for_date():
    # --------------------------------------------------------
    # asks the user for a date to check the day of the week for
    # --------------------------------------------------------
    if (args.date == None):
        message = """--[ Enter the date ]--
        format :  dd-mm-yyyy"""

        print(message)
        #   get date from user
        user_date = input()
    else:
        print("Accepting Date Command Option")
        print(args.date[0])

        user_date = args.date[0]
    #   testing
    # user_date = select_random_date()
    create_new_doomsday(user_date)

def create_new_doomsday(date):
    # --------------------------------------------------------
    # Serves as an entry into the Doomsdate class and starts the work done
    # --------------------------------------------------------
    #   create new class instance
    doomsday = Doomsday()
    #   run the method
    Doomsday.get_doomsday(date, doomsday)

def quiz_mode():
    # --------------------------------------------------------
    # Dets a random date to quiz the user
    # --------------------------------------------------------
    print('--[ Getting a date... ]--')
    random_date = select_random_date()

    print(f'Your date to guess is : ')
    print()
    print(f'[   {random_date}   ]')
    print()
    input()

    print('When ready to check the date press [ \'Enter\' ] to continue.')
    
    create_new_doomsday(random_date)
    
def select_random_date():
    # --------------------------------------------------------
    # Generates a random day, month, year to use as a test.
    # --------------------------------------------------------
    # I know this does not account for random days that would not work.
    day = random.randrange(1,31)
    month = random.randrange(1,12)
    year = random.randrange(1600, 2199)

    return str(day) + '-' + str(month) + '-' + str(year)

__main__()

