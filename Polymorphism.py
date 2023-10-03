class Animal:
    def __init__(self, name) -> None:
        self.name = name

    def make_sound(self):
        print('animal making sound')

class Cat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Cat sound')

class Dog(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Dog sound')

class Goat(Animal):
    def __init__(self, name) -> None:
        super().__init__(name)

    def make_sound(self):
        print('Goat sound')

don = Cat('Real Madrid')
don.make_sound()

donti = Dog('Real Madrid')
donti.make_sound()

black  = Goat('Bercelona')
black.make_sound()

animals = [don, donti, black]
for animal in animals:
    animal.make_sound()


        