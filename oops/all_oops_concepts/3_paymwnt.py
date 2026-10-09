# 3. Create:
# • Abstract class PaymentMethod with pay(), validate()
# • Subclasses: CardPayment, WalletPayment, UPIPayment
# • Encapsulate user balance
# • Use @property to control reading available funds
# • Overload + operator to combine two payment methods into “split payment”
# • Demonstrate polymorphism through a checkout loop.



from abc import ABC,abstractmethod
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self,balance):
        pass
    @abstractmethod
    def validate(self):
        pass 
class CardPayment(PaymentMethod):
    def __init__(self,balance):
        self.__balance = balance
    @property
    def balance(self):
        return self.__balance
    def validate(self):
        return self.__balance > 0
    def pay(self,amount):
        if self.validate() and amount < self.__balance:
            self.__balance -= 1
            print("Payment is done using the card")
    def __add__(self,other):
        
