num = int(input())
print(num , " X ", num , "Matrix\n")
for i in range(num): #row
    for j in range(num): #column
        print(f"{i}{j} |", end=" ")
    print()