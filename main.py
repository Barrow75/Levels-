# Day 5: Prompt
# Write a Python program that:
#
# Asks the user to input grades for multiple subjects.
# Calculates the average grade.
# Determines the corresponding letter grade based on the average:
# A for 90–100
# B for 80–89
# C for 70–79
# D for 60–69
# F for below 60
# Displays the grades entered, the average grade, and the letter grade.
# Handles invalid inputs gracefully (e.g., non-numeric grades)


grades = []
while True:
    print("Enter the grade for math")

    while True:
        try:
            math_input = int(input("Math: "))
            if 90 <= math_input <= 100:
                print("Math is A")
            elif 80 <= math_input <= 89:
                print("Math is B")
            elif 70 <= math_input <= 79:
                print("Math is C")
            elif 60 <= math_input <= 69:
                print("Math is D")
            elif math_input <= 59:
                print("Math F")
                grades.append(math_input)
            break
        except ValueError:
            print("Not a valid input")

    print("Enter the grade for Science")

    while True:
        try:
            science_input = int(input("Science: "))
            if 90 <= science_input <= 100:
                print("Science is A")
            elif 80 <= science_input <= 89:
                print("Science is B")
            elif 70 <= science_input <= 79:
                print("Science is C")
            elif 60 <= science_input <= 69:
                print("Science is D")
            elif science_input <= 59:
                print("Science F")
                grades.append(science_input)
            break
        except ValueError:
            print("Not a valid input")

    print("Enter the grade for History")

    while True:
        try:
            history_input = int(input("History: "))
            if 90 <= history_input <= 100:
                print("Science is A")
            elif 80 <= history_input <= 89:
                print("Science is B")
            elif 70 <= history_input <= 79:
                print("Science is C")
            elif 60 <= history_input <= 69:
                print("Science is D")
            elif history_input <= 59:
                print("Science F")
                grades.append(history_input)
            break
        except ValueError:
            print("Not a valid input")

    print("Enter the grade for Other Subject")

    while True:
        try:
            other_input = int(input("Other Subject: "))
            if 90 <= other_input <= 100:
                print("Other is A")
            elif 80 <= other_input <= 89:
                print("Other is B")
            elif 70 <= other_input <= 79:
                print("Other is C")
            elif 60 <= other_input <= 69:
                print("Other is D")
            elif other_input <= 59:
                print("Other F")
                grades.append(other_input)
            break
        except ValueError:
            print("Not a valid input")
    print("Grades entered:", grades)

    total = sum(grades)
    length = len(grades)
    print("Average Grade:", total/length)

    break

