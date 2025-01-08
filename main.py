# Day 4: Prompt
# Write a Python program that acts as a simple calculator. The program should:
#
# Ask the user for two numbers.
# Ask the user which operation they want to perform: addition, subtraction, multiplication, or division.
# Perform the selected operation and display the result.
# Include error handling:
# Prevent crashes if the user enters invalid input.
# Handle division by zero gracefully.
# Allow the user to perform another calculation or exit the program.




while True:

    while True:
        try:
            num1 = int(input("Enter a number: "))
            print("Valid Input")

            break
        except ValueError:
            print("This is not a number")

    while True:
            try:
                operations = input("Choose Operatrion +, -, /, *: ")
                if operations in ['+', '-', '*', '/']:
                    print("Valid Input")
                    break

            except ValueError:
                print("This is not a number")
    while True:
            try:
                num2 = int(input("Enter another number: "))
                print("Valid Input")
                break

            except ValueError:
                print("This is not a number")

    #break

    if operations == '+':
        print(num1 + num2)

    elif operations == '-':
        print(num1 - num2)

    elif operations == '*':
        print(num1 * num2)

    elif operations == '/':
        print(num1 / num2)

    print("Would you like to do another calculation? ")
    user = input("Yes or No?: ").lower()

    if user != 'yes':
        break


