class Laptop:
    def __init__(self,brand, price, color, memory) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.memory = memory

    def run(self):
        return f'Running Laptop {self.brand}'
    
    def coding(self):
        return f'Learing python and practicing'
    
class Phone:
    def __init__(self,brand, price, color, sim) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.sim = sim

    def run(self):
        return f'Whole day you are using phone'

    def call(self, number, text):
        return f'Sending message to {number}'
    
class Camera:
    def __init__(self, brand,price,color,pixel) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.pixel = pixel

    def run(self):
        pass

    def change_lens(self):
        pass
