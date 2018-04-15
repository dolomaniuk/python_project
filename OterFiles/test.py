class Car:
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

class ElecticCar(Car):
    def __init__(self, number_of_wheels, seating_capacity, maximum_velocity):
        Car.__init__(self, number_of_wheels, seating_capacity, maximum_velocity)

elFord = ElecticCar(4, 6, 260)
print(elFord.number_of_wheels)
print(elFord.seating_capacity)
print(elFord.maximum_velocity)