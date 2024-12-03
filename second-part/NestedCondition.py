
num = int(input())

if num > 10:
    if num%2==0:
        print("Even number", num)
else:
    print("Number is less then 10")
# get multiple Input from user   
multipleInput = input().split()
a = [int(num) for num in multipleInput]
print(a)
