#สร้างฟังก์ชั่นเปิดไฟ

def turnon():
    global switch_status
    switch_status = True #เปลี่ยนสถานะเป็นเปิดไฟ


#สร้างฟังก์ชั่นปิดไฟ
def turnoff():
    global switch_status
    switch_status = False #เปลี่ยนสถานะเป็นปิดไฟ

switch_status = False #ไฟปิด

print(f'Status = {switch_status}') #False
turnon()
print(f'Status = {switch_status}') #True
turnoff()
print(f'Status = {switch_status}') #False
turnoff()
print(f'Status = {switch_status}') #False
print(f'Status = {switch_status}') #False