class Elevator:
    def __init__(self, floor_range):
        self.floor_range = floor_range      # ASSOCIATION
        self.current_floor = floor_range.bottom

    def floor_up(self):
        if self.current_floor < self.floor_range.top:
            self.current_floor += 1
            print("Elevator is now at floor", self.current_floor)

    def floor_down(self):
        if self.current_floor > self.floor_range.bottom:
            self.current_floor -= 1
            print("Elevator is now at floor", self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()

