class BankAccount:
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance
 
    def deposit(self, amount):
        if amount < 0:
            raise ValueError("Deposit amount cannot be negative.")
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient balance for withdrawal.")
        self.balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

account = BankAccount("Bhumi", 1000)

try:
    account.deposit(500)
    account.withdraw(2000)  # This will raise an error
except ValueError as e:
    print("Error:", e)

account.check_balance()
