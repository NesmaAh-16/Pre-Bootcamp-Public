class BankAccount:
    def __init__(self, int_rate, balance=0):
        self.int_rate=int_rate
        self.balance=balance
    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if(self.balance-amount<0):
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
     
test_account_A = BankAccount(0.02, 100)    
test_account_B= BankAccount(0.03) 

test_account_A.deposit(20).deposit(30).deposit(40).withdraw(100).yield_interest().display_account_info() #91.8
test_account_B.deposit(200).deposit(300).withdraw(400).withdraw(150).yield_interest().display_account_info() #97.85

   
