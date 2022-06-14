#ต้องสร้างclass = แม่พิมพ์ ตัวต้นแบบ
#object = สิ่งที่ได้ออกมาจากแม่พิมพ์ ถูกสร้างมาจากแม่พิมพ์
class LightSwitch():
    def __init__(self) -> None: #เครื่องหมาย'_' สองครั้งทั้งหน้าและหลัง init
        self.switch_status = False

    def turnon(self):
        self.switch_status = True

    def turnoff(self):
        self.switch_status = False

    def show(self):
        print(f'status = {self.switch_status}')

#สร้างวัตถุ(object) จากแม่พิมพ์(class)
switch_obj = LightSwitch() #switch_obj ถูกสร้างมาจากแม่พิมพ์LightSwitch

#เรียกใช้method
switch_obj.show() #False
switch_obj.turnon()
switch_obj.show() #True
switch_obj.turnoff()
switch_obj.show() #False
switch_obj.turnoff()
switch_obj.show() #False
switch_obj.show() #False