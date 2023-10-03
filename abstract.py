from abc import *
class Animal(ABC):
    @abstractmethod  #enforce all derived class
    def eat(self):
        print('I need food!!!')

    def move(self):
        print('moving somewhere!!!!')

class Monkey(Animal):
    def __init__(self, name) -> None:
        self.name = 'Monkey'
        self.name = name
        super().__init__()

    def eat(self):
        print('eating something!!!')

    def move(self):
        print('hanging!!!')

lio =  Monkey('lucky')
lio.eat()
lio.move()