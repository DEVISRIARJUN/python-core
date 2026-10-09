# 12. Design an abstract class PaymentGateway with:
# • authenticate()
# • pay(amount)
# • refund(amount)
# Implement subclasses:
# • UPIPayment
# • CardPayment
# • NetBankingPayment



from abc import ABC,abstractmethod
class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self):
        pass
    @abstractmethod
    def pay(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
class UPIPayment(PaymentGateway):
    def authenticate(self):
        print("Authentucate successful")
    def pay(self,amount):
        print("Paid",amount,"Using phonepe")
    def refund(self,amount):
        print("Refunded",amount,"From phonepe")
class CardPayment(PaymentGateway):
    def authenticate(self):
        print("Authentication Successful")
    def pay(self,amount):
        print("Paid",amount,"Using my walletcard")
    def refund(self,amount):
        print("Refunded the",amount,"To my wallet")
class Netbanking(PaymentGateway):
    def authenticate(self):
        print("Authentication sucessful")
    def pay(self,amount):
        print("Padi the",amount,"Using my netbanking")
    def refund(self,amount):
        print("Refunded the",amount,"to my netbanking")

print("Using upi payment")
upi = UPIPayment()
upi.authenticate()
upi.pay(2000)
upi.refund(5000)

print()
print("using the cardpayment")
card = CardPayment()
card.authenticate()
card.pay(5000)
card.refund(3500)

print()
print("Using the netbanking payment")
netbank = Netbanking()
netbank.authenticate()
netbank.pay(6000)
netbank.refund(7000)