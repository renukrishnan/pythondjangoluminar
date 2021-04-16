#a=[1,2,3]
#print(a[2])#print(a[7])--> indexbound
lst=[1,2,3]
try:
    i=int(input("index"))
    print(lst[i])
except Exception as e:
    print("exception")

