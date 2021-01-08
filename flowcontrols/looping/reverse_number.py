#print reverse of a number

num=int(input("Enter a number:"))

while(num>0): #while(num!=0)
    digit=num%10
    print(digit,end="")#if we not give end,then it will take end as new line.
    num=num//10
