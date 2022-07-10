class JuiceOrder:
    total = 0
    def __init__(self,menu:str,size:str) -> None:
        self.menu = menu.upper()
        self.size = size.upper()
        self.price:int = 0

    def check_menu(self):
        menu_dict = {
            'OJ':25,
            'AJ':25,
            'WJ':30,
            'PJ':30,
            }
        if self.menu in menu_dict:
            self.price = menu_dict.get(self.menu)
        
    def compute_price(self):
        if self.size == 'L':
            self.price += 5
        else:
            self.price
        JuiceOrder.total =  self.price 

    def display_order(self):
        self.check_menu()      
        self.compute_price()   
        return f'{self.menu}({self.size}*{self.price}) => {JuiceOrder.total} baht'

if __name__ == '__main__':
    order1 = JuiceOrder('WJ','L')
    order2 = JuiceOrder('OJ','R')
    order3 = JuiceOrder('PJ','L')
    print(order1.display_order())
    print(order2.display_order())
    print(order3.display_order())