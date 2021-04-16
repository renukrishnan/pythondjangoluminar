#pattern matching
#re  --package for pattern matching

import re
count=0
matcher=re.finditer('ab','abbbabbbab')
for match in matcher:
    count+=1
print("count=",count)

# match.start() and match.group() program

import re
count=0
matcher=re.finditer('ab','abbbabbbab')
for match in matcher:
    print("match available at ",match.start())  # match.start() returns matchinmg start position
    print("group", match.group())  # match.group() gives the object which we are matching...which object finds match
    count+=1
print("count=",count)