# Day 3: Prompt
# Write a Python program that takes a list of numbers from the user (separated by spaces), calculates the sum and average of the numbers, and prints them out.

print("Enter numbers that you want to add together, space them out")

user = list(map(int,input("The numbers are: ").split()))

print(user)

add = sum(user)
print("The sum off all the nubers is: ", add)
