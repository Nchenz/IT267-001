from vehicle import Vehicle
class Motorcycle(Vehicle):
    def __init__(self, name, wheels, max_speed, vin) -> None:
        super().__init__(name, wheels, max_speed, vin)

    def set_cc(self,cc):
        self.cc = cc

    def bike_detail(self):
        self.v_detail()
        print(f'CC: {self.cc}')

    #overiding method
    """ def v_detail(self):
        super().v_detail()
        print(f'CC: {self.cc}')"""