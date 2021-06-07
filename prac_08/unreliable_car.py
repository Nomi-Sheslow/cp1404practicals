from prac_08.car import Car
import random


class UnreliableCar(Car):
    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def __str__(self):
        return "{}, {}km driven.".format(super().__str__(), self.odometer)

    def drive(self, distance):
        """Drive like parent Car but calculate fare distance as well."""
        distance_driven = 0
        drive_value = random.randint(0, 100)
        if drive_value < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
