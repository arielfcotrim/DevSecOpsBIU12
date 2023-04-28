# This python script is used to get a month from a user input and then determine how many days there are in that month.
# import libraries to automatically set custom date and time values instead of hard-coding the values
import calendar
from datetime import datetime


def get_month():
    """
        Prompts the user to enter a numeric value representing a month (1-12),
        determines the number of days in that month, and returns a string with
        the month's name, year, and number of days.

        :return: A string with the month's name, year, and number of days.
        """
    # initialize error message variable
    invalid_value_msg = "Please enter a numeric value from 1 to 12."

    # run until the user enters a valid value
    while True:
        try:
            month = int(input("Please enter the month's number (1-12): "))

            # check if input value is a valid month number
            if 1 <= month <= 12:
                # get the month's name from calendar module for the month number input
                month_name = calendar.month_name[month]
                # get the current year of the world using the datetime module
                year = datetime.now().year
                # check how many days there are in the specified month of the current year
                month_days = calendar.monthrange(year, month)[1]

                # message with all the info stored in the variables
                return f"{month_name} {year} has {month_days} days."

            # if input value is not a valid month number, catch the exception and print the error message
            else:
                print(f"{invalid_value_msg}\n")

        # if input value is not an integer, catch the exception and print the error message
        except ValueError:
            print(f"{invalid_value_msg}\n")


my_month = get_month()
print(my_month)
