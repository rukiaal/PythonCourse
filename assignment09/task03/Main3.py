from Building3 import Building
my_building = Building(bottom=0, top=10, num_elevators=3)

my_building.run_elevator(0, 5)
my_building.run_elevator(1, 8)
my_building.run_elevator(2, 3)


my_building.fire_alarm()