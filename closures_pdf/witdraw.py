
# Write a function bank_account(balance).

# -   The outer function receives the initial balance.
# -   The inner function receives an amount to withdraw.
# -   Print the remaining balance.
# -   Return the inner function.


def bank_account(balance):
    def amount(withdraw):
        if balance >= withdraw:
            final = balance - withdraw
            print(final)
            return final
        else:
            print("Insufficient balance")
    return amount
c = bank_account(50000)
c(51000)