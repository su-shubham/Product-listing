def add(num1:int,num2:int):
    return num1+num2

def subtract(num1:int,num2:int):
    return num1-num2

def multiply(num1:int,num2:int):
    return num1*num2

def divide(num1:int,num2:int):
    return num1/num2

class BankAccount():
    def __init__(self,statring_balance=0):
        self.balance=statring_balance

    def deposit_balance(self,amount):
        self.balance += amount
    
    def withdraw_balance(self,amount):
        self.balance -=amount
    
    def interest(self):
        self.balance *=1.1

        
