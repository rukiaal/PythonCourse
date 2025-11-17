class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom     # elevator starts at bottom floor

    def floor_up(self):
        self.current_floor += 1
        print("Elevator is now at floor", self.current_floor)

    def floor_down(self):
        self.current_floor -= 1
        print("Elevator is now at floor", self.current_floor)

    def go_to_floor(self, target):
        while self.current_floor < target:
            self.floor_up()
        while self.current_floor > target:
            self.floor_down()
