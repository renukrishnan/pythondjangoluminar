import re
n=input("enter your mail id:")
x='^[a-zA-Z0-9_-.+]+[@]+[a-zA-Z]+[.]+[a-zA-Z]+$' #[a-zA-Z0-9_-+.]+  --> + indicates the rule a+ in quantifiers, means including group
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")