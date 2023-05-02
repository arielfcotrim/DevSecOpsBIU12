# This program prints the natural numbers in a given range in descending order.


def get_range():
    """
    Get the range from the user.
    :return: given_range
    """
    # Error message
    err_msg = "ERROR | Invalid input. Please enter a whole number. \n" \
              "ERROR | Log: \n"

    # New line variable for formatting
    new_line = "\n"

    # Run the loop until the user enters a valid input
    while True:
        try:
            # Get the range from the user
            given_range = int(input("Enter the range: "))

            return given_range

        # If the user enters a non-integer value
        except ValueError as e:
            # Print the error message, the error log and add a new line for readability
            print(err_msg, e, new_line)


def print_natural_nums_in_desc_order(given_range):
    """
    Print the natural numbers in a given range in descending order.
    :param given_range: given_range
    """
    # Print the natural numbers in a given range in descending order
    # The range descends from the value given_range to 0 (not inclusive) in steps of -1
    for i in range(given_range, 0, -1):
        # print the natural numbers in the same line
        print(i, end=" ")


# Main program
# call the function to print the natural numbers and use the function get_range() as the parameter
print_natural_nums_in_desc_order(given_range=get_range())
