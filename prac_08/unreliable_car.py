from prac_08.car import Car
import random


class UnreliableCar(Car):

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliablity = reliability

    def drive(self, distance):
        if random.randint(0, 101) < self.reliablity:
            super().drive(distance)
        return distance
