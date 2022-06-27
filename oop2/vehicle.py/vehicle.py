class Vehicle:
    def __init__(self,name,wheels,max_speed,vin) -> None:
        #public attribute
        self.name = name
        self.wheels = wheels
        #protected attribute
        self._max_speed = max_speed
        #private attribute
        self.__vin = vin

    def set_vin(self,vin):
        self.__vin = vin
        
    def v_detail(self):
        print('=========================')
        print(f'Name: {self.name}')
        print('=========================')
        print(f'Wheels: {self.wheels}')
        print(f'Max speed: {self._max_speed}')
        print(f'Vin: {self.__vin}')