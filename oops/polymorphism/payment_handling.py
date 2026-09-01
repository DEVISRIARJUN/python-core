#   Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism.



class Upi:
    def pay(self,amount):
        print(f"{amount} paid using the upi")
class Card:
    def pay(self,amount):
        print(f"{amount} paid using the card")
class Cash:
    def pay(self,amount):
        print(f"{amount} paid using the cash")
def pay(obj,amount):
    obj.pay(amount)
def pay2(obj,amount):
    if isinstance(obj,Upi):
        obj.pay(amount)
l = [Upi(),Card(),Cash()]
for i in l:
    pay(i,7000)
    pay2(i,2000)