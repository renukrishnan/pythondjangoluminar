lst=[10,8,7,11,12,6,5]

#step 1,sort this list
#[5,6,7,8,10,11,12]
lst.sort()
flag=0
low=0
upper=len(lst)-1
element=int(input("enter element for search:"))
while(low<=upper): #0<6
    mid=(low+upper)//2 #mid=3
    if(element>lst[mid]):
        low=mid+1
    elif(element<lst[mid]):
        upper=mid-1
    elif(element==lst[mid]):
        flag+=1
        break
if flag==0:
    print("element not found")
else:
    print("element found")