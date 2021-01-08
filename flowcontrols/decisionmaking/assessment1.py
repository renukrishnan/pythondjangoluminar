#read two numbers
# print true if sum of two numbers is equal to 100 or anyone num is 100
#else print false

num1=int(input("Enter num1:"))
num2=int(input("enter num2:"))
if((num1+num2==100)|(num1==100)|(num2==100)):
    print(" True")
else:
    print("false")