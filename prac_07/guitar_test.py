from prac_07.guitar import Guitar
guitars = []
print("My guitars!")
name = input("Name: ")
while name != "":
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    guitar = Guitar(name, year, cost)
    guitars.append(guitar)
    name = input("Name: ")

print("These are my guitars")
for guitar in guitars:
    print(guitar)