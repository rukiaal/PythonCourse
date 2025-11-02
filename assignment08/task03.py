class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0


    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


car = Car("ABC-123", 142)

car.travelled_distance = 2000
car.current_speed = 60

car.drive(1.5)

print("Travelled distance:", car.travelled_distance, "km")
