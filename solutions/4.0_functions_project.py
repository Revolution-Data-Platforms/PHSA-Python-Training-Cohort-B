def fahrenheit_to_celsius(temp):
    return (temp - 32) * 5/9

def celsius_to_fahrenheit(temp):
    return (temp * 9/5) + 32

print("Temperature Converter\n")

while True:
    print("Choose an option:")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")

    choice = input("\nEnter your choice (1/2): ")

    if choice in ('1', '2'):
        temp = float(input("Enter temperature: "))

        if choice == '1':
            result = fahrenheit_to_celsius(temp)
            print(temp, "°F is", result, "°C.")

        elif choice == '2':
            result = celsius_to_fahrenheit(temp)
            print(temp, "°C is", result, "°F.")

    else:
        print("Invalid input.")
