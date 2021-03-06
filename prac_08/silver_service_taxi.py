from prac_08.taxi import Taxi


class SilverServiceTaxi(Taxi):
    FLAGFALL = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel)
        self.price_per_km *= fanciness

    def __str__(self):
        return "{}, fuel={}, odo={}, {}km on current fare, ${:.2f}/km plus flagfall of ${:.2f}".format(
            super().__str__(), self.fuel, self.odometer,
            self.current_fare_distance,
            self.price_per_km, self.FLAGFALL)

    def get_fare(self):
        return self.price_per_km * self.current_fare_distance + self.FLAGFALL
