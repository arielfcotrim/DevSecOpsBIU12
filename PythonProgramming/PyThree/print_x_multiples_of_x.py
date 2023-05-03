# this python script prints the first x multiples of a number.


# Initialize variables to hold Error Messages
err_msg = "ERROR | Number of loops must be an integer greater than 0.\n"
log_msg = "LOG: \n"
odd_number_err_msg = "invalid range input: 'odd number'"
new_line = "\n"


def get_range():
    """
    How many times to loop == how many multiples of x to print.
    :return: loops
    """

    # Run the loop until the user enters a valid input
    while True:
        # try to get the number from the user
        try:
            loops = int(input("Number of loops: "))

            # checks that number of loops is an even number
            if loops <= 0:
                raise ValueError(odd_number_err_msg)

            return loops

        # if the user enters a value that is not a whole even number, display error message
        except ValueError as e:
            print(err_msg, log_msg, e, new_line)


def get_number():
    """
    Number to print multiples of.
    :return: number
    """

    while True:
        try:
            number = float(input("Number to print multiples of: "))

            return number

        except ValueError as e:
            print(err_msg, log_msg, e, new_line)


def get_multiples(loops, number):
    """
    Print multiples of number.
    :param loops: number of loops
    :param number: number to print multiples of
    :return: None
    """
    # Initialize variable to hold multiples
    multiples = ""

    # Initialize multiplier
    multiplier = 1
    # Loop through the range of loops
    for i in range(loops):
        # Multiply the number by the current multiplier
        multiple = number * multiplier

        # If the multiple is a whole number, convert it to an integer
        if multiple.is_integer():
            multiple = int(multiple)

        # Concatenate the multiple to the multiples string
        multiples += str(multiple) + " "

        # Increment the multiplier
        multiplier += 1

    return multiples


# Main program
my_multiples = get_multiples(get_range(), get_number())
print(my_multiples)
