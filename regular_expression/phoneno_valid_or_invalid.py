import re
n=input("enter phonenumber:")
x='\d{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

# chech the phone number valid or not in the condition +91 (indian country code)
import re
n=input("enter phonenumber:")
x='^[+][9][1]\d{10}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")