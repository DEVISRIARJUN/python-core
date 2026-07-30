# Question 3

# Write a function discount(percent).

# -   The outer function receives the discount percentage.
# -   The inner function receives the product price.
# -   Print the final price after applying the discount.
# -   Return the inner function.

def discount(percent):
    def product(original_price):
        final_price = original_price - (original_price * percent / 100)
        # print(final_price)
        return final_price
    return product
c = discount(20)
print(c(10000))
