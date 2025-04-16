class BankAccount: 
    def __init__(self, account_holder_name, balance=0):
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Insufficient balance.")

    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")

  
account = BankAccount("Bhumi", 1000)
account.deposit(500)
account.withdraw(300)
account.check_balance()
