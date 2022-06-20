"""class CoffeeOrder:
    menu_type = 'Coffee'
    total = 0

    def __init__(self,customer_name,menu,num,size,price) -> None:
        self.customer_name = customer_name
        self.menu = menu
        self.num = num
        self.size = size
        self.price = price

    def check_menu(self):
        menu_dict = {'CM':5.99,'CP':4.99,'AM':4.99,'CL':4.99,'VL':4.75,'ES':3.00}
        if menu_dict == 'CM':
            return self.price == menu_dict.values[1]
        elif menu_dict == 'CP':
            return self.price == menu_dict.values[2]
        elif menu_dict == 'AM':
            return self.price== menu_dict.values[3]
        elif menu_dict == 'CL':
            return self.price == menu_dict.values[4]
        elif menu_dict == 'VL':
            return self.price == menu_dict.values[5]
        else:
            return self.price == menu_dict.values[6]

    def compute_price(self):
        if self.size == 'L':
            total = (self.price + 1) * self.num
            return total
        elif self.size == 'XL':
            total = (self.price + 1.5) * self.num
            return total
        else:
            total = (self.price * self.num)
            return total

    def display_detail(self):
        print(f'{self.customer_name}, {self.menu}, {self.size} ({self.num * self.price}) => {total}')"""

class CoffeeOrder:
    #class variable
    menu_type = 'Coffee'
    total = 0
    def __init__(self,customer_name:str,menu:str,num:int=1,size:str='R') -> None:
        #instance variable
        self.customer_name = customer_name
        self.menu = menu.upper()
        self.num = num
        self.size = size.upper() #ใส่ตัวเล็กหรือใหญ่จะเปลี่ยนให้เป็นตัวใหญ่
        #กำหนด price ไว้ก่อน หรือไม่ก็ได้
        self.price = 0

    def check_menu(self):
        menu_dict = {
            'CM':5.99,
            'CP':4.99,
            'AM':4.99,
            'CL':4.99,
            'VL':4.75,
            'ES':3.00
            }
        if self.menu in menu_dict:
            self.price = menu_dict.get(self.menu)
        """ if self.menu == 'CM':
            self.price = menu_dict.get('CM')""" #หรือไล่เขียนแบบนี้ไปเรื่อยๆก็ได้
    def compute_price(self):
        if self.size == 'L':
            #self.price = self.price + 1
            self.price += 1
        elif self.size == 'XL':
            self.price += 1.5
        else:
            self.price

        #คำนวนราคารวมทั้งหมด = จำนวนแก้ว * ราคา
        CoffeeOrder.total = self.num * self.price  #ตัวแปรtotalเป็นclass variable ต้องเรียกจากชื่อmetod.ตามด้วยชื่อclass variable

    def display_detail(self):
        self.check_menu()      #ให้display_detail เรียกใช้method อื่นๆ เพระาต้องทำmethod นี้ก่อนอยุ่แล้ว
        self.compute_price()    #ให้display_detail เรียกใช้method อื่นๆ เพระาต้องทำmethod นี้ก่อนอยุ่แล้ว
        return f'{self.customer_name}, {self.menu}, {self.size} ({self.num}{self.size} * ${self.price}) => ${CoffeeOrder.total}' #ตัวแปรtotalเป็นclass variable ต้องเรียกจากชื่อmetod.ตามด้วยชื่อclass variable

    def __del__ (self):
        print('Object was destroied')

#create object
if __name__ == '__main__':
    order1 = CoffeeOrder('John','es')
    order2 = CoffeeOrder('Mary','am',2,'l')

    """order1.check_menu()   #เพราะเรียกใช้ใน disp;ay_detail แล้วก็ไม่ต้องเรียกใช้แล้ว
    order1.compute_price()""" #เพราะเรียกใช้ใน disp;ay_detail แล้วก็ไม่ต้องเรียกใช้แล้ว
    print(order1.display_detail())

    """order2.check_menu()  #เพราะเรียกใช้ใน disp;ay_detail แล้วก็ไม่ต้องเรียกใช้แล้ว
    order2.compute_price()"""  #เพราะเรียกใช้ใน disp;ay_detail แล้วก็ไม่ต้องเรียกใช้แล้ว
    print(order2.display_detail())