from FloorRange import FloorRange
from Elevator import Elevator
floors = FloorRange(1, 10)
e = Elevator(floors)
e.go_to_floor(5)
e.go_to_floor(1)