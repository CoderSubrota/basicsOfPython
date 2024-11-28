array = [45,89,[12,65],False,23,"Subrota"]

print(type(array))

size = len(array)

print("Size: ", size)

array.append("Chandra")
array.insert(3,"Bangladesh")
array.remove(45)
array.pop()
array.clear()

for num in array:
        print (num) 



