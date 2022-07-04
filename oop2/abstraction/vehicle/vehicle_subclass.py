import imp
from vehicle_abstract import Vehicle

class Car(Vehicle):
    def __init__(self, brand, speed) -> None:
        #super().__init__(brand, speed)
        Vehicle.__init__(self,brand,speed) #เรียกผ่านชื่อclass ต้องใส่selfและพารามิเตอร์ทั้งหมด
        self.__year = 0 
        self.__maintanance = 0

    @property
    def year(self):
        return self.__year
    @year.setter
    def year(self,value):
        self.__year = value
    @property
    def maintanance(self):
        return self.__maintanance
    @maintanance.setter
    def mantanace(self,value):
        self.__maintanance = value

    #implement abstract method
    def show_detail(self):
        super().show_detail()
        print('==== Car Detail ====')
        print(f'{self.brand} with speed {self.speed} km/hr')
        print(f'manufactered in {self.year} has')
        print(f'{self.gear} gear and {self.seat} seats')

    #implement car method
    def show_maintanance(self):
        print('-- Car Maintanance --')
        print(f'The lastest maintance in {self.maintanance}')


class Truck(Vehicle):
    pass

class Motocycle(Vehicle):
    pass