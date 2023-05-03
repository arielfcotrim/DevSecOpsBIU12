# this python script will add 2 or more numbers together

def addition_calculator():
    """
    This function repeatedly asks the user to enter numbers and adds them to a running total until the user inputs "add".
    :return: running_total: The sum of all the numbers entered by the user.
    """
    # Store the greeting and explanation in variables to make it easier to change them later if needed.
    greeting = " ----:: Welcome to the Addition Calculator ::----"
    number_input_explanation = "  :: You may add 2 or more numbers each time ::"

    # Store the error messages in variables to make it easier to change them later if needed.
    invalid_input_err_msg = "ERROR | Invalid input.\n" \
                            "ERROR | You may only enter numerical values or the word 'add'.\n" \
                            " INFO | Log - "
    must_input_two_numbers_err_msg = "ERROR | You must enter at least 2 numbers before you can add them.\n"
    try_again = "INFO | Please start over...\n"

    # custom new_line variable to make it easier to add new lines to the print statements.
    new_line = "\n"

    # Store the word "add" in a variable to make it easier to change it later if needed.
    add = "add"

    # Initialize the running total to 0.0 and increment at the end of the loop.
    running_total = 0.0

    # Display welcome message and instructions for using the calculator
    print(greeting)
    print(number_input_explanation)
    print()

    # Initialize the counter to 0 and increment at the end of the loop.
    counter = 0
    while True:
        try:
            user_input = input("Enter the numbers you would like to add and type 'add' when you are done: ")

            # If the user enters "add" and at least two numbers have been entered, break the loop
            if user_input == add and counter > 1:
                break

            # If the user enters "add" and less than two numbers have been entered, raise an Exception
            elif user_input == add and counter <= 1:
                raise Exception(must_input_two_numbers_err_msg)

            # If the user enters something other than a number or "add", raise a ValueError
            if not float(user_input) and not add:
                raise ValueError(invalid_input_err_msg)

            counter += 1

            # Convert user input to a float and add it to the running total
            number = float(user_input)
            running_total += number

        # Catch any exceptions that are raised and print an error message
        except ValueError as e:
            print(invalid_input_err_msg + str(e), new_line, try_again)
            continue

        except Exception as e:
            print(e, try_again, new_line)
            continue

    # If the running total is an integer, convert it to an integer before returning it
    if running_total.is_integer():
        running_total = int(running_total)

    return running_total


# Main program
my_addition_calculator = addition_calculator()
print(my_addition_calculator)
