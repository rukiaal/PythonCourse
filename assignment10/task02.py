class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class ElectricCar(Car):
    def __init__(self, registration_number, maximum_speed, battery_capacity):
        super().__init__(registration_number, maximum_speed)
        self.battery_capacity = battery_capacity


class GasolineCar(Car):
    def __init__(self, registration_number, maximum_speed, tank_volume):
        super().__init__(registration_number, maximum_speed)
        self.tank_volume = tank_volume



# MAIN PROGRAM

car = Car("ABC-123", 142)
print("Basic Car Information:")
print(" Registration:", car.registration_number)
print(" Max Speed:", car.maximum_speed)
print(" Current Speed:", car.current_speed)
print(" Travelled Distance:", car.travelled_distance, "km")



electric = ElectricCar("ABC-15", 180, 52.5)
gasoline = GasolineCar("ACD-123", 165, 32.3)

# Set speeds
electric.current_speed = 120
gasoline.current_speed = 140

# Drive both for 3 hours
electric.drive(3)
gasoline.drive(3)

print("Electric Car Distance:", electric.travelled_distance, "km")
print("Gasoline Car Distance:", gasoline.travelled_distance, "km")
