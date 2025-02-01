#!/bin/python3

class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    
    def debit(self, amount):
        self.balance -= amount
        print("Tk.", amount, "was debited from your account.")

    def credit(self, amount):
        self.balance += amount
        print("Tk.", amount, "was credited to your account.")

    def display(self):
        return self.balance
    
#creating object of class Account
acc1 = Account(10500, 23310728506)
acc1.debit(1500)
acc1.credit(2000)
print("Your account balance is:", acc1.display())