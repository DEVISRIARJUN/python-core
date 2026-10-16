# 6. Create a class in a module that uses private attributes and @property / 
# @setter decorators. Import the class into another module and show how 
# encapsulation protects the data while still allowing controlled access.


class Balance:
    def __init__(self,balance):
        self.__balance = balance
    @property
    def show_balance(self):
        return self.__balance
    @show_balance.setter
    def deposit_bal(self,amount):
        if self.__balance > 0:
            self.__balance += amount
        return self.__balance

