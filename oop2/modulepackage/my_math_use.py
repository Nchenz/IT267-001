#from my_math import sqrt,circle_area
import my_math as my #เรียกทุกตัวตั้งชื่อเล่นว่าmy

if __name__ == '__main__':
    square_number = my.sqrt(5) #เรียกใช้โดย ชื่อโมดูล.ชื่อฟังก์ชั่น
    print(square_number)
    print(my.PI)
    print(my.circle_area(3))