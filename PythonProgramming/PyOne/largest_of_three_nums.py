# This python script receives a user input of three different numbers and returns which number is the largest value

# initialize variable for message to be returned if both numbers are equal
no_unique_largest_num_msg = "There is no unique highest number. Please input three numbers with different values."


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
    elif num3 > num1 and num3 > num2:
        largest_num = num3

    # return the largest number with the appropriate message
    return largest_num_msg + f"{largest_num}."


def get_num_input_from_user():
    # the script should run until the conditions are met
    while True:
        try:
            # get user input to inject into function parameters
            num_input_1 = float(input("Insert your first number: "))
            num_input_2 = float(input("Insert your second number: "))
            num_input_3 = float(input("Insert your third number: "))

            # check if inputted numbers are integers
            # if so, convert them to integers in order to print the correct message
            if num_input_1.is_integer():
                num_input_1 = int(num_input_1)

            if num_input_2.is_integer():
                num_input_2 = int(num_input_2)

            if num_input_3.is_integer():
                num_input_3 = int(num_input_3)

            # if both numbers are equal, restart the loop
            if num_input_1 == num_input_2:
                print(f"\n{no_unique_largest_num_msg}\n")
                continue

            # call function to get the smallest number and print the message
            print(f"\n{get_largest_number(num_input_1, num_input_2, num_input_3)}")

            # then, break out of the loop
            break

        # if any value besides an integer is inputted, print an error message
        except ValueError:
            print("\nInvalid input! You must input three NUMBERS.\n")


# call function that receives user input of two different number values
# this function also calls the function to get the smallest number
get_num_input_from_user()

# script finished successfully
print("\nThank you for using this program :)"
      "\nGoodbye!")
