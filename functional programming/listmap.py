lst=[4,2,1,6,7,8]
#if number is less than 5 --> minus 1
#if number is greater than 1 --> plus 1
#output--> 3,1,0,7,8,9]

updatelist=[]
for i in lst:
    if (i<5):
        i-=1
        updatelist.append(i)
    else:
        i+=1
        updatelist.append(i)
print(updatelist)
#using lamda

result=list(map(lambda num:num-1 if num<5 else num+1,lst))
print(result)