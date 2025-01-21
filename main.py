print("Calculator")

def add(a, b):
    return  a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if  b == 0:
        raise ZeroDivisionError("Cannot divide by 0")

    return a/b

while True:



    while True:
        try:
            number = float(input("Eneter a number: "))
            break
        except ValueError:
            print("Not a number")

    while True:
        try:
            operation = input("Enter an Operation: ")
            if operation in ['+', '-', '*', '/']:
                break
        except ValueError:
            print("Not valid operation")

    while True:
        try:
            number2 = float(input("Eneter another number: "))
            break
        except ValueError:
            print("Not a number")

    if operation == '+':
        result = add(number, number2)
        print(result)

    elif operation == '-':
        result = subtract(number, number2)
        print(result)

    elif operation == '*':
        result = multiply(number, number2)
        print(result)

    elif operation == '/':
        result = divide(number, number2)
        print(result)

    print("Would you like to do another calculation? ")
    user = input("Yes or No?: ").lower()

    if user != 'yes':
        break
