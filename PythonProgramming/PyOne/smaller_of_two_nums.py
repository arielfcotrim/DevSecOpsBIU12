# This python script receives a user input of three different numbers and returns which number is the largest value
# Yes, this is overkill. But I wanted to write as a program that attempts to take all possibilities into account.
# A program for something this simple should have zero bugs and should not stop running until concluded successfully.


# initialize global variable for script execution completed successfully
goodbye_message = "Thank you for using this program :) " \
                  "\nGoodbye!"

# initialize variables for error messages
invalid_input_msg = "Invalid input! Input is not a numerical value..."
values_are_identical_msg = "Both numbers are identical..."

# rules explanation message
input_rule_explanation = "* You are allowed to input only numerical (integers and floats) values.\n" \
                         "* The value of each number must be unique."


def get_num_input_from_user():
    # initialize variables for numbers as zero since value will be assigned based on input and loop number
    num1 = 0
    num2 = 0

    counter = 0
    while counter < 2:
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
        else:
            num2 = num_input

        counter += 1

    return num1, num2


def is_value_identical(num1, num2):
    # determine the highest value
    highest_num = max(num1, num2)

    # check if there is only one highest number
    if num1 != num2:
        return highest_num

    else:
        return None


def set_highest_number():
    while True:
        try:
            # get input from user
            num1, num2 = get_num_input_from_user()

            # check if there is a unique highest number
            highest_num = is_value_identical(num1, num2)
            if highest_num is not None:
                return highest_num

            # if there are two highest values which are equal, notify user and restart the loop
            print(f"\n{values_are_identical_msg}"
                  f"\n{input_rule_explanation}"
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
