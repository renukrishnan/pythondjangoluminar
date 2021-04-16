f=open("movies.csv","r")
dict={}
for lines in f:
    data=lines.split(",")
    #print(data)
    year=data[2]
    if year not in dict:
       dict[year]=1
    else:
        dict[year]+=1
for k,v in dict.items():
    print(k,"=======>",v)
result=sorted(dict,key=dict.get,reverse=True)
print("highest no. of movies released in the year",result[0],"=====>",dict.get(result[0]))