def separate_pos_neg_numbers(numbers):
    """
    Separates positive and negative numbers from a list
    :param numbers: list of numbers
    :return: positive_numbers, negative_numbers: tuple of positive and negative numbers
    """
    # initialize empty lists for positive and negative numbers
    positive_numbers = []
    negative_numbers = []

    # iterate over each number in the list
    for number in numbers:
        # if the number is non-negative, add it to the positive list
        if number >= 0:
            positive_numbers.append(number)

        # otherwise, add it to the negative list
        else:
            negative_numbers.append(number)

    # return a tuple of the two lists
    return positive_numbers, negative_numbers


def is_list_empty(which_list):
    """
    Checks if a list is empty
    :param which_list: list to check
    :return: None
    """

    # check if the list is empty and return True if it is
    if not which_list:
        return True

    # otherwise, return False
    else:
        return False


def print_list(num_list, list_name):
    """
    Prints a list along with its name
    :param num_list: list to print
    :param list_name: name of the list
    :return: None
    """
    empty_list_message = f"{list_name}: There are no {list_name.lower()} in the original list..."

    if not is_list_empty(which_list=num_list):  # check if the list is empty
        print(f"{list_name}: {num_list}")  # print the list if it is not empty

    else:  # otherwise, print a message saying that the list is empty
        print(empty_list_message)


# Main program
# create a list of numbers
numbers_list = [-23, 4, -6, 23, -9, 21, -3, 45, -8, 14]

# call the function to separate the numbers
positive_nums, negative_nums = separate_pos_neg_numbers(numbers_list)

print_list(num_list=numbers_list, list_name="Original numbers")
print_list(num_list=positive_nums, list_name="Positive numbers")
print_list(num_list=negative_nums, list_name="Negative numbers")
