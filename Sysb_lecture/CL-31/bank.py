class Bank: 
    balance=0 
    def __init__(self, name, inital_balance=0): 
        self.username = name
        self.inital_balance = inital_balance
        self.balance += inital_balance

    def show(self): 
        print(f"name: {self.username} \nbalance: {self.balance}") 
        # return f"name: {self.username} \nbalance: {self.balance}"

    def deposit(self, amount): 
        if amount >= 100:
            self.balance += amount
            print(f"{amount} deposit Successful! \ncurrent balance: {self.balance}") 
        else:
            print(f"at least deposit 100 or over")
    
    def withdrow(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{amount} withdrow Successful! \ncurrent balance: {self.balance}") 
        else:
            print(f"insufficient balance")

name = input("enter name: ") 
amount = int(input("enter amount: ")) 
user = Bank(name, amount) 
user.show() 
dpst = input("enter diposit amount: ") 
user.deposit(dpst) 
out = input("enter withdraw amount: ")
user.withdrow(out) 
