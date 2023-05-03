# this python script prints all the prime numbers within a specified range


def greet_prime_numbers():
    """
    This function displays a greeting and explanation of the program.
    :return: None
    """
    # Store the greeting and explanation in variables to make it easier to change them later if needed.
    greeting = " ----:: Welcome to the Prime Number Finder ::----"
    number_input_explanation = " ::Let's define a range within which to search::"

    print(greeting)
    print(number_input_explanation)
    print()


def is_prime(number):
    """
    This function checks if a number is prime.
    :param number: 
    :return: boolean
    """
    # all prime numbers are greater than 1
    if number > 1:
        # check for factors from 2 (first prime number) to the number itself
        for i in range(2, number):
            # if the number is divisible by any factor, it is not prime
            if (number % i) == 0:
                return False

        # if the loop completes without finding any factors, the number is prime
        return True

    # numbers less than or equal to 1 are not prime
    else:
        return False


def get_range_inputs():
    """
    This function returns the start and end range of the range of numbers to be checked.
    :return: tuple
    """
    # display greeting and explanation
    greet_prime_numbers()

    # Error message
    err_msg = "ERROR | Invalid input.\n" \
              "ERROR | You may only enter whole numbers.\n" \
              " INFO | Log - "

    new_line = "\n"

    # loop until the user enters valid input
    while True:
        try:
            # get the start and end range of the range of numbers to be checked
            start = int(input("Enter the start number: "))
            end = int(input("Enter the end number: "))

            # return the start and end range of the range of numbers to be checked
            return start, end

        # catch any exceptions that are raised and print an error message
        except ValueError as e:
            print(err_msg + str(e) + new_line)


def get_primes_in_range(start, end):
    """
    This function returns a list of all the prime numbers within a specified range.
    :param: start
    :param: end
    :return: list
    """
    # initialize a list to store the prime numbers
    prime_numbers = []

    # loop through the range of numbers and check if each is prime
    for number in range(start, end+1):
        if is_prime(number):
            prime_numbers.append(number)

    # return the prime numbers
    return prime_numbers


def print_prime_numbers():
    """
    This function prints all the prime numbers within a specified range.
    :return:
    """
    # get the start and end range of the range of numbers to be checked
    start, end = get_range_inputs()

    # get the prime numbers
    prime_numbers = get_primes_in_range(start, end)

    # create a string to display as the preface for the prime numbers
    console_output = f"Prime numbers between {start} and {end} are:"
    print(console_output)

    # print the prime numbers from the list
    for prime_number in prime_numbers:
        print(prime_number)


# Main program
print_prime_numbers()
