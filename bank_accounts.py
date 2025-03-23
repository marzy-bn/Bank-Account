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

class BankOfAmerica(BankAccount):
    def __init__(self, name, balance, interest_rate):
        self.interest_rate = interest_rate
        super().__init__(name, balance)
    
    def get_interest_amount(self, duration):
        interest_amount = super().get_balance() * (self.interest_rate / 100) * duration
        return interest_amount        

#class BOALoan(BankOfAmerica):
#    def __init__(self, )

obj = BankOfAmerica('Tom',10000, 2)
amount = obj.get_interest_amount(2)
print(amount)

"""
num = BankAccount('Tom',10000)
num.deposit(1000)
print(num.get_balance())
num.withdraw(20000)
print(num.get_balance())
print(num.__dict__)
num.name = 'Steve'
print(num.__dict__)
print(num.get_balance())
"""
