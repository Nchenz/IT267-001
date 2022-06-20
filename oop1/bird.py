#global variable ประกาศนอกclass ได้เลย
bird_type = 'parrot'
class Bird:
    #class variable 
    bird_name = 'Peter'
    def __init__(self,color) -> None:
        #instance variable 
        self.color = color
        
        #local variable จะไม่มี self นำหน้า และถูกเรียกใช้ได้แค่ในฟังก์ชั่นที่มันอยู่เท่านั้น
        country = 'Thailand'
        print(country)

    def show(self):
        return f'{bird_type} {Bird.bird_name} has {self.color}'

#create object
if __name__ == '__main__':
    my_bird = Bird('Red,Yellow')
    print(my_bird.show())
    print(f'**** {bird_type}****') #เรียกใช้ global variable ในส่วนmain ได้
    
    
    """เรียก class variable มาใช้ในส่วน main
    print(bird_name) เรียกแบบนี้ไม่ได้ error"""
    #เรียก class variable มาใช้ในส่วน main ชื่อclass.class variable
    print(Bird.bird_name)
     #เรียก class variable มาใช้ในส่วน main ชื่อวัตถุ.class variable เพราะวัตถุถอดแบบมากจากclass
    print(my_bird.bird_name)

    """เรียก instance variable ในส่วนmain
    print(Bird.color) เรียกแบบนี้ไม่ได้ error"""
    #เรียก instance variable ในส่วนmain ชื่อวัตถุ.instance variable
    print(my_bird.color)