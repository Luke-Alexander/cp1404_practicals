from prac_08.silver_service_taxi import SilverServiceTaxi


prius = SilverServiceTaxi("Hummer", 100, 2)
prius.drive(18)
print("Current fare is $", prius.get_fare())
print(prius)

prius.start_fare()
prius.drive(100)
print("Current fare is $", prius.get_fare())
print(prius)

car = SilverServiceTaxi("car",100,3)
print(car.price_per_km, car.FLAGFALL)