person = {"name":"Subrota", "age":23, "education":"Diploma IT", "profession":"Web developer"}

print(person["name"])
print(person["age"])
print(person["education"])
print(person["profession"])
print()

print("Before delete and update key\n")

for key,value in person.items():
    print("key: ", key, "value: ", value)
print()
    
person["name"]="David"

del person["profession"]

print()
print("After delete and update key\n")

for key,value in person.items():
    print("key: ", key, "value: ", value)
    