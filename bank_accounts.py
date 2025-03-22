class BankAccount:
    
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance
    
    def deposit(self, amount):
        self.__balance += amount


    def withdraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
        else:
            print('Insufficient balance')

    def get_balance(self):
        return self.__balance
    
num = BankAccount('Tom',10000)
num.deposit(1000)
print(num.get_balance())
num.withdraw(20000)
print(num.get_balance())
print(num.__dict__)
num.name = 'Steve'
print(num.__dict__)
print(num.get_balance())