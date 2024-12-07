
number=0
# first case 
try:
    num=55/"dfdf"
    number= num 
except:
    print("You have an error !!")
finally:
    print("This is finally")
    
# second case 

try: 
    num = 45/"20"
# except:
#     print("You have an error!!") 
finally:
    print("This is finally !!")
    
# third case 
number2=0
try:
    num = 121/24
    number2=num
except:
    print("You have an error !!")
    
finally:
    print(number2)
    
# forth case 
try:
    num = 120*3
    number2=num
finally:
    print(number2)
    
    
    