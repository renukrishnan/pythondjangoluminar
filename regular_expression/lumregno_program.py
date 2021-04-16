import re
f2=open("lumregno2","w")# ("lumregno","a") can also use this method. "a" represents append, means will create a new file and write the data.
f=open("/home/user/PycharmProjects/luminarpythonProject/regular_expression/lumregno","r")
x="([A-Z]{3}\d{2}[P][Y]\d{3}$)"# x="[L][U][M]\d{2}[P][Y]\d{4}
for num in f:
    number=num.rstrip("\n")
    match = re.fullmatch(x,number)
    if match!=None:
        f2.write(number)
        f2.write("\n")


