# import the calendar module for getting the day name
import calendar


# define a function to get numerical input from user
def get_num_input():
    # initialize error message variable
    error_message = "Only whole numbers are allowed!"

    # run until user enters a numerical value
    while True:
        try:
            # get input from user
            number = int(input("Enter a number: "))

            return number

        # catch invalid value and throw error message
        except ValueError:
            print(f"\n{error_message}")


# define a function to calculate the day of the week based on a given number
def get_day_of_week(number):
    # the remainder of the division by 7 is the day of the week
    day_of_week = number % 7
    # create a suffix based on the position of the day of the week
    suffix = "st" if day_of_week == 0 or day_of_week == 1 \
        else "nd" if day_of_week == 2 else "rd" if day_of_week == 3 else "th"

    # initialize variables with custom messages
    # if number input is 0, adjust the message to include that the day corresponds to day 1 in Israel
    # this is also a tip of the hat and a wink to python's zero-index format
    day_zero_message = f"The number, {number}, " \
                       f"corresponds to the {day_of_week + 1}{suffix} day of the week in Israel, " \
                       f"{calendar.day_name[day_of_week - 1]}."

    # if number input is any other positive integer, display the corresponding day of the week
    day_message = f"The number, {number}, " \
                  f"corresponds to the {day_of_week}{suffix} day of the week, " \
                  f"{calendar.day_name[day_of_week - 1]}."

    # Note that the -1 and +1 operations are necessary because the calendar.day_name list starts at Monday = 0,
    # while the day_of_week variable starts at Sunday = 0. Therefore, to map between them, we need to subtract
    # one from day_of_week when indexing into the calendar.day_name list, and add one to day_of_week when
    # displaying the result, to get the correct day number.

    # check if the number is 0
    if number == 0:
        return day_zero_message

    # otherwise, check if the number is a positive integer
    else:
        return day_message


# call the functions to get the day of the week and print the result
my_day = get_day_of_week(get_num_input())
print(my_day)
