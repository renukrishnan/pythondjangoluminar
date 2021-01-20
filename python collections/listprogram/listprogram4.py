#list=[1,2,3,4,5], give input as 6 then output should be all the list pair whose sum will be the input(4,2) (5,1)
#input=7,then output should be (4,3) (5,2)

lst=[1,2,3,4,5]
num=int(input("enter a number to find pairs:"))
for i in range(0,len(lst)):
    for j in range(i+1,len(lst)):
        if(lst[i]+lst[j]==num):
            print(lst[i],lst[j])
