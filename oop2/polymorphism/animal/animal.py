class Animal:
    def __init__(self,name,age) -> None:
        self.__name = name
        self.__age = age

    #มีข้อมูลprivate ต้องสร้าง
    @property   #getterของname
    def name(self):
        return self.__name
    @name.setter   #setterของname
    def name(self,value):
        self.__name = value 

    @property   #getterของage
    def age(self):
        return self.__age
    @age.setter #setterของage
    def age(self,value):
        self.__age = value

    def info(self):
        print('----- Animal Information ------')

    def make_sound(self):
        print('=== Animal Sound ===')