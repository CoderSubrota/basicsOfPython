from abc import ABC, abstractmethod

class Bank_Account(ABC):
     def __init__(self,bank_holder,balance):
           self.bank_holder = bank_holder
           self.balance=balance
           
     @abstractmethod
     def deposit(self,amount):
         pass
     
     @abstractmethod 
     def withdraw(self,amount):
         pass
     
class Saving_Account(Bank_Account):
    
    def deposit(self, amount):
          if amount < 10 or amount > 25000:
              print("Amount is not valid enter amount between 10 to 25000 for deposit")
          else:
              self.balance +=amount
              
    def withdraw(self, amount):
     if amount < 10 or amount > 25000:
              print("Amount is not valid enter amount between 10 to 25000 for withdraw")
     else:
         self.balance -= amount
         
    def __repr__(self):
         print()
         return f"Welcome {self.bank_holder} your current balance is: ${self.balance}"
     
bank_class = Saving_Account("Subrota Chandra",10)

bank_class.deposit(5400)
bank_class.withdraw(2000)

print(bank_class)
        