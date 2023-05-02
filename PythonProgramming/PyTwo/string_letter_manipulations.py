# this python script does string manipulations to the classic "hello world" string based on the letter "o"


def print_char_index_position(string, character):
    index_position_msg = f"The index position of the letter, '{character}', is: "

    for index in range(len(string)):
        if string[index] == character:
            print(index_position_msg + str(index))


def get_string_before_char(string, character):
    partial_string = ""

    for index in range(len(string)):
        if string[index] == character:
            break

        partial_string += string[index]

    return partial_string


def get_string_after_char(string, character):
    reversed_string = string[::-1]

    partial_string = ""
    for index in range(len(reversed_string)):
        if reversed_string[index] == character:
            break

        partial_string += reversed_string[index]

    normalized_string = partial_string[::-1]

    return normalized_string


def get_string_without_char(string, character):
    modified_string = ""
    for letter in string:
        if letter != character:
            modified_string += letter

    return modified_string


my_string = "hello world"
char = "o"

string_before_char = get_string_before_char(my_string, char)
string_after_char = get_string_after_char(my_string, char)
string_without_char = get_string_without_char(my_string, char)

print_char_index_position(my_string, char)
print(string_before_char)
print(string_after_char)
print(string_without_char)
