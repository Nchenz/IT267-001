class Dessert:
    def __init__(self) -> None:
        self.dessert = ['Ice cream','Mango stick rice']

    def show_dessert(self):
        return f'Dessert: {self.dessert}'

class Drink:
    def __init__(self) -> None:
        self.drink = ['Coffee','Tea','Wine','Soda']

    def add_drink(self,new_drink:str):
        #ชื่อlist.append(จะเพิ่มค่าไปที่ไหน)
        self.drink.append(new_drink)

    def show_drink(self):
        return f'Drink: {self.drink}'