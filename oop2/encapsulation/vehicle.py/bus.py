from vehicle import Vehicle
class Bus(Vehicle):
    def __init__(self, name, wheels, max_speed, vin) -> None:
        super().__init__(name, wheels, max_speed, vin)

    def set_color(self,color):
        self.color = color

    def set_capacity(self,capacity):
        self.capacity = capacity

    def bus_detail(self):
        self.v_detail()
        print(f'Color: {self.color}')
        print(f'Capacity: {self.capacity}')