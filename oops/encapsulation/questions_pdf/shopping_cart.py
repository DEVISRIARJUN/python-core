# 8. Create a ShoppingCart class where:
# • items are stored privately
# • users cannot directly modify item list
# • only add/remove methods are allowed
# • provide a method to get a safe copy of the cart items (not direct reference to internal
# list)

class Shoppingcart:
    def __init__(self):
        self.__items = []
    def __add__(self,p):
        self.__items.append(p)
    def __sub__(self,p):
        self.__items.remove(p)
    def get_cart(self):
        return self.__items.copy()
c1 = Shoppingcart()
c1 + "iphone"
c1 + "laptop"
c1 - "iphone"  
print(c1.get_cart())      