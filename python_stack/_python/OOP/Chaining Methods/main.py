class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account_balance=0
    
    def make_deposit(self,amount):
        self.account_balance+=amount
        return self
    
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        return self
        
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
        return self
     
    def display_user_balance(self):
        print(f"User: {self.name} ,Balance: ${self.account_balance}")
    
guido= User("Guido van Rossum","guido@python.com")
monty= User("Monty python","monty@python.com")
dojo= User("Dojo python","dojo@python.com")

#first instance
guido.make_deposit(20).make_deposit(40).make_deposit(60).make_withdrawal(20).display_user_balance()  #100

#second instance
monty.make_deposit(20).make_deposit(40).make_withdrawal(20).make_withdrawal(20).display_user_balance()  #20

#third instance
dojo.make_deposit(100).make_withdrawal(30).make_withdrawal(20).make_withdrawal(40).display_user_balance()  #10

guido.transfer_money(dojo,30).display_user_balance()  #70
dojo.display_user_balance()   #40
    
    