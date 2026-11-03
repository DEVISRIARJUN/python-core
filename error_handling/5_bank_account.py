#  Create a class BankAccount with an attribute balance. Implement a method withdraw(amount) that raises an exception if the withdrawal amount is greater than the available balance.


# class BankAccount:
#     def __init__(self,balance):
#         self.balance = balance
#     def withdraw(self,amount):
#         if amount > self.balance:
#             raise Exception("Insuffiecient balance")
#         self.balance -= amount
#         print("Withdrawl Sucessful")
#         print("Remaining balance is : ",self.balance)
# b = BankAccount(5000)
# b.withdraw(2000)
# b.withdraw(4000)


class Bankaccount:
    def __init__(self,balance):
        self.balance = balance
    def withdraw(self,amount):
        if amount > self.balance:
            raise Exception("Insuffiecient balance")
        self.balance -= 1
        print("Withdrawl successful")
        print("reamining amount is",self.balance)
b  =Bankaccount(3000)
b.withdraw(2000)

b.withdraw(1000)

