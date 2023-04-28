# This python script checks is a number can be divided by 3 without any remainder.


# Function to get a number from the user
def get_number_input():
    """
    Prompts the user to enter a whole number and returns it.
    If the user inputs a non-integer value, an error message is displayed and the user is prompted again.
    :return: number
    """
    while True:
        try:
            # input from the user must be an integer (whole number)
            number = int(input("Enter a whole number: "))

            return number

        # if value input from user is not an integer, throw an error and restart the loop
        except ValueError:
            print("\nOnly whole numbers are allowed.\n")


# this function checks if a number can be divided by 3 without any remainder
def is_divisible_by_3():
    """
    Calls the get_number_input function to prompt the user to enter a whole number.
    Returns True if the number entered is divisible by 3 without any remainder, and False otherwise.
    :return: boolean
    """
    # initialize a variable to store the number entered by the user by calling the function
    number = get_number_input()

    # check if dividing by 3 produces a remainder of 0
    if number % 3 == 0:
        # if divisible by 3...
        return True

    # if not divisible by 3...
    else:
        return False


print(f"\n{is_divisible_by_3()}")
