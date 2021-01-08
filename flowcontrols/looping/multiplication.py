#print multiplication table of any number

num=int(input("Enter a num:"))
limit=int(input("Enter the limit:"))
i=1
while(i<=limit):
    mul=i*num
    print(i,"*",num,"=",mul)
    i+=1