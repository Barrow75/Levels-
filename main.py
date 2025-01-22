
def Fahrenheit_to_Celsius(fahrenheit):

    celsius = (fahrenheit - 32) * 5/9
    return celsius

def Celsius_to_Fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def Celsius_to_Kelvin(celsius):
    kelvin = celsius + 273.15
    return kelvin

def Kelvin_to_Celsius(kelvin):
    celsius = kelvin - 273.15
    return celsius

def main():
    print("What conversion would you like to do?")
    choice = ("Chose a choice "
              "1. Fahrenheit to Celsius, \n"
              "2. Celsius to Fahrenheit, \n"
              "3. Celsius to Kelvin, \n"
              "4. Kelvin to Celsius \n")
    print(choice)
    while True:
        try:
            user_choose = int(input("Choose an Option: "))
            if user_choose < 1 or user_choose > 4:
                print("Invalid Choice; Choose (1-4)")

            elif user_choose == 1:
                print(f"You are converting Fahrenheit to Celsius")
                temperature = float(input("Convert: "))
                conversion = Fahrenheit_to_Celsius(temperature)
                print(f"{temperature}°F is {conversion}°C")

            elif user_choose == 2:
                print(f"You are converting Celsius to Fahrenheit")
                temperature = float(input("Convert: "))
                conversion = Celsius_to_Fahrenheit(temperature)
                print(f"{temperature}°C is {conversion}°F")

            elif user_choose == 3:
                print(f"You are converting Celsius to Kelvin")
                temperature = float(input("Convert: "))
                conversion = Celsius_to_Kelvin(temperature)
                print(f"{temperature}°C is {conversion}°K")

            elif user_choose == 4:
                print(f"You are converting Kelvin to Celsius")
                temperature = float(input("Convert: "))
                conversion = Kelvin_to_Celsius(temperature)
                print(f"{temperature}°K is {conversion}°C")


            break

        except ValueError:
            print("Not a valid option or temperature")


main()