#check all numbers lies between is prime or not
#prime can only have two factors(it wii be divisle by 1 and that number only). 15 is not a prime coz it have more than two factors.

low=int(input("Enter lowelimit:"))
upper=int(input("Enter upperlimit:"))
flag=0
if(low==1):
    print("not prime")
else:
    for i in range(low,(upper+1)):
        for j in range(2,i):
            if(i%j==0):
                flag=flag+1
                break
            else:
                flag=0
        if(flag==0):
            print(i)
