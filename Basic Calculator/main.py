__author__ = "Ritik Sharma"
__email__ = "sharmaritik351@gmail.com"

print("Welcome to Basic Calculator!")
print("It calculated the arithmetic result of two numbers!")
print("Following operators are accepted: (+, -, *, /, //, %, **)")

operator: str = input("Enter the operation you want to perform : ")
number1: float = int(input("Enter the first number: "))
number2: float = float(input("Enter the second number: "))

def calculator(first_number: float, second_number: float, operator_type: str):
    if operator_type == "+":
        return first_number + second_number

    elif operator_type == "-":
        return first_number - second_number

    elif operator_type == "*":
        return first_number * second_number

    elif operator_type == "/":
        return first_number / second_number

    elif operator_type == "//":
        return first_number // second_number

    elif operator_type == "**":
        return first_number ** second_number

    elif operator_type == "%":
        return first_number % second_number

    else:
        raise ValueError("Enter a valid operator")

result = calculator(first_number=number1, second_number=number2, operator_type=operator)
print("Result = ", result)
