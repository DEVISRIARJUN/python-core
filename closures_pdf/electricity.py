# Question 1
# Write a function electricity(rate_per_unit).
# -   The outer function receives the cost per unit.
# -   The inner function receives the number of units consumed.
# -   Print the total electricity bill.
# -   Return the inner function.


def electricity(rate_per_unit):
    def bill(units):
        total = rate_per_unit * units
        print(total)
        return total
    return bill
c = electricity(5)
c(50)
