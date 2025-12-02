def celsius_to_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(f):
    celsius = (f - 32) / 1.8
    return celsius

selection = input('Select "C" or "F": ')
thermometer = float(input("Write down your numbers: "))

if selection == "C":
    print(f"Transfer from C° to F° is: {celsius_to_fahrenheit(thermometer)}°")
elif selection == "F":
    print(f"Transfer from F° to C° is: {fahrenheit_to_celsius(thermometer)}°")
else:
    print("You used the wrong letters!")