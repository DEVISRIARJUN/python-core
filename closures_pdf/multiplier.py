# Question 6

# Write a function multiplier(number).

# -   The outer function receives one number.
# -   The inner function receives another number.
# -   Print their multiplication.
# -   Return the inner function.

def multiplier(number):
    def another(number2):
        multiply = number * number2
        print(multiply)
        return multiply
    return another
c = multiplier(5)
c(5)