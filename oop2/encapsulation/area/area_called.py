from area import Area
b = float(input('Enter base: '))
h = float(input('Enter high: '))

aobj = Area()
#เช็ทค่าเข้า setter เพื่อกำหนดค่า base , high
aobj.base = b
aobj.high = h
print(f'Area: {aobj.compute_area()}')