class Rectangle:
    def __init__(self,width,length) -> None:
        self.width = width  #กำหนดค่าลงตัวแปร width ตัวซ้าย
        self.length = length
        self.area = 0

    def get_data(self):
        pass

    def compute_area(self):
        self.area = self.width * self.length     #attributeในclass สามารถเรียกใช้ได้ทุกตัวโดยไม่ต้องreturnค่า

    def print_area(self):
        print(f"Rectangle Area : {self.area}")

#สร้าง object
rec_obj = Rectangle(2,5) #ระบุค่าของตัวแปรwidth กับ length
rec_obj.compute_area() #เรียกใช้method .ตามด้วยชื่อ method
rec_obj.print_area()

#ใส่ค่าเอง ไม่ได้รับค่าจากuser