from documentary_private import Documentary
m =Documentary('Mulan',2020,'action')
#m.__get_movie() #เรียก private method ไม่ได้
#print(m.__genre) #เรียก private attribute ไม่ได้

m.print_detail()  #เรียกใช้  private method จาก  private method ที่เตรียมไว้

print(f'Year: {m._Movie__year}') #ลักไก่เข้าถึงตัวแปร private --> obj.name._classname__private attribute