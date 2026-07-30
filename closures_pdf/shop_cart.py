# Question 9

# Write a function shopping_cart(item_name).

# -   The outer function receives the item name.
# -   The inner function receives:
#     -   quantity
#     -   price per item
# -   Print the item name, quantity, and total price.
# -   Return the inner function.

def shopping_cart(item_name):
    def cart(quantity,price):
        total = quantity * price
        return f"name : {item_name} \n qunatity : {quantity} \n price : {total}"
    return cart
c =shopping_cart("THAR")
print(c(2,400000))