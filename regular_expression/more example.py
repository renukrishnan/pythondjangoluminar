#to check a word is valid or not by using the condition:
#     combination of upper and lower case letters ending with a number

import re
n=input("enter a word:")
x="([a-zA-Z]+\d{1}$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

#check a string,starting with a and ending with b
import re
n=input("enter a word:")
x="(^a[a-zA-Z0-9\W]*b$)"
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")