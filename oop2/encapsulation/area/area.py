#getter and setter
class Area:
    def __init__(self,base=1,high=1) -> None:
        self.__base = base
        self.__high = high

    #getter base, high ตามจำนวนของตัวแปร 
    @property
    def base(self):
        return self.__base

    @property
    def high(self):
        return self.__high

    #setter base, high
    @base.setter  #จะรับค่า value เข้าไปเซ็ท
    def base(self,value):
        self.__base = value

    @high.setter
    def high(self,value):
        self.__high = value

    #common method
    def compute_area(self):
        return (0.5 * self.base * self.high)  #ไปเรียกใช้property โดยดึงมาจาก getter ไม่ไปดึงจากตัวแปนโดยตรง