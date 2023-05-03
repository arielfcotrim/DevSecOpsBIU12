# this python program reverses a number input from the user.


def get_number():
    """
    Get the word from the user.
    :return: word
    """
    # Initialize variables to hold Error Messages
    single_digit_err_msg = "ERROR | Please enter at least two digits.\n"
    not_numeric_err_msg = "ERROR | Please enter a whole number. Floats, characters and letters are not allowed.\n"

    # Run the loop until the user enters a valid input
    while True:
        # try to get the number from the user
        try:
            number = input("Enter a number: ")

            # single digits cannot be reversed
            if number.isnumeric() and len(number) <= 1:
                raise ValueError(single_digit_err_msg)

            # only whole numbers are allowed
            elif not number.isnumeric():
                raise ValueError(not_numeric_err_msg)

            return number

        # if the user enters a value that is not a single word, an error message of the specific mistake is displayed
        except ValueError as e:
            print(e)


def reverse_number(number):
    """
    Reverse the word.
    :param: number
    :return: reversed_number
    """
    # message to be displayed on the console
    console_message = "Your number in reverse comes out as: "

    # pythonic way to reverse a string
    reversed_number = number[::-1]

    # return the console message concatenated with the reversed word
    return console_message + reversed_number


# Main program
# call the function to reverse the word and use the function get_word() as the parameter
my_word_reversed = reverse_number(number=get_number())
print(my_word_reversed)
