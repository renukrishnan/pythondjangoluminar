#  *args and **kwargs

#*args is use to give n number of arguments in the form of tuple
def add(*args):
    sum=0
    for num in args:
        sum+=num
    return sum
res=add(10,20,30,40)
print(res)

#**kwargs takes value as dictionary format with key value
def print_person_details(**kwargs):
    print(kwargs)
print_person_details(name="ajay",birthplace="thrissur",wrkplace="kakkanad")


lst=[10,50,64,2,89,34]
s=sorted(lst,reverse=True)
print(s)


#employee program
employee={
    1000:{"name":"sajay","design":"pythontrainer","exp":3},
    1001:{"name":"aajay","design":"bigdata","exp":2},
    1002:{"name":"shibu","design":"java","exp":2}

}
eid=int(input("enter employee id:"))
if(eid in employee):
    print(employee[eid]["name"])
else:
    print(" eid is not exist")

#to print only name of emnployee when onlu eid is given in a function,using **kwargs
def emp_details(**kwargs):
    id=kwargs["eid"]
    prop=kwargs["prop"]
    if id in employee:
        print(employee[id]["name"])
        print(employee[id][prop]) # can also give as "design" as previous name one , but in that case only design will get next time if we want exp ,then we have to give prop.
    else:
        print(" eid is not exist")

emp_details(eid=1000,prop="design")