class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner  # Public attribute
        self.__balance = balance  # Private attribute

    # Getter method to read private balance safely
    def get_balance(self):
        return self.__balance

    # Setter method to update private balance with validation
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Deposit amount must be positive.")

    # Private method
    def __log_transaction(self, action):
        print(f"[LOG]: {action}")


account = BankAccount("Alice", 1000)

# Public access works directly
print(account.owner)  # Output: Alice

# Private access using methods
account.deposit(500)  # Output: Deposited $500. New balance: $1500
print(account.get_balance())  # Output: 1500
