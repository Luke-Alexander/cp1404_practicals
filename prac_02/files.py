
out_file = open("name.txt", "w")
name = input("What is your name? ")
print(name, file=out_file)
out_file.close()

file = open("name.txt", "r")
name = file.read().strip()
print("Your name is", name)
file.close()

file = open("numbers.txt", "r")
number1 = int(file.readline())
number2 = int(file.readline())
print(number1 + number2)
file.close()
