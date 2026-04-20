class User:
    def __init__(self,name,email):
        self.name=name
        self.email=email
        self.account_balance=0
    
    def make_deposit(self,amount):
        self.account_balance+=amount
    
    def make_withdrawal(self,amount):
        self.account_balance-=amount
        
    def display_user_balance(self):
        print(f"User: {self.name} ,Balance: ${self.account_balance}")
    
    def transfer_money(self, other_user, amount):
        self.make_withdrawal(amount)
        other_user.make_deposit(amount)
    

guido= User("Guido van Rossum","guido@python.com")
monty= User("Monty python","monty@python.com")
dojo= User("Dojo python","dojo@python.com")

#first instance
guido.make_deposit(20)
guido.make_deposit(40)
guido.make_deposit(60)
guido.make_withdrawal(20)
guido.display_user_balance()  #100

#second instance
monty.make_deposit(20)
monty.make_deposit(40)
monty.make_withdrawal(20)
monty.make_withdrawal(20)
monty.display_user_balance()  #20

#third instance
dojo.make_deposit(100)
dojo.make_withdrawal(30)
dojo.make_withdrawal(20)
dojo.make_withdrawal(40)
dojo.display_user_balance()  #10

guido.transfer_money(dojo,30)
guido.display_user_balance()  #70
dojo.display_user_balance()   #40
    
    