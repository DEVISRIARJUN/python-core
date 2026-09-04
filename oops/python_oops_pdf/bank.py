#   Q8. Create:
# • Base Account → withdraw()
# • Subclass SavingsAccount → modifies withdraw()
# • Subclass PremiumSavingsAccount → overrides again but calls parent using super()
# Show how polymorphism works across multiple levels.


class Account:
    def withdraw(self):
        print("Account created")
class SavingsAccount(Account):
    def withdraw(self):
        print("Savings Account created")
class PreminumSavingsAccount(SavingsAccount):
    def withdraw(self):
        super().withdraw()
        print("Premium Savings Account Created")
s = SavingsAccount()
s.withdraw()
p = PreminumSavingsAccount()
p.withdraw()