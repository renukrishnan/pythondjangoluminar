#
num=input("enter number:")#taking input as string
i=1
data=0
pattern=""
while(i<=int(num)):#coverting num to integer only to check condition,then again it will be back to string
    res=num*i
    pattern=pattern+"+"+res
    data+=int(res)
    i+=1
pattern=pattern.lstrip("+")
print(pattern)
print("=",data)
