# This python script receives a user input of three different numbers and returns which number is the largest value


# initialize global variable for script execution completed successfully
goodbye_message = "Thank you for using this program :) " \
                  "\nGoodbye!"


def get_num_input_from_user():
    # initialize variables for error messages
    invalid_input_msg = "Invalid input! You must input two NUMBERS."
    nums_are_equal_msg = "All numbers are equal. Please, input three numbers with different values."

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

            # get user input to inject into function parameters
            num3 = float(input("Insert the third number: "))
            # if input is an integer, convert its type to integer
            if num3.is_integer():
                num3 = int(num3)

            # if both numbers are equal, restart the loop
            if num1 == num2 and num1 == num3:
                print(f"\n{nums_are_equal_msg}\n")
                continue

            # return the numbers provided by the user
            return num1, num2, num3

        # if any value besides an integer is inputted, print an error message
        except ValueError:
            print(f"\n{invalid_input_msg}\n")


def get_largest_number(num1, num2, num3):
    # initialize variables for messages to be returned alongside the larger value
    largest_num_msg = "The largest number is "

    # initialize variable for the largest number
    largest_num = 0

    # if num1 is larger than num2 and num3, assign its value to the largest_num variable
    if num1 > num2 and num1 > num3:
        largest_num = num1

    # if num2 is larger than num1 and num3, assign its value to the largest_num variable
    elif num2 > num1 and num2 > num3:
        largest_num = num2

    # if num3 is larger than num1 and num2, assign its value to the largest_num variable
    else:
        largest_num = num3

    # return the largest number with the appropriate message
    return largest_num_msg + f"{largest_num}."


# initialize variable which calls the function to get the largest number
# initialize the function to get user input as the argument of the largest number function
largest_number = get_largest_number(*get_num_input_from_user())
print(f"\n{largest_number}")

# script finished successfully
print(f"\n{goodbye_message}")
