#base class, parent class, common attributr + functionality
#derived class, child class, uncommon attribute + functionality\
class Gadget:
    def __init__(self,brand, price, color,origin) -> None:
        self.brand = brand
        self.price = price
        self.color = color
        self.origin = origin

    def run(self):
        return f'Running Laptop {self.brand}'
    
class Laptop:
    def __init__(self, memory, ssd) -> None:
        self.memory = memory
        self.ssd = ssd

    def coding(self):
        return f'Learing python and practicing'
    
class Phone(Gadget):
    def __init__(self, brand, price, color,origin, sim) -> None:
        self.sim = sim
        super().__init__(brand,price, origin, color)

    def phone_call(self, number, text):
        return f'Sending message to {number}'
    
    def __repr__(self) -> str:
        return f'phone: {self.brand}, {self.price}, {self.sim}'
    
class Camera:
    def __init__(self, pixel) -> None:
        self.pixel = pixel

    def change_lens(self):
        pass

my_phone = Phone('iphone', 65000, 'Golden', 'USA', True)
print(my_phone.brand)
print(my_phone)
