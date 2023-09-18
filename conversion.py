def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit- 32)*5/9
    return celsius

def celcius_to_fahrenheit (celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit


temperature = float(input("Enter the temperature: "))
unit = input("Enter the unit (C or F): ")

if unit.upper() == "C":
    converted_temperature = celcius_to_fahrenheit(temperature)
    print(f"{temperature} degrees Celsius is equal to {converted_temperature}  degrees fahrenheit.")

elif unit.upper() == "F":
    converted_temperature = fahrenheit_to_celsius(temperature)
    print(f"{temperature} degrees Fahrenheit is equal to {converted_temperature}  degrees Celsius.")

else:
    print("Invalid unit print either C or F.")


