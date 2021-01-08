#read a number
#read upperlimit
#read lowerlimit
#calculate 1**num,and check whether it lies between upper and lower,if then print that number

num=int(input("Enter number:"))
lower=int(input("Enter lower limit:"))
upper=int(input("Enter upper limit:"))
for i in range(1,upper):
    res=i**num
    if((res>=lower)&(res<=upper)):
        print(i)
