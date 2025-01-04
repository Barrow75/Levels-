# Beginner 1 minute to code the first one, and then different techniques to achieve same result:
# prompt: Write a Python program that asks the user for their name and prints a personalized greeting.
# Example: What is your name? John,
# Hello, John! Welcome!


# simple string
print("What is your name")
user = input("Enter your name: ")
print(f"Hello, {user}! Welcome!")

print("\n")

# simple function
def welcoming():
    print("What is your name")
    user = input("Enter your name: ")
    print(f"Hello, {user}! Welcome!")
welcoming()

print("\n")

# moderate function
def welcome(name):
    print("What is your name")

    print("Hello",name + "! Welcome!")
welcome("John")

print('\n')

# advanced function
def greeting(name):
    print("What is your name?")
    user = input("Write your name: ")

    return f"Hello {user}"
print(greeting(f"{user}"))
