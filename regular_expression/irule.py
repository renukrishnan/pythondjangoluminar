import re
n="helloo"# if i give 7 letters in n as input output will be invalid
x='\w{6}' # means words of 6 no. of letter
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")

# create a rule for n="56kg"
import re
n="56kg"
x='\d{2}[a-z]{2}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")