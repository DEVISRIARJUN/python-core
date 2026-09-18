# 5. Create a Product class where:
# • price cannot be negative
# • discount cannot exceed 70%
# • internal final price calculation should not be directly exposed
# Provide only one public method get_final_price().


class Product:
    def __init__(self,price,discount):
        self.price = price
        self.discount = discount
    
    


