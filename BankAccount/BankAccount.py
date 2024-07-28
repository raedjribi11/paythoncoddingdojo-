class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.balance = balance
        self.int_rate = int_rate
    
    def deposit(self, amount):
        self.balance += amount
        return self 

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self  

    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self 

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.int_rate
        return self 
# Testing the BankAccount class with different test data and scenarios
account1 = BankAccount()
account1.deposit(100).withdraw(50).yield_interest().display_account_info()


# Creating an instance of BankAccount with specific initial balance and interest rate
account2 = BankAccount(int_rate=0.02, balance=200)
account2.deposit(200).withdraw(500).yield_interest().display_account_info()
