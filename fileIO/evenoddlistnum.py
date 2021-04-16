evenlst=[]
oddlst=[]
f=open("/home/user/PycharmProjects/luminarpythonProject/fileIO/numbers","r")
for num in f:
    if (int(num)%2==0):
        evenlst.append(int(num.rstrip("\n")))
    else:
        oddlst.append(int(num.rstrip("\n")))
print("even list is: ",evenlst)
print("odd list is: ",oddlst)
print("evenlist sum= ",sum(evenlst))
print("oddlist sum is:",sum(oddlst))