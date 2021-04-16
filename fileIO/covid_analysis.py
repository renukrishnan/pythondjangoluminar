f=open("covid_19_india.csv","r")
dict={}
for lines in f:
    data=lines.rstrip("\n").split(",")
    #print(data)
    #want only state , confirmed cases
    state=data[3].rstrip("***")
    if(state=="Telengana"):
        state="Telangana"
    confirmed_cases=int(data[8])
    if state not in dict:
        dict[state]=confirmed_cases #confirmed case value gets from that dataset
    else:
        dict[state]=confirmed_cases
for k,v in dict.items():
    print(k,"=======>",v)
result=sorted(dict,key=dict.get,reverse=True)
print("highest cases is in",result[0],dict.get(result[0]))

#to print states in alphabetical order, sorted(dict)