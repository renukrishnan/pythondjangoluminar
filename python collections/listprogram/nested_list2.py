lst=[[10,20],[21,22],[51,52],[53,54,55,56]]
#output should be [10,12,21,22,51,52,53,54,55,56]
numlist=[]
for no in lst:# no=[10,20]
    for n in no:# n=10
        numlist.append(n)
print(numlist)
