class Shape:
    def __init__(self,shape) -> None:
        self.__shape = shape
        self.__area = 0  #ให้เป็น 0 ก่อนเพราะต้องคำนวน

    #shape property
    @property
    def shape(self):
        return self.__shape
    @shape.setter
    def shape(self,value):
        self.__shape = value
    
    #area property
    @property
    def area(self):
        return self.__area
    @area.setter
    def area(self,value):
        self.__area = value

    def compute_area(self):
        pass