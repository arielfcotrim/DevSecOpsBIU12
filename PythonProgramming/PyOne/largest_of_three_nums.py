# This python script receives a user input of three different numbers and returns which number is the largest value


# initialize global variable for script execution completed successfully
goodbye_message = "Thank you for using this program :) " \
                  "\nGoodbye!"

no_unique_highest_msg = "There is no unique highest number..."


def get_num_input_from_user():
    # initialize variables for error messages
    invalid_input_msg = "Invalid input! You must input three NUMBERS; no other characters allowed."
    nums_are_equal_msg = "All numbers are equal..."
    highest_num_rule_explanation = "* There should be at least ONE number with a unique value.\n" \
                                   "* There should be ONLY ONE high number value."

    while True:
        try:
            # initialize variables for numbers as zero since value will be assigned based on input and loop number
            num1 = 0
            num2 = 0
            num3 = 0

            counter = 0
            while counter < 3:
                # initialize variable for rule on suffix
                digit = counter + 1
                suffix = f"{'st' if (counter + 1) == 1 else 'nd' if (counter + 1) == 2 else 'rd' if (counter + 1) == 3 else 'th'}"

                # get input from user using the current loop iteration number and its suffix
                num_input = float(input(f"Insert the {digit}{suffix} number: "))
                # if not float, convert input to int
                if num_input.is_integer():
                    num_input = int(num_input)

                # each loop, assign the current input to the appropriate variable
                if counter == 0:
                    num1 = num_input
                elif counter == 1:
                    num2 = num_input
                else:
                    num3 = num_input

                # if all numbers are equal, print error + rule explanation
                # reset the counter and start over
                if num1 == num2 == num3:
                    print(f"\n{nums_are_equal_msg}"
                          f"\n{highest_num_rule_explanation}"
                          f"\n")
                    continue

                else:
                    # increment the counter if all conditions were met for current loop
                    counter += 1

            # determine the highest value
            highest_num = max(num1, num2, num3)

            # check if there is only one highest number
            if (
                    (num1 == highest_num and num1 != num2 and num1 != num3) or
                    (num2 == highest_num and num2 != num1 and num2 != num3) or
                    (num3 == highest_num and num3 != num1 and num3 != num2)
            ):
                return num1, num2, num3

            # if there are two highest values which are equal, notify user and restart the loop
            print(f"\n{no_unique_highest_msg}"
                  f"\n{highest_num_rule_explanation}"
                  f"\n")

        # catch any values which are not of type float or int
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
        return no_unique_highest_msg

    # return the largest number with the appropriate message
    # return largest_num_msg + f"{largest_num}."


# initialize variable which calls the function to get the largest number
# initialize the function to get user input as the argument of the largest number function
largest_number = get_highest_num(*get_num_input_from_user())
print(f"\n{largest_number}")

# script finished successfully
print(f"\n{goodbye_message}")













# def get_num_input_from_user():
#     # initialize variables for error messages
#     invalid_input_msg = "Invalid input! You must input three NUMBERS."
#     nums_are_equal_msg = "All numbers are equal. Please, input three numbers with different values."
#
#     while True:
#         try:
#             # initialize variables for numerical values to be input by user
#             num1 = float(input("Insert a number: "))
#             num2 = float(input("Insert a number: "))
#             num3 = float(input("Insert a number: "))
#
#             # if input numbers are not floats, convert to integers
#             if num1.is_integer():
#                 num1 = int(num1)
#             if num2.is_integer():
#                 num2 = int(num2)
#             if num3.is_integer():
#                 num3 = int(num3)
#
#             # if all numbers are equal, restart the loop
#             if num1 == num2 == num3:
#                 print(f"\n{nums_are_equal_msg}\n")
#                 continue
#
#             # determine the highest value
#             highest_num = max(num1, num2, num3)
#
#             # check if there is only one highest number
#             if (num1 == highest_num and num1 != num2 and num1 != num3) or \
#                     (num2 == highest_num and num2 != num1 and num2 != num3) or \
#                     (num3 == highest_num and num3 != num1 and num3 != num2):
#                 return num1, num2, num3
#
#             print(f"\n{no_unique_highest_msg}\n")
#
#         except ValueError:
#             print(f"\n{invalid_input_msg}\n")


# def get_highest_num(num1, num2, num3):
#     # initialize variables for messages to be returned alongside the larger value
#     highest_num_msg = "The largest number is "
#
#     # initialize variable for the largest number
#     highest_num = 0
#
#     # determine the highest value
#     if num1 >= num2 and num1 >= num3:
#         highest_num = num1
#     elif num2 >= num1 and num2 >= num3:
#         highest_num = num2
#     else:
#         highest_num = num3
#
#     # check if there is only one highest number
#     if highest_num == num1 and highest_num != num2 and highest_num != num3:
#         return highest_num_msg + f"{num1}."
#     elif highest_num == num2 and highest_num != num1 and highest_num != num3:
#         return highest_num_msg + f"{num2}."
#     elif highest_num == num3 and highest_num != num1 and highest_num != num2:
#         return highest_num_msg + f"{num3}."
#     else:
#         return no_unique_highest_msg

    # return the largest number with the appropriate message
    # return largest_num_msg + f"{largest_num}."