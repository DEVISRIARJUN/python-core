# 1. Design a banking system with:
# • An abstract base class Account with deposit(), withdraw(),
# calculate_interest().
# • Subclasses: SavingsAccount, CurrentAccount, FixedDepositAccount.
# • Each account must:
# o Encapsulate balance (private)
# o Provide controlled access through properties
# o Override interest calculation differently
# • Include a static method to validate amount.
# • Include a class method to update bank-wide interest policies.


from abc import ABC, abstractmethod


class Account(ABC):

    interest_rate = 0.5

    @abstractmethod
    def deposit(self, amount):
        pass

    @abstractmethod
    def withdraw(self, amount):
        pass

    @abstractmethod
    def calculate_interest(self):
        pass

    @staticmethod
    def validate_amount(amount):
        if amount > 0:
            return True
        return False

    @classmethod
    def policies(cls, new_rate):
        cls.interest_rate = new_rate


class SavingsAccount(Account):

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balances(self):
        return self.__balance

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount

    def withdraw(self, amount):
        if self.validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount

    def calculate_interest(self):
        return self.__balance * 0.04


class CurrentAccount(Account):

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balances(self):
        return self.__balance

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount

    def withdraw(self, amount):
        if self.validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount

    def calculate_interest(self):
        return self.__balance * 0.02


class FixedDepositAccount(Account):

    def __init__(self, balance):
        self.__balance = balance

    @property
    def balances(self):
        return self.__balance

    def deposit(self, amount):
        if self.validate_amount(amount):
            self.__balance += amount

    def withdraw(self, amount):
        if self.validate_amount(amount) and amount <= self.__balance:
            self.__balance -= amount

    def calculate_interest(self):
        return self.__balance * 0.07


s = SavingsAccount(5000)
print("Savings :",s.balances)

s.deposit(10000)
print("After Deposited",s.balances)

s.withdraw(7800)
print("After withdraw",s.balances)


print(s.calculate_interest())