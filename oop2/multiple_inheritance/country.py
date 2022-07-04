from geographic import Geographic
from temperature import Temperature

class Conutry(Geographic,Temperature): #multiple inheritance
    """ def __init__(self,name,area,population) -> None:
        self.name = name
        self.area = area
        self.population = population"""
    
    def __init__(self,name,area,population) -> None:
        #super().__init__() #ระบุชื่อคลาสแม่ กรณ๊ชื่อตัวแปรซ้ำกัน ไม่ต้องมีself
        Geographic.__init__(self) #เรียกใช้จากชื่อคลาสแม่ ต้องมีself
        Temperature.__init__(self)
        self.name = name
        self.area = area
        self.population = population

    def getpopulationdensity(self):
        return self.population / self.area

    def showdetails(self):
        print(f'Country: {self.name}') #ประเทศ
        #สถานที่ตั้ง latitude และ longitude
        print(f'Location: {self.getcordinate()}') #เรียกฟังก์ชันจากclass อื่นที่คำนวนไว้แล้ว ต้องใส่เครื่องหมาย() ด้วย
        
        #แสดงขนาดพื้นที่,จำนวนประชากร,และความหนาแน่นของประชากร
        print(f'Population: {self.population:,d}')  #:,d => ใส่คอมม่าในหลักพันขึ้นไป
        print(f'Area: {self.area:,.2f}')
        print(f'Density: {self.getpopulationdensity():,.2f}')
        
        #แสดงtimezone, climate , temperature , weather
        print(f'Timezone: {self.gettimeZone()}')
        print(f'Climate: {self.getclimate()}')
        print(f'Temperture(C): {self.getcelsius():,.2f}')
        print(f'Temperture(F): {self.getfahrenheit():,.2f}')
        print(f'Weather: {self.getweather()}')

        print('*********************************')