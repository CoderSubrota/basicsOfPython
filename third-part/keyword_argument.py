def key_args(**keyargs):
     return keyargs 

key_result = key_args(name="Subrota", age=23, education="Diploma IT")

print(key_result.get("name"))
print(key_result.get("age"))
print(key_result.get("education"))
