#list[2,6,4] , output shoulb be list[10,6,8]--> 0th position=6+4, 1st position=2+4, 2nd position=2+6
#list[3,4,5] , output should be list[9,8,7]--> 0th position=4+5, 1st position=3+5, 2nd position=3+4
#total of list values=sum()
#20
#20-2=18
#20-5=15
#20-6=14
#20-7=13
limit=int(input("Enter limit:"))
#lst=[2,5,6,7]
lst=list()
for i in range(0,limit):
    number=int(input("enter values for list:"))
    lst.append(number)
out=list()
total=sum(lst)
for num in lst:
    out.append(total-num)
print(out)