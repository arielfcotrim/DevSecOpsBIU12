# This python script receives a user input of three different numbers and returns which number is the largest value


# initialize global variable for script execution completed successfully
goodbye_message = "Thank you for using this program :) " \
                  "\nGoodbye!"

# initialize variables for error messages
invalid_input_msg = "Invalid input! You must input three NUMBERS; no other characters allowed."
no_unique_highest_msg = "There is no unique highest number..."

# rules explanation message
highest_num_rule_explanation = "* There should be at least ONE number with a unique value.\n" \
                               "* There should be ONLY ONE highest number value."


def get_num_input_from_user():
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

        counter += 1

    return num1, num2, num3


def is_highest_number_unique(num1, num2, num3):
    # determine the highest value
    highest_num = max(num1, num2, num3)

    # check if there is only one highest number
    if (
            (num1 == highest_num and num1 != num2 and num1 != num3) or
            (num2 == highest_num and num2 != num1 and num2 != num3) or
            (num3 == highest_num and num3 != num1 and num3 != num2)
    ):
        return highest_num

    else:
        return None


def set_highest_number():
    while True:
        try:
            # get input from user
            num1, num2, num3 = get_num_input_from_user()

            # check if there is a unique highest number
            highest_num = is_highest_number_unique(num1, num2, num3)
            if highest_num is not None:
                return highest_num

            # if there are two highest values which are equal, notify user and restart the loop
            print(f"\n{no_unique_highest_msg}"
                  f"\n{highest_num_rule_explanation}"
                  f"\n")

        # catch any values which are not of type float or int
        except ValueError:
            print(f"\n{invalid_input_msg}\n")


def display_highest_number():
    # initialize variables for messages to be returned alongside the larger value
    highest_num_msg = "The highest number is "
    highest_num = set_highest_number()

    return f"{highest_num_msg}" + f"{highest_num}."


# initialize variable which calls the function to get the largest number
# initialize the function to get user input as the argument of the largest number function
highest_number = display_highest_number()
print(f"\n{highest_number}")

# script finished successfully
print(f"\n{goodbye_message}")
