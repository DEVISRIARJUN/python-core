# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price().


class Product:
    def __init__(self,price,discount):
        if price < 0:
            print("Invalid price")
            return
        if discount > 70:
            print("discount exceeded")
            return
        self.__price = price
        self.__discount = discount
    def __finalcalculation(self):
        discount_price = self.__price * self.__discount / 100
        final_price = self.__price - discount_price
        return final_price
    def get_final_price(self):
        return self.__finalcalculation()
p = Product(1000,20)
print(p.get_final_price())

            
        