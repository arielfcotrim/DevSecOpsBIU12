# this python script prints all the prime numbers between 1 and x using the Sieve of Eratosthenes algorithm.


def hello_from_sieve():
    """
    This function displays a greeting and explanation of the program.
    :return: None
    """
    # Store the greeting and explanation in variables to make it easier to change them later if needed.
    greeting = "              ----:: Welcome to the Prime Number Finder ::----"
    number_input_explanation = \
        ":: This program uses the Sieve of Eratosthenes algorithm to find all the prime numbers ::" \

    print(greeting)
    print(number_input_explanation)
    print()


def get_limit():
    """
    This function returns the start and end range of the range of numbers to be checked.
    :return: tuple
    """
    # display greeting and explanation
    hello_from_sieve()

    # Error message
    invalid_input_err_msg = "ERROR | You may only enter whole numbers.\n"
    invalid_limit_err_msg = "ERROR | You must enter a number greater than 2.\n"
    log_msg = " INFO | Log - "

    new_line = "\n"

    # loop until the user enters valid input
    while True:
        try:
            # get the start and end range of the range of numbers to be checked
            limit = int(input("Enter the upper end of the range: "))

            if limit < 3:
                raise Exception(invalid_limit_err_msg)

            # return the start and end range of the range of numbers to be checked
            return limit

        # catch any exceptions that are raised and print an error message
        except ValueError as e:
            print(invalid_input_err_msg + log_msg + str(e) + new_line)

        except Exception:
            print(invalid_limit_err_msg)


def get_prime_numbers(limit):
    """
    This function uses the Sieve of Eratosthenes algorithm to generate a list of prime numbers up to a given limit.
    :param: limit (int): The upper bound of the range to check for primes
    :return: list: A list of prime numbers within the specified range
    """
    # Create a boolean list indicating whether each number is prime, initialized to True for all numbers up to limit
    primes = [True] * limit

    # Set the first two indices to False since 0 and 1 are not prime
    primes[0] = primes[1] = False

    # Iterate over numbers up to the square root of the limit (rounded up to the nearest integer)
    for number in range(2, int(limit**0.5) + 1):
        # If the current number is prime
        if primes[number]:
            # Set all multiples of the current number (starting from number*number) to False, since they are not prime
            primes[number*number:limit:number] = [False] * len(primes[number*number:limit:number])

    # Return a list of all indices where the value is True (i.e. the prime numbers)
    return [i for i, is_prime in enumerate(primes) if is_prime]


def print_primes(prime_numbers, limit):
    """
    This function prints the prime numbers.
    :param: prime_numbers: list: A list of prime numbers within the specified range
    """
    # display greeting and explanation
    hello_from_sieve()

    # create a string to display as the preface for the prime numbers
    console_output = f"The prime numbers that exist between 1 and {limit} are:"
    print(console_output)

    # Print the prime numbers
    for prime_number in prime_numbers:
        print(prime_number)


# Main program
if __name__ == "__main__":
    # Get the start and end range of the range of numbers to be checked
    end_num = get_limit()

    # Get a list of all the prime numbers within the specified range
    prime_nums = get_prime_numbers(limit=end_num)

    # Print the prime numbers
    print_primes(prime_numbers=prime_nums, limit=end_num)
