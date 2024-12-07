class Person:
    def __init__(self,name):
        self.name = name #public access modifier 

class Person_Email(Person):
    
    def __init__(self, name,email):
         self._email = email #protect access modifier 
         super().__init__(name)

class Person_Info(Person_Email):
    
     def __init__(self, name, email, bank_balance):
         self.__bank_balance=bank_balance #private access modifier 
         super().__init__(name, email)
          
     def get_bank_balance(self):
            return f"Your bank balance is: ${self.__bank_balance}"
        

person_info = Person_Info("Subrota", "subrota78@gmail.com",4456)

print("Name: ",person_info.name)
print("Email: ",person_info._email)
print(person_info.get_bank_balance())

# print(dir(Person_Info))


