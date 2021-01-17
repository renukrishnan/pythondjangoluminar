lst=[10,11,12,13,14,15,16,17]
#even numbers --> evenlist
#odd numbers --> oddlist
#find total of evenlist,oddlist
evensum=0
oddsum=0
evenlst=list()
oddlst=list()
for num in lst:
    if num%2==0:
        evenlst.append(num)
    else:
        oddlst.append(num)
print(oddlst)
print(evenlst)
print("oddsum=",sum(oddlst))
print("evensum=",sum(evenlst))
