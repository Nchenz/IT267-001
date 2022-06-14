class Item:
    def __init__(self,name:str,price:float,quantity:int) -> None:  
        assert price >= 1 ,f"Price should more than or equal to 1"
        assert quantity >= 1,f"Quantity should more than or equal to 1"
        #รู้ ชื่อสินค้า ราคา จำนวน
        self.name = name
        self.price = price
        self.quantity = quantity
        

    def calculate_total_price(self):
        #ราคาสุทธิ = ราคาสินค้า * จำนวนสินค้า
        return self.price * self.quantity #รีเทิร์นค่าให้คำนวนได้

    def __del__ (self):
        print(f'Object was destroied')

if __name__ == "__main__":
    #สร้าง object
    item1 = Item("cup",25,2)
    item2 = Item("cone",10,3)
    print(f'*****Total Price*****')
    print(f'{item1.name}: {item1.calculate_total_price()}')
    print(f'{item2.name}: {item2.calculate_total_price()}')