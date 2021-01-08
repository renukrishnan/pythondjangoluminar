num1=int(input("enter first number,num1= "))
num2=int(input("enter second number,num2= "))

#temp=num1
#num1=num2
#num2=temp
#print("after swapping, num1=",num1, "num2=",num2)

#without using temp variable

num1=num1+num2
num2=num1-num2
num1=num1-num2
print(num1)
print(num2)