#rule1--> x='a+'  a including group
import re
x="a+"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
   print("match available at ",match.start())
   print("group", match.group())
#rule2-->  x='a*' count including zero number of a
import re
x="a*"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#rule3--> x='a?' count a as each including zero no of a
import re
x="a?"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#rule4--> x='a{2}' 2 no of a's position
import re
x="a{2}"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#rule5--> x='a{2,3}' minimum 2 a and maximum 3 a
import re
x="a{2,3}"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#rule6--> x='^a'  check position starting with a
import re
x="^a"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())
#rule7--> x='a$' check position ending with a
import re
x="a$"
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())