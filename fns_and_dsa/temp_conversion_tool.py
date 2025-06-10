FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

    return fahrenheit

try:
    temperature = int(input("Enter the temperature to convert: "))
    units = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").lower()

    if units == "f":
        print(f"{temperature} is {convert_to_fahrenheit(temperature)}F")
    elif units == "c":
        print(f"{temperature} is {convert_to_celsius(temperature)}C")
    else:
        print("Invalid input. Please enter 'C' or 'F'.")
except ValueError:
    print("Invalid temperature. Please enter a numeric value.")