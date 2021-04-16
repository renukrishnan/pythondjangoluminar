#word count program by opening data file
f=open("data","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(" ")
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
for k,v in dict.items():
    print(k,":",v)