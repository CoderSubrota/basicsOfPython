numbers = [1,2,3,4,5,6]
# filter 
even_numbers = list(filter(lambda x : x%2 ==0, numbers))
print("Even numbers filter: ", even_numbers)


odd_numbers = list(filter(lambda x : x%2 ==1, numbers))
print("Odd numbers from filter: ",odd_numbers)

# map 
def multNumber(element):
    return element * 3

result = list(map(multNumber, numbers))

for num in result:
    print(num) 
    
# find 

myString = "Hello World"
textIndex = myString.find("World") 
print(textIndex)

