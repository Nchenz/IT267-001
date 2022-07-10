class Donkey:
    def __init__(self,age:int,weight:float) -> None:
        self.age = age
        self.weight = weight

    def sound(self):
        print(f'Donkey makes eeyore sound')

    def show_info(self):
        print(f'Age: {self.age}-year-old')
        print(f'Weight: {self.weight} kg')