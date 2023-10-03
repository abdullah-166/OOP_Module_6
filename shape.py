from math import *
class Shape:
    def __init__(self, name) -> None:
        self.name = name

class Rectangle(Shape):
    def __init__(self, name, length, width) -> None:
        self.length = length
        self.width =  width
        super().__init__(name)

    def get_area(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, name, radius) -> None:
        self.radius = radius
        super().__init__(name)

    def get_area(self):
        return pi * self.radius*self.radius
    
circle = Circle('radius',6)
print(circle.get_area())
    


