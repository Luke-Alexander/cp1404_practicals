from prac_08.taxi import Taxi
from prac_08.silver_service_taxi import SilverServiceTaxi

print("Let's drive!")
menu_hold = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2),
         SilverServiceTaxi("Hummer", 200, 4)]
bill = 0


while menu_hold != "q":
    if menu_hold == "c":
        taxi_choice = int(input("0 - {}\n1 - {}\n2 - {}\nChoose taxi:".format(taxis[0], taxis[1], taxis[2])))
    elif menu_hold == "d":
        distance = int(input("Drive how far:"))
        taxis[taxi_choice].start_fare()
        taxis[taxi_choice].drive(distance)
        ride_cost = taxis[taxi_choice].get_fare()
        print("Your {} trip cost you ${:.2f}".format(taxis[taxi_choice].name, ride_cost))
        bill += ride_cost
        print("Bill to date: ${:.2f}".format(bill))
    else:
        print("Invalid input; enter a valid key")
    menu_hold = input("q)uit, c)hoose taxi, d)rive\n>>>").lower()
