# this python script receives a mathematical expression as input and evaluates if it is correct


user_formula = input("Enter your expression: ")

user_formula_split = user_formula.split("=")

expression = user_formula_split[0].strip()

supposed_result = user_formula_split[1].strip()

actual_result = eval(expression)

if supposed_result == str(actual_result):
    print("Correct")

else:
    print("Incorrect")



