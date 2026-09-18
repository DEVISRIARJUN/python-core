

# 1. Create a BankAccount class that stores:
# • account number
# • balance (should not be directly modifiable)
# You must:
# 1. Make the balance attribute inaccessible from outside.
# 2. Provide functions to deposit/withdraw that validate the amount.
# 3. Prevent withdrawal if balance becomes negative.
# 4. Show what happens if someone tries to modify balance directly and why
# encapsulation prevents it.

class BankAccount:
    def __init__(self,accnumber,balance):
        self.accnumber = accnumber
        self.__balance = balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Deposited",amount)
        else:
            print("Invalid deposit")
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawl")
        elif amount > self.__balance:
            print("Insuffiecient balance")
        else:
            self.__balance -= amount
            print("Withdrawn",amount)  
    def show_balance(self):
        print("Balance :",self.__balance)
b = BankAccount(123438604735,10000)  
b.show_balance()
b.deposit(350)
b.show_balance()
b.withdraw(0)
b.withdraw(455)
b.show_balance()
b.__balance = 5000
b.show_balance()
print(b.__balance)

