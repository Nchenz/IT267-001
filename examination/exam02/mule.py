from horse import Horse
from donkey import Donkey

class Mule(Horse,Donkey):
    def __init__(self, name: str, color: str, max_height: float) -> None:
        super().__init__(name, color, max_height=200)

    def run(self):
        super().run()
        print(f'Mule is running')

    def show_info(self):
        super().show_info()
        print(f'***** {self.name} Info *****')
        print(f'Name: {self.name}')
        print(f'Color: {self.color}')
        print(f'Max Height: {Horse.max_height}')
        print(f'Age: {self.age}')
        print(f'Weight: {self.weight}')