# this python script will transform each word in a list of strings to all caps and print them separately

def get_string_list_all_caps(strings_list):
    """
    Capitalizes each word in a list of strings and returns them separately.

    :param strings_list: A list of strings/words.
    :return: A list of capitalized words.
    """
    all_caps_strings_list = []  # Initialize a list to store the capitalized words

    for string in strings_list:  # Iterate over each string in the list
        split_strings = string.split()  # Split the string into a list of words

        for word in split_strings:  # Iterate over each word in the list
            all_caps_strings_list.append(word.upper())  # Add the capitalized word to the list

    return all_caps_strings_list  # Return the list of capitalized words


def print_words(strings_list):
    """
    Prints each word in a list of strings.

    :param strings_list: A list of strings/words.
    :return: None.
    """

    for string in strings_list:  # Loop over each string in the list
        print(string)  # Print the string


# Initialize a list of strings to be capitalized
my_strings = ["hello world", "this is a sentence", "another EXAMPLE"]

# Call the function to capitalize each word in the list of strings
words_all_caps = get_string_list_all_caps(my_strings)

# Call the function to print each word in the list of capitalized words
print_words(words_all_caps)
