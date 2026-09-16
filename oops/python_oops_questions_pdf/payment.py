# Q10. Design a polymorphic system for payment handling (UPI, Card, Cash) — all have a
# pay() method.
# Now implement a version that checks types explicitly using isinstance() before calling
# pay().
# Compare both designs and explain why one breaks the spirit of polymorphism


class UPI:
    def pay(self):
        print("Payment made using UPI")


class Card:
    def pay(self):
        print("Payment made using Card")


class Cash:
    def pay(self):
        print("Payment made using Cash")


def process_payment(payment):
    payment.pay()


payments = [UPI(), Card(), Cash()]

for payment in payments:
    process_payment(payment)