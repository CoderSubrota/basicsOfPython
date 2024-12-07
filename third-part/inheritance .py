class Person:
    def __init__(self,name):
        self.name=name

class Person_Email(Person):
    def __init__(self, name,email):
        self.email = email
        super().__init__(name)
        
class Person_Country(Person_Email):
    def __init__(self, name, email,country):
        self.country=country
        super().__init__(name, email)
        
class Person_Gender(Person_Country):
     def __init__(self, name, email, country, gender):
         self.gender = gender
         super().__init__(name, email, country)
         
     def __repr__(self):
        return f"{self.name} {self.email} {self.country} {self.gender}"
    
person_class = Person_Gender("Subrota Chandra", "subrota788@gmail", "Bangladesh", "Male")

print(person_class)

