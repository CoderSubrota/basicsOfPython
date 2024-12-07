class Representation:
    
      def __init__(self,name,email,country):
            self.name = name
            self.email=email
            self.country = country
            
      def __repr__(self):
            return f"{self.name} {self.email} {self.country}"
        
repre_class = Representation("Subrota","subrota7@gmail.com","Bangladesh")

print("without representation: ", repre_class.name, repre_class.email, repre_class.country)

print("with representation: " , repre_class)
