from animal import Animal

class Dog(Animal):
    def info(self):
        #super().info() ทำแบบนี้ได้
        Animal.info(self)  #เรียกจากชื่อคลาสแม่แบบนี้ก็ได้ และตามจำนวนพารามิเตอรืตามคลาสแม่
        print(f'I am a dog.')
        print(f'My name is {self.name}') #เรียกใช้private พารามิเตอร์ได้  เพราะทำgetter setter แล้ว
        print(f'I am {self.age} years old.')

    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Woof!! Woof!! sound.')

class Cat(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print(f'I am a cat.')
        print(f'My name is {self.name}') 
        print(f'I am {self.age} years old.')

    def make_sound(self):
        #super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Meow!! Meow!! sound.')

class Cow(Animal):
    def info(self):
        #super().info()
        Animal.info(self)
        print(f'I am a cow.')
        print(f'My name is {self.name}') 
        print(f'I am {self.age} years old.')
    
    def make_sound(self):
        super().make_sound()
        Animal.make_sound(self)
        print(f'Hey! I make Moo!! Moo!! sound.')

