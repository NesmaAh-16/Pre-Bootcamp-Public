class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if(self.balance-amount)<0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        else:
            self.balance-=amount
        return self
    def yield_interest(self):
        if(self.balance>0):
         self.balance= self.balance + (self.balance *self.int_rate ) 
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")

class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.accounts={
            "test_account_A" : BankAccount(0.02, 100),    
            "test_account_B" : BankAccount(0.03) 
        }
    
    def make_deposit(self, account_name, amount):
        self.accounts[account_name].balance+=amount  
        return self
    
    def make_withdrawal(self, account_name,amount):
        self.accounts[account_name].balance-=amount  
        return self
        
    def display_user_balance(self):
        print(f"User: {self.name}")
        for name,account in self.accounts.items():
            print(f"Account Name: {name}")
            account.display_account_info()
        return self
    
    def transfer_money(self,my_account_name, other_user, other_account_name, amount):
        self.make_withdrawal(my_account_name, amount)
        other_user.make_deposit(other_account_name, amount)    
    
guido= User("Guido van Rossum","guido@python.com")
monty= User("Monty python","monty@python.com")
dojo= User("Dojo python","dojo@python.com")

guido.make_deposit("test_account_A", 100)
guido.make_deposit("test_account_B", 700)
guido.transfer_money("test_account_A", monty, "test_account_B",300)

guido.display_user_balance()
monty.display_user_balance()

   