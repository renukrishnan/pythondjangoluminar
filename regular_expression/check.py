#rule1-->either
import re
x="[abc]" # input should have either a,b or c
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())

#rule2-->except abc-->"[^abc]"
import re
x="[^abc]" # output should not read a,b or c
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())

#rule3--> small letter a to z-->  "[a-z]"
import re
x="[a-z]" # output should not read a,b or c
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())

#rule4--> capital letter A to Z-->  "[A-Z]"
import re
x="[A-Z]" # output should read A,B or C
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())

# rule5--> x='[a-zA-Z]' -->both lower and upper case are checked
import re
x="[a-zA-Z]" # output should read A,B or C and a,b or c
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())

# rule6--> x='[0-9]' -->check digits
import re
x="[0-9]" # output should read 0-9(any digits)
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())
#rule7--> x='[^a-zA-Z0-9]' --> special symbol--> ^ --> means not, so except alphabets and digits
import re
x="[^a-zA-Z0-9]"
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())
#rule8 -->to check space-->"\s"
import re
x="\s"
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())
#rule9--> x='\d' check the digits
import re
x="\d"
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())
#rule10--># x='\D' except digits
import re
x="\D"
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())
#rule11--> x='\w' all words except special characters
import re
x="\w"
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())
#rule12--> x='\W' for special characters
import re
x="\W"
matcher=re.finditer(x,'abt c@5kz')
for match in matcher:
    print("match available at ",match.start())
    print("group", match.group())