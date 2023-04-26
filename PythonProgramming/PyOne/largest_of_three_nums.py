# This python script receives a user input of three different numbers and returns which number is the largest value


# initialize global variable for script execution completed successfully
goodbye_message = "Thank you for using this program :) " \
                  "\nGoodbye!"


def get_num_input_from_user():
    # initialize variables for error messages
    invalid_input_msg = "Invalid input! You must input three NUMBERS."
    nums_are_equal_msg = "All numbers are equal. Please, input three numbers with different values."
    no_unique_highest_msg = "There is no unique highest number. Please input three numbers with different values."

    while True:
        try:
            # initialize variables for numerical values to be input by user
            num1 = float(input("Insert a number: "))
            num2 = float(input("Insert a number: "))
            num3 = float(input("Insert a number: "))

            # if input numbers are not floats, convert to integers
            if num1.is_integer():
                num1 = int(num1)
            if num2.is_integer():
                num2 = int(num2)
            if num3.is_integer():
                num3 = int(num3)

            # if all numbers are equal, restart the loop
            if num1 == num2 == num3:
                print(f"\n{nums_are_equal_msg}\n")
                continue

            # determine the highest value
            highest_num = max(num1, num2, num3)

            # check if there is only one highest number
            if (num1 == highest_num and num1 != num2 and num1 != num3) or \
                    (num2 == highest_num and num2 != num1 and num2 != num3) or \
                    (num3 == highest_num and num3 != num1 and num3 != num2):
                return num1, num2, num3

            print(f"\n{no_unique_highest_msg}\n")

        except ValueError:
            print(f"\n{invalid_input_msg}\n")


def get_highest_num(num1, num2, num3):
    # initialize variables for messages to be returned alongside the larger value
    highest_num_msg = "The largest number is "

    # initialize variable for the largest number
    highest_num = 0

    # determine the highest value
    if num1 >= num2 and num1 >= num3:
        highest_num = num1
    elif num2 >= num1 and num2 >= num3:
        highest_num = num2
    else:
        highest_num = num3

    # check if there is only one highest number
    if highest_num == num1 and highest_num != num2 and highest_num != num3:
        return highest_num_msg + f"{num1}."
    elif highest_num == num2 and highest_num != num1 and highest_num != num3:
        return highest_num_msg + f"{num2}."
    elif highest_num == num3 and highest_num != num1 and highest_num != num2:
        return highest_num_msg + f"{num3}."
    else:
        return "There is no unique highest number. Please input three numbers with different values."

    # return the largest number with the appropriate message
    # return largest_num_msg + f"{largest_num}."


# initialize variable which calls the function to get the largest number
# initialize the function to get user input as the argument of the largest number function
largest_number = get_highest_num(*get_num_input_from_user())
print(f"\n{largest_number}")

# script finished successfully
print(f"\n{goodbye_message}")
