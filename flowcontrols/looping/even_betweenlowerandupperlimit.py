
#read lower and upper limit
#print all even numbers between lower and upper limit

lower=int(input("Enter  lowerlimit:"))
upper=int(input("Enter  upperlimit:"))
while(lower<=upper):
    if(lower%2==0):
        print(lower)
    lower+=1