def myArguments(*args):
    return args
result = myArguments(45,78,98,5,6,8)

print("Touple: ",result) 


def myArguments2(**args): 
    return args
result2 = myArguments2(name="subrota", age=23, language="Bengali")

print("Object: ",result2)
