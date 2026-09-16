# Q2. Design a
# class Product that
# Maintains a base tax rate applicable to all products.
# Each product has a name and base price.
# Has a method to compute final price including tax.
# Can change tax rate for all products using one method.
# Includes a function to check whether a given price is valid or not (non-negative and realistic).

class Product:
    tax_rate = 12
    def __init__(self,name,price):
        self.name = name
        self.price = price
    def final_price(self):
        tax = self.price * Product.tax_rate / 100
        return self.price + tax
    @classmethod
    def change_tax(cls,new_tax):
        cls.tax_rate =   new_tax
    @staticmethod
    def valid(price):
        if price >= 0 and price <= 100000:
            print("Valid price")
        else:
            print("Not valid price")
c1 = Product("Arjun",20000)
print(c1.name)
print(c1.price)
print(Product.valid(50000))
Product.change_tax(15)