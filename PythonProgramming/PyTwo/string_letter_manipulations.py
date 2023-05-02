# this python script does string manipulations to the classic "hello world" string based on the letter "o"


def print_char_index_position(string, character):
    """
    Prints the index position of a character in a given string.

    :param string: A string.
    :param character: A character to search for in the string.
    :return: None.
    """

    index_position_msg = f"The index position of the letter, '{character}', is: "

    # Iterate over the indices of the string
    for index in range(len(string)):
        # Check if the character at the current index is the one we are looking for
        if string[index] == character:
            # Print the index position message followed by the current index
            print(index_position_msg + str(index))


def get_string_before_char(string, character):
    """
    Returns the substring of the input string before the first occurrence of a given character.

    :param string: A string.
    :param character: A character to search for in the string.
    :return: A string containing the substring before the first occurrence of the character.
    """

    string_before_char_msg = f"The string before the letter, '{character}', is: "

    partial_string = ""
    # Iterate over the indices of the string
    for index in range(len(string)):
        # Check if the character at the current index is the one we are looking for
        if string[index] == character:
            # Stop iterating if we find the first occurrence of the character
            break
        # Append the current character to the partial string
        partial_string += string[index]

    return string_before_char_msg + partial_string


def get_string_after_char(string, character):
    """
    Returns the substring of the input string after the last occurrence of a given character.

    :param string: A string.
    :param character: A character to search for in the string.
    :return: A string containing the substring after the last occurrence of the character.
    """

    string_after_char_msg = f"The string after the letter, '{character}', is: "

    partial_string = ""
    # Iterate over the indices of the string in reverse order
    for index in range(len(string) - 1, -1, -1):
        # Check if the character at the current index is the one we are looking for
        if string[index] == character:
            # Stop iterating if we find the last occurrence of the character
            break
        # Append the current character to the partial string
        partial_string += string[index]

    # Reverse the partial string to get the correct order of characters
    normalized_string = partial_string[::-1]

    return string_after_char_msg + normalized_string


def get_string_without_char(string, character):
    """
    Returns the input string with all occurrences of a given character removed.

    :param string: A string.
    :param character: A character to remove from the string.
    :return: A string containing the input string with all occurrences of the character removed.
    """

    modified_string_msg = f"The string without the letter, '{character}', is: "

    modified_string = ""
    # Iterate over the characters in the string
    for letter in string:
        # Check if the current character is not the one we are looking for
        if letter != character:
            # Append the current character to the modified string
            modified_string += letter

    return modified_string_msg + modified_string


# Main program
my_string = "hello world"
char = "o"

# Get the index position of each occurrence of the character
print_char_index_position(my_string, char)
print()

# Get the string before the first occurrence of the character
string_before_char = get_string_before_char(my_string, char)
print(string_before_char)

# Get the string after the last occurrence of the character
string_after_char = get_string_after_char(my_string, char)
print(string_after_char)

# Get the string with all occurrences of the character removed
string_without_char = get_string_without_char(my_string, char)
print(string_without_char)
