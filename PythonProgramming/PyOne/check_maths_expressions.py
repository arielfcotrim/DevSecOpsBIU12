# This python script receives an equation and evaluates if it is correct
import re
import numexpr as ne


def get_valid_equation():
    """
    Prompts user to enter an equation and checks if it matches a valid equation pattern.
    Returns the equation if it is valid, otherwise displays an error message and instruction.

    :return: equation.strip()
    """

    # initialize message variables
    invalid_equation = "ERROR: Not a valid equation."
    invalid_input = "ERROR: Invalid input."
    instruction = \
        "INFO: Equations should include two numbers connected by an operator, an equal sign and a resulting number."

    # initialize regular expression pattern to match the equation format
    operator_pattern = r'^\s*\d+(\.\d+)?\s*[+\-*/%]{1,2}\s*\d+(\.\d+)?\s*=\s*\d+(\.\d+)?\s*$'

    while True:
        try:
            # get equation input from user
            equation = input("Enter your equation: ")

            # check if the input string matches the expected format
            if re.match(operator_pattern, equation):
                return equation.strip()

            else:
                # display error message and instruction
                print(invalid_equation + "\n" + instruction + "\n")

        except ValueError:
            # display error message and instruction
            print(invalid_input + "\n" + instruction + "\n")


def split_equation(equation):
    """
    Receives an equation as input and splits it into expression and supposed result.
    Returns a tuple containing the expression and the supposed result.

    :param equation: equation.strip()
    :return: expression, supposed_result
    """

    # Define list of valid operators
    operators = ["+", "-", "*", "/", "//", "%", "**"]

    # Remove all whitespace characters from the equation
    equation = ''.join(equation.split())

    # Split the equation into left and right sides
    left_side, right_side = equation.split("=")

    # Check which side of the equation contains the expression and which contains the supposed result
    if all(character.isdigit() or character in operators for character in left_side):
        # The left side contains the expression
        expression = left_side
        supposed_result = right_side
        return expression, supposed_result

    elif all(character.isdigit() or character in operators for character in right_side):
        # The right side contains the expression
        expression = right_side
        supposed_result = left_side
        return expression, supposed_result


def evaluate_equation(expression, supposed_result):
    """
    Receives an equation expression and its supposed result and uses numexpr to evaluate the expression.
    Compares the actual and supposed results and returns True if they match, False otherwise.

    :param expression, supposed_result
    :return: True or False (boolean)
    """

    # initialize message variables
    zero_division_err_msg = "ERROR: Division by zero."
    invalid_eq_format = "ERROR: Invalid equation format."

    try:
        # evaluate the expression using numexpr
        actual_result = ne.evaluate(expression)

        # check if the actual and supposed results match
        if float(supposed_result) == actual_result:
            return True
        else:
            return False

    except ZeroDivisionError:
        # handle division by zero error
        print(zero_division_err_msg)
        return False

    except (ValueError, TypeError):
        # handle invalid equation format error
        print(invalid_eq_format)
        return False


# get the equation from the user
my_equation = get_valid_equation()

# split the equation into expression and supposed result
my_expression, my_supposed_result = split_equation(my_equation)

# evaluate the expression and compare to supposed result
is_equation_valid = evaluate_equation(my_expression, my_supposed_result)
print(is_equation_valid)
