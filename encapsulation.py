class Bank:
    def __init__(self, holder_name, initial_deposit) -> None:
        self.name = holder_name #public attribute
        self.__balance = initial_deposit #protected attribute
        self._branch = 'Uttara-10' #private attribute

    def deposit(self, amount):
        self.__balance += amount

    def get_balance(self):
        return self.__balance

    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance = self.__balance - amount
            return amount
        else:
            return f'Not enough money'

rafsan = Bank('choto vai', 5000)
print(rafsan.name)
rafsan.deposit = 2000
print(rafsan.get_balance())
print(rafsan._branch)
print(rafsan.withdraw(3))

        