class Student:
    #major:str = 'IT' กำหนดค่าdefault ในกรณีผู้ใช้ไม่ใส่ค่า จะใส่อัตโนมัติ
    #major = 'IT'
    def __init__(self,id:str,name:str,major:str = 'IT') -> None:  
        self.id = id
        self.name = name
        self.major = major

    def display_detail(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')
        print(f'Major: {self.major}')

    def __del__ (self):
        print(f'Object was destroied')

if __name__ == "__main__":
    jessica = Student("111","Jessica","IT")
    jessica.display_detail()

    john = Student("112","John","MKT")
    john.display_detail()

    amy = Student('113','Amy')
    amy.display_detail()