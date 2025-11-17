from Elevator3 import Elevator

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        for _ in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, destination):
        elevator = self.elevators[number]   # choose elevator
        elevator.go_to_floor(destination)   # move it to target floor

    def fire_alarm(self):
        print("*** FIRE ALARM! Moving all elevators to bottom floor ***")
        for elevator in self.elevators:
            elevator.go_to_floor(self.bottom)

