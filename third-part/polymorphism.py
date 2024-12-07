from math import pi

class Shape:
    def __init__(self,name):
             self.name = name 
         
    def area(self):
       pass

class Rectangle(Shape):
     def __init__(self, name):
          super().__init__(name)
         
     def area(self, height, width):
        return height * width 
    
class Circle(Shape):
    def __init__(self, name):
         super().__init__(name)
         
    def area(self, radius):
        return pi * radius * radius

class Triangle(Shape):
    def __init__(self, name):
         super().__init__(name)
         
    def area(self, x, y):
        return 1/5*(x*y)


rec = Rectangle("Rectangle")
print(rec.name ,"area: ", rec.area(10,7))

cir = Circle("Circle")
print(cir.name, "area: ", cir.area(12))

tri = Triangle("Triangle")
print(tri.name, "area", tri.area(20,20))

