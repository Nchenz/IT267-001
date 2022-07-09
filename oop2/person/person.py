class Person:
    def __init__(self,name) -> None:
        self.name = name

    def welcome(self):
        print(f'Hi, {self.name}')