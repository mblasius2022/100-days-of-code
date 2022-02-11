"""7. Create a calculator function
Write a Python function that accepts three parameters. The first parameter
is an integer. The second is one of the following mathematical operators:
+, -, /, or . The third parameter will also be an integer.

The function should perform a calculation and return the results. For example,
if the function is passed 6 and 4, it should return 24.
"""
def subtract(n1, n2):
    """ subtract numbers"""
    return n1-n2

def addition(n1, n2):
    """ add numbers """
    return n1+n2

def multiply(n1, n2):
    """ multiply numbers"""
    return n1*n2

def division(n1, n2):
    """divide numbers"""
    return n1/n2

def modulus(n1,n2):
    """returns the remainder from division"""
    return n1%n2

def exponential(n1,n2):
    """ raises n1 to the power of n2"""
    return n1**n2


def get_input():
    """ gets the users input"""
    n1 = float(input("Enter the first number: "))
    n2 = float(input("Enter the second number: "))
    print("Operators")
    print("/ = division")
    print("* = multiplication")
    print("+ = addition ")
    print("- = subtraction")
    print("** = exponential")
    print("% = residual")
    operator = input("Enter operator: ")

    if operator == '*':
       result = multiply(n1, n2)
    elif operator == '/':
        result = division(n1, n2)
    elif operator == '+':
        result = addition(n1, n2)
    elif operator == '-':
        result = subtract(n1, n2)
    elif operator == '%':
        result = modulus(n1, n2)
    elif operator == "**":
        result = exponential(n1,n2)


    print(f"The result of {n1}{operator}{n2} is {result}")

    repeat = input("Another Calculation y or n: ")
    if repeat == 'y':
        get_input()
    else:
        print("next time")

get_input()