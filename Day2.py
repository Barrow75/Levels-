# Day 2: Beginner 5 minute to code:
# prompt: Write a Python program that asks the user for a number and checks if it is even or odd.

print("Enter a number to see if it is even or odd")

num = int(input("The number is: "))

if num % 2 == 0:
    print(f"{num} is even")

else:
    print(f"{num} is odd")


# with a simple function
def EvenOdd():
    num = int(input("The number is: "))

    if num % 2 == 0:
        print(f"{num} is even")

    else:
        print(f"{num} is odd")
EvenOdd()

def Even_Odd(num):

    if num % 2 == 0:
        return  f""

    else:
        print("Odd")

num = int(input("The number is: "))
result = Even_Odd(num)
print(result)
