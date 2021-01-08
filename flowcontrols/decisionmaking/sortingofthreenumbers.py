num1=int(input("enter num1"))
num2=int(input("enter num2"))
num3=int(input("enter num3"))
if((num1>num2)&(num1>num3)):
    if(num2>num3):
        print("after sorting:",num1,num2,num3)
    else:
        print("after sorting:",num1,num3,num2)
elif((num2>num1)&(num2>num3)):
    if(num1>num3):
        print("after sorting:",num2,num1,num3)
    else:
        print("after sorting:",num2,num3,num1)
elif((num3>num1)&(num3>num2)):
    if (num2>num1):
        print("after sorting:",num3,num2,num1)
    else:
        print("after sorting:",num3,num1,num2)