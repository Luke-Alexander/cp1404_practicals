def main():
    name = get_name()
    frequency = int(input("Frequency of letters: "))
    return change_name(frequency, name)


def change_name(frequency, name):
    new_name = ""
    for letter in range(0, len(name), frequency):
        new_name += name[letter]
    return new_name


def get_name():
    name = input("What is your name: ")
    while name == "":
        name = str(input("Please enter a valid name: "))
    return name


print(main())
