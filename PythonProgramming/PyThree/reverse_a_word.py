# this python program reverses a single word input from the user.


def get_word():
    """
    Get the word from the user.
    :return: word
    """
    # Initialize variables to hold Error Messages
    number_input_err_msg = "ERROR | Invalid input. Please enter a word, not a number."
    empty_space_err_msg = "ERROR | Invalid input. Please enter a word, not an empty space."
    one_char_err_msg = "ERROR | Invalid input. Please enter a word with more than one character."
    sentence_err_msg = "ERROR | Invalid input. Please enter a single word, not multiple words."
    palindrome_err_msg = "ERROR | Invalid input. Please enter a word that is a palindrome."

    # Run the loop until the user enters a valid input
    while True:
        # try to get the word from the user
        try:
            word = input("Enter a word: ")

            # check if the word is:
            # a number, an empty space, one character, a sentence or a palindrome (written the same way backwards)

            if word.isnumeric():
                raise ValueError(number_input_err_msg)

            elif len(word) == 0:
                raise ValueError(empty_space_err_msg)

            elif len(word) == 1:
                raise ValueError(one_char_err_msg)

            elif len(word.split()) > 1:
                raise ValueError(sentence_err_msg)

            elif word[::-1] == word:
                raise ValueError(palindrome_err_msg)

            return word.lower()

        # if the user enters a value that is not a single word, an error message of the specific mistake is displayed
        except ValueError as e:
            print(e)


def reverse_word(word):
    """
    Reverse the word.
    :param word: word
    :return: reversed_word
    """
    # message to be displayed on the console
    console_message = "Your word in reverse comes out as: "

    # pythonic way to reverse a string
    reversed_word = word[::-1]

    # return the console message concatenated with the reversed word
    return console_message + reversed_word


# Main program
# call the function to reverse the word and use the function get_word() as the parameter
my_word_reversed = reverse_word(word=get_word())
print(my_word_reversed)
