# will try to do every single code with documentation

# Write a Python program that simulates rolling a six-sided dice multiple times. The program should:
#
# Roll the dice a user-specified number of times.
# Store the results in a list.
# Display the frequency of each number (1 through 6) in the rolls.

# blueprint - it is a random dice roll - random module
#           - user inputs for how many times the dice is rolled
#           - display it


import random


print("Eneter a number to roll the dice that many times")
user_roll = int(input("Roll the die: "))

stored_rolls = []

for roll_number in range(user_roll):
    dice_roll = random.randint(1, 6)
    stored_rolls.append(dice_roll)

print(stored_rolls)



