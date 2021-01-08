name="luminar"
#ranimul
length=len(name)-1
while(length>=0):
    print(name[length],end="")
    length-=1


#another method
name = "luminar"
# ranimul
length = len(name) - 1
reverse=""
while (length >= 0):
    reverse+=name[length]
    length -= 1
print(reverse)

#len() has indexing from 1 where as array starts indexing from 0. thats y here length talen as len()-1
#array needs name [6] to store 7 length value called luminar.
#name[0] to name[6]= luminar