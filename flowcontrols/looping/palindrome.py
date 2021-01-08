num=int(input("Enter a number:"))
res=0
while(num>0): #while(num!=0)
    digit=num%10
    res=res*10+digit
    num=num//10
print("res=",res)