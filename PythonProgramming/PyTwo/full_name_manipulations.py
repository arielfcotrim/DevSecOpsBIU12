def get_full_name():
    """
    Prompts the user to input their full name and returns it as a string.

    :return: A string representing a full name.
    """

    return input("Enter your full name: ")


def print_last_five_chars(full_name):
    """
    Prints the last five characters of a string.

    :param full_name: A string representing a full name.
    """

    print(full_name[-5:])


def print_first_third(full_name):
    """
    Prints the first third of a string.

    :param full_name: A string representing a full name.
    """

    third = len(full_name) // 3

    print(full_name[:third])


def count_letter_a(full_name):
    """
    Counts the number of times the letter 'a' appears in a string.

    :param full_name: A string representing a full name.
    :return: The count of letter 'a' occurrences.
    """
    a = 'a'
    full_name = full_name.upper()

    return full_name.count(a.upper())


def check_for_letter_b(full_name):
    """
    Checks if the letter 'b' appears in a string.

    :param full_name: A string representing a full name.
    :return: True if the letter 'b' is present, False otherwise.
    """

    return 'b' in full_name


def create_name_list(full_name):
    """
    Creates a list containing the first name and surname from a full name string.

    :param full_name: A string representing a full name.
    :return: A list containing the first name and surname.
    """

    name_list = full_name.split()
    return name_list


def invert_name_list(name_list):
    """
    Inverts the order of items in a list.

    :param name_list: A list containing the first name and surname.
    :return: The inverted list.
    """

    return name_list[::-1]


def set_index_to_all_caps(name_list, index):
    """
    Makes the surname in a list of name all capital letters.

    :param index:
    :param name_list: A list containing the first name and surname.
    :return: The modified list.
    """

    name_list[index] = name_list[index].upper()
    return name_list


def remove_middle_char(first_name):
    """
    Removes the middle character from a string.

    :param first_name: A string representing a first name.
    :return: The modified string.
    """

    length = len(first_name)

    if length % 2 == 0:
        middle = length // 2 - 1

    else:
        middle = length // 2

    first_name = first_name[:middle] + first_name[middle + 1:]

    return first_name


def get_modified_full_name(name_list):
    first_name = remove_middle_char(name_list[0])

    modified_name_list = set_index_to_all_caps(name_list, 1)
    last_name = modified_name_list[1]

    full_name = first_name + ' ' + last_name

    return full_name


def name_manipulations(full_name):
    """
    Modifies a full name string based on a series of transformations.

    :param full_name: A string representing a full name.
    :return: The modified full name string.
    """
    # Print first five characters
    print_last_five_chars(full_name)

    # Print first third of name
    print_first_third(full_name)

    # Count letter 'a'
    a_count = count_letter_a(full_name)
    print(f"Letter 'a' appears {a_count} times")

    # Check for letter 'b'
    b_check = check_for_letter_b(full_name)
    print(f"Letter 'b' {'is' if b_check else 'is not'} present")

    # Create name list
    name_list = create_name_list(full_name)
    print(name_list)

    # Invert name list
    inverted_name_list = invert_name_list(name_list)
    print(inverted_name_list)

    # Make surname caps
    modified_inverted_name_list = set_index_to_all_caps(inverted_name_list, 0)  # fix required here
    print(modified_inverted_name_list)

    # Remove middle character from first name
    first_name = remove_middle_char(name_list[0])
    print(first_name)

    full_name = get_modified_full_name(name_list)
    print(full_name)


name_manipulations(get_full_name())
