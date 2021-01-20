limit=int(input("Enter limit:"))
#lst=[2,5,6,7]
lst=list()
for i in range(0,limit):
    number=input("enter values for list:")
    lst.append(number)
element=input("enter element you want to search:")
flag=0
count=0
for num in lst:
    if(element==num):
        flag+=1
        break
    else:
        pass
    count+=1
if flag==0:
    print("element not found")
else:
    print(" elememt found at",count,"position")