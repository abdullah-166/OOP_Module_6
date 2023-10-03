class Company:
    def __init__(self, name, address) -> None:
        self.name = name
        self.bus = []
        self.routes = []
        self.driver = []
        self.counter = []
        self.manager = []
        self.supervisor = []
        self.fare = []
        pass

class Driver:
    def __init__(self, name, age, license) -> None:
        self.name = name
        self.age = age
        self.license = license
        pass

class Counter:
    def __init__(self) -> None:
        pass
    def purchase_ticker(self, start, destination):
        pass

class Passenger:
    pass

class Supervisor:
    pass

abir = Driver('abir', 'LM123', 35)

    