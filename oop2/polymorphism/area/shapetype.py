from shape import Shape
from math import pi  #นำเข้าค่าpi

class Square(Shape):
    def __init__(self,lenght = 0) -> None:
        super().__init__('Square')  #ส่งค่าshapeไปให้classแม่
        self.__lenght = lenght
    
    @property
    def lenght(self):
        return self.__lenght
    @lenght.setter
    def lenght(self,value):
        self.__lenght = value

    #overiding
    def compute_area(self):
        super().compute_area()
        self.area = self.lenght ** 2
        #area มาจากคลาสแม่

    def print_square(self):
        self.compute_area()   #เนื่องจากต้องคำนวนพื้นที่มาก่อน สามารถใช้คำสั่งนี้เรียกใช้แสดงค่าพื้นที่ในนี้ได้เลย โดยการสร้างobj ไม่ต้องเรียกคำสั่ง compute_area แล้ว เรียกแค่ print_square ได้เลย ก็จะแสดงค่าที่คำนวนพื้นที่มาด้วยเลย
        print(f'{self.shape} area = {self.area:,.2f}')
        #shape มาจากคลาสแม่

class Circle(Shape):
    def __init__(self,radius = 0) -> None:
        super().__init__('Circle')
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    @radius.setter
    def radius(self,value):
        self.__radius = value

    def compute_area(self):
        super().compute_area()
        self.area = pi * (self.radius ** 2)
    
    def print_circle(self):
        self.compute_area()
        print(f'{self.shape} area = {self.area:,.2f}')

class Triangle(Shape):
    def __init__(self,base=0,high=0) -> None:
        super().__init__('Triangle')
        self.__base = base
        self.__high = high

    @property
    def base(self):
        return self.__base
    @base.setter
    def base(self,value):
        self.__base = value

    @property
    def high(self):
        return self.__high
    @high.setter
    def high(self,value):
        self.__high = value
    
    def compute_area(self):
        super().compute_area()
        self.area = 0.5 * self.base * self.high

    def print_triangle(self):
        self.compute_area()
        print(f'{self.shape} area = {self.area:,.2f}')