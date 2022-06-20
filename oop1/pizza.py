class Pizza:
    def __init__(self, ingredients) :
        self.ingredients = ingredients
    
    def __repr__(self) :
        #ส่งคืนค่าที่สามารถพิมพ์ได้
        return f'Pizza({self.ingredients})'
    
    @classmethod
    def margherita(cls):
        return cls ({'mozzarella','tomatoes'})

    @classmethod
    def prosciutto(cls):
        return cls ({'mozzarella','tomatoes','ham'}) 
    
    @staticmethod
        #มักเป็น utility หรือ helper function เพื่อทำให้ code เป็น modular
    def size(ch):
        ch = ch.upper()
        if ch == 'S':
            return 'small: 6 inches, 4 slices'
        elif ch == 'L':
            return 'Large: 14 inches, 10 slices'
        else:
            return 'Default Medium: 12 inches, 8 slices'
        
#create instance สร้างวัตถุ
my_pizza = Pizza('Cheese, Meat')
print(my_pizza)
print(my_pizza.margherita())

#static method
print('---- Satatic Method ----')
print(Pizza.size('L'))

#class method
print('---- Class Method ----')
print(Pizza.margherita()) #เรียกผ่านชื่อclass
print(Pizza.prosciutto())
print(my_pizza.margherita()) #เรียกผ่านชื่อobject
print(Pizza.ingredients) #cannot access instannce variable ต้องเรียกผ่านobject เท่านั้น