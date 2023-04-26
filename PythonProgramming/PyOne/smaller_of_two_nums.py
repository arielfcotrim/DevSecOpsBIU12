# This python script receives a user input of two different numbers and returns which number is the smallest value

# initialize variable for message to be returned if both numbers are equal
nums_are_equal_msg = "Both numbers are equal. Please, input two numbers with different values."


def get_smallest_number(num1, num2):
    # initialize variable for messages to be returned alongside the smaller value
    smallest_num_msg = "The smallest number is "

    # if num1 is smaller than num2, return it with the appropriate message
    if num1 < num2:
        return smallest_num_msg + f"{num1}."

    # else, return num2 with the appropriate message
    else:
        return smallest_num_msg + f"{num2}."


def get_num_input_from_user():
    # the script should run until the conditions are met
    while True:
        try:
            # get user input to inject into function parameters
            num_input_1 = float(input("Insert your first number: "))
            num_input_2 = float(input("Insert your second number: "))

            # check if inputted numbers are integers
            # if so, convert them to integers in order to print the correct message
            if num_input_1.is_integer():
                num_input_1 = int(num_input_1)

            if num_input_2.is_integer():
                num_input_2 = int(num_input_2)

            # if both numbers are equal, restart the loop
            if num_input_1 == num_input_2:
                print(f"\n{nums_are_equal_msg}\n")
                continue

            # call function to get the smallest number and print the message
            print(f"\n{get_smallest_number(num_input_1, num_input_2)}")

            # then, break out of the loop
            break

        # if any value besides an integer is inputted, print an error message
        except ValueError:
            print("\nInvalid input! You must input two NUMBERS.\n")


# call function that receives user input of two different number values
# this function also calls the function to get the smallest number
get_num_input_from_user()

# script finished successfully
print("\nThank you for using this program :)"
      "\nGoodbye!")
