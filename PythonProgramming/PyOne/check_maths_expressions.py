# This python script receives an equation and evaluates if it is correct
import re
import numexpr as ne


def get_equation():
    # initialize message variables
    invalid_equation = "ERROR: Not a valid equation."
    invalid_input = "ERROR: Invalid input."
    instruction = \
        "INFO: Equations should include two numbers connected by an operator, an equal sign and a resulting number."

    # initialize variable for pattern of operators
    operator_pattern = r'^\s*\d+(\.\d+)?\s*[+\-*/%]{1,2}\s*\d+(\.\d+)?\s*=\s*\d+(\.\d+)?\s*$'

    while True:
        try:
            equation = input("Enter your equation: ")

            # check if the input string matches the expected format
            if re.match(operator_pattern, equation):
                return equation.strip()

            else:
                print(invalid_equation + "\n" + instruction + "\n")

        except ValueError:
            print(invalid_input + "\n" + instruction + "\n")


def split_equation(equation):
    # check which side has only numbers and operators
    operators = ["+", "-", "*", "/", "//", "%", "**"]

    # remove all whitespace characters from the equation
    equation = ''.join(equation.split())

    # split the equation into left and right sides
    left_side, right_side = equation.split("=")

    if all(character.isdigit() or character in operators for character in left_side):
        expression = left_side
        supposed_result = right_side
        return expression, supposed_result

    elif all(character.isdigit() or character in operators for character in right_side):
        expression = right_side
        supposed_result = left_side
        return expression, supposed_result


def evaluate_equation(expression, supposed_result):
    try:
        # evaluate the expression using numexpr
        actual_result = ne.evaluate(expression)

        # check if the actual and supposed results match
        if float(supposed_result) == actual_result:
            return True
        else:
            return False

    except ZeroDivisionError:
        print("ERROR: Division by zero.")
        return False

    except (ValueError, TypeError):
        print("ERROR: Invalid equation format.")
        return False


# get the equation from the user
my_equation = get_equation()

# split the equation into expression and supposed result
my_expression, my_supposed_result = split_equation(my_equation)

# evaluate the expression and compare to supposed result
result = evaluate_equation(my_expression, my_supposed_result)
print(result)
