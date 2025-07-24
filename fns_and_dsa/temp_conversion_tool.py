FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR 
    return celsius

def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

temprature = input("Enter the temperature to convert: ")
type = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")

if type == 'C':
    result = convert_to_fahrenheit()
    print(f"{temprature}C is {result}")
elif type == 'F':
    result = convert_to_celsius()
    print(f"{temprature}F is {result}")
else:
    print("Enter C or F")



