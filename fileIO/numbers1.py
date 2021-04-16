lst=[]
f=open("numbers","r")
for num in f:
    lst.append(int(num.rstrip("\n")))#list value read as string value, to get it into integer we use int()
print(lst)
print(sum(lst))
