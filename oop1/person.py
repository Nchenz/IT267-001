class  person:
    country = "Thailand" #class variables
    def __init__(self,name,gender,profession,hours) -> None:
        #instance variables
        self.name = name
        self.gender = gender
        self.profession = profession
        self.hours = hours

    
    def work(self):
        print(f'{self.name} is working as a {self.profession}')

    def study(self):
        print(f'{self.name} studies for {self.hours}hour(s)')

    def show(self):
        print(f'Name:{self.name} Gender:{self.gender} Profession:{self.profession} Study:{self.hours}')

    def __del__ (self):
        print(f'Object was destroied')

#สร้าง object
jessa = person("jessa","Female","Software Engineer","10")
jessa.show()
jessa.work()
jessa.study()

#สร้าง object ตัวใหม่
jon = person("Jon","Male","Doctor","15")
jon.show()
jon.work()
jon.study()

#สร้าง object ตัวใหม่
lalisa = person("Lalisa","Female","Korea Singer","13")
lalisa.work()

#เรียกใช้ class variables
print(f"Class Variables: {person.country}")
print(f"Instance Variables: {lalisa.country}")

#เปลี่ยนค่า เฉพาะ object
lalisa.country = "Korea"
print("--------")
print(f"Class Variables: {person.country}")
print(f"Instance Variables: {lalisa.country}")
print(f"Instance Variables: {jon.country}")  #ไม่กระทบกับค่าของobject อื่นๆ

#แก้class 
person.country = "England"
print("*******")
print(f"Class Variables: {person.country}")
print(f"Instance Variables: {lalisa.country}")
print(f"Instance Variables: {jon.country}")