import re
valid=[]
f=open("/home/user/PycharmProjects/luminarpythonProject/regular_expression/vehiclenum","r")
x='[a-zA-Z]{2}\d{2}[a-zA-z]{2}\d{4}'# x="[Kk][Ll]\d{2}[a-zA-Z]{2}\d{4}
for num in f:
    number=num.rstrip("\n")
    match = re.fullmatch(x,number)
    if match!=None:
        valid.append(number)
print(valid)

