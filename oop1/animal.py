class Animal:
    #Class Variable
    animal = 'CAT'

    def new_animal(self,name:str,breed:str,color:str,age:int): #เพิ่มhint ในการใส่ค่า ไม่ได้เป็นการกำหนดdata type
        #Instance Variable
        self.name = name
        self.breed = breed
        self.color = color
        self.age = age

    def print_detail(self):
        print(f'************')
        print(f'Name:{self.name}')
        print(f'Animal:{self.animal}')
        print(f'Breed:{self.breed}')
        print(f'Color:{self.color}')
        print(f'Age:{self.age}')

#สร้าง object
if __name__ == "__main__":
    ula = Animal()
    ula.new_animal("Ula","Scottish","White",1)
    ula.print_detail()

#แก้class 
Animal.animal = "FISH"
if __name__ == "__main__":
    ula = Animal()
    ula.animal = "DOG" #เปลี่ยนเฉพาะของula
    ula.new_animal("Ula","Scottish","White",1)
    ula.print_detail()

    drac = Animal()
    drac.new_animal("Drac","Scottish","White",1)
    #เปลี่ยนค่าตัวแปร แก้ไขข้อมูล จาก Scottish เป็น Catfish
    drac.breed = "Catfish"
    drac.print_detail()


    #เรียกดูข้อมูลของ object ผ่านทางชื่อ class
    Animal.print_detail(ula) #ula.print_detail()
    Animal.print_detail(drac) #drac.print_detail()