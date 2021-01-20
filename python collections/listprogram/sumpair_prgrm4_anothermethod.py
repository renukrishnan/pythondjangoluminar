lst=[1,2,3,5]
low=0
upp=len(lst)-1
element=int(input("enter element:"))
while(low<upp):
    tot=lst[low]+lst[upp]
    if(element==tot):
        print(lst[low],lst[upp])
        break
    elif(element>tot):
        low+=1
    else:
        upp-=1