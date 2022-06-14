class Rectangle:
    def __init__(self) -> None:
        self.width = 0
        self.length = 0
        self.area = 0

    def get_data(self):
        self.width = float(input("Enter width: "))
        self.length = float(input("Enter length: "))

    def compute_area(self):
        self.area = self.width * self.length     #attributeในclass สามารถเรียกใช้ได้ทุกตัวโดยไม่ต้องreturnค่า

    def print_area(self):
        print(f"Rectangle Area : {self.area}")

#สร้าง object
rec_obj = Rectangle() #ระบุค่าของตัวแปรwidth กับ length
rec_obj.get_data()     #เรียกใช้method .ตามด้วยชื่อ method
rec_obj.compute_area() 
rec_obj.print_area()

#รับค่าจาก user