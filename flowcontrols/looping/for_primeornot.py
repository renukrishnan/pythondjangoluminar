#check given number is prime or not
#prime can only have two factors(it wii be divisle by 1 and that number only). 15 is not a prime coz it have more than two factors.
num=int(input("enter number:"))
flag=0
if(num==1):
    print("not prime")
else:
    for i in range(2,num):
        if(num%i==0):
            flag=flag+1
        break
    else:
        flag=0

    if flag==0:
        print("prime")
    else:
        print("not prime")
