# Question 2
# Write a function salary(bonus).
# -   The outer function receives the bonus amount.
# -   The inner function receives the employee’s basic salary.
# -   Print the total salary after adding the bonus.
# -   Return the inner function.

def salary(bonus):
    def employ(basicsal):
        total = basicsal + bonus
        # print(total)
        return total
    return employ
c = salary(1000)
print(c(20000))