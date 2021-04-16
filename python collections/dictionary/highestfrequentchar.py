pattern="ABABBACEEEEEEEEEE"
#find the highest frequent character, here it is E( no of E is highest here)
dict={}
for ch in pattern:# A B A ..
    if ch not in dict:# a is not in dict then increment value
        dict[ch]=1
    else:
        dict[ch]+=1
for key,value in dict.items():
   print(key,",",value)
#print(dict.get("E"))# will get the value of key E , result is 10
result=sorted(dict,key=dict.get,reverse=True)
print("highest frequent character is",result[0])
