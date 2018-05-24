MENU = """C – Convert Celsius to Fahrenheit
F – Convert Fahrenheit to Celsius
Q – Quit"""
print(MENU)
choice = input(">>> ").upper()


def get_fahrenheit(celsius):
    return celsius * 9.0 / 5 + 32


def get_celsius(fahrenheit):
    return 5 / 9 * (fahrenheit - 32)


while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        print("Result: {:.2f} C".format(get_fahrenheit(celsius)))
    elif choice == "F":
        fahrenheit = float(input("Fahrenheit: "))
        print("Result: {:.2f} C".format(get_celsius(fahrenheit)))
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")
