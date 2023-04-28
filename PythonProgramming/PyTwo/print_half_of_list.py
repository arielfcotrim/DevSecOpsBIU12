import math


def get_first_half_of_list():
    """
    This function prompts the user to enter a list of numbers separated by commas,
    converts each string in the list to an integer, calculates the midpoint of the
    list (rounded up), and returns the first half of the list (up to the midpoint).

    :return: first_half_of_list (a list containing the first half of the user input list of numbers)
    """

    # Prompt user to enter a list of numbers
    user_list = input("Enter a list of numbers separated by commas: ")

    # Split the user input into a list of strings
    user_list = user_list.split(',')
    # Convert each string in the list to an integer
    user_list = [int(i) for i in user_list]

    # Get the length of the list
    length = len(user_list)
    # Calculate the midpoint of the list (rounded up)
    midpoint = math.ceil(length / 2)
    # Get the first half of the list (up to the midpoint)
    first_half_of_list = user_list[:midpoint]

    # Return the first half of the list
    return first_half_of_list


# Example usage:
print(get_first_half_of_list())  # Prompts user to enter a list of numbers, e.g. "1,2,3,4,5,6"
