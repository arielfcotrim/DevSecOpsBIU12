# This python script receives a user input of two different numbers and returns which number is the smallest value


# initialize global variable for script execution completed successfully
goodbye_message = "Thank you for using this program :) " \
                  "\nGoodbye!"


def get_num_input_from_user():
    # initialize variables for error messages
    invalid_input_msg = "Invalid input! You must input two NUMBERS."
    nums_are_equal_msg = "Both numbers are equal. Please, input two numbers with different values."

    # the script should run until the conditions are met
    while True:
        try:
            # get user input to inject into function parameters
            num1 = float(input("Insert the first number: "))
            # if input is an integer, convert its type to integer
            if num1.is_integer():
                num1 = int(num1)

            # get user input to inject into function parameters
            num2 = float(input("Insert the second number: "))
            # if input is an integer, convert its type to integer
            if num2.is_integer():
                num2 = int(num2)

            # if both numbers are equal, restart the loop
            if num1 == num2:
                print(f"\n{nums_are_equal_msg}\n")
                continue

            # if two valid and non-identical numerical values are input, return both values (breaks out of the loop)
            return num1, num2

        # if any value besides a number is provided, print an error message
        except ValueError:
            print(f"\n{invalid_input_msg}\n")


def get_smallest_number(num1, num2):
    # initialize variable for messages to be returned alongside the smaller value
    smallest_num_msg = "The smallest number is "

    # if num1 is smaller than num2, return it with the appropriate message
    if num1 < num2:
        return smallest_num_msg + f"{num1}."

    # else, return num2 with the appropriate message
    else:
        return smallest_num_msg + f"{num2}."


smallest_number = get_smallest_number(*get_num_input_from_user())
print(f"\n{smallest_number}")

# script finished successfully
print(f"\n{goodbye_message}")
