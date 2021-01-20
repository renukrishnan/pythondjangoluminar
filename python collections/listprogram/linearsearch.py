lst=[10,11,12,13,14,15]
element=int(input("enter element you want to search:"))
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

#to overcome drawbacks of linearsearch, binary search inroduced.

