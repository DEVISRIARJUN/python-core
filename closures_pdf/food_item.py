# Question 7

# Write a function restaurant(food_item).

# -   The outer function stores the food item.
# -   The inner function receives the quantity.
# -   Print the order details.
# -   Return the inner function.

def restaurent(food_item):
    def food(quantity):
        return f"food : {food_item} \n quantity : {quantity}"
    return food
c = restaurent("pongal")
print(c(5))