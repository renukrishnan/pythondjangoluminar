#print() to print message in console
#input()
#len()
#l.strip()
#r.strip()
#split()
#type()
#functions are used to perform a particular task.
#function calls by functionname() or function_name(argmnts,argmnts,....)

#how to create function:
# 2 ways
# def functionname(parameter,parameter,..):
    #function definition
#function_name()
#lamda function is the latest version of using functions, it will take later

#function with parameters and no return value(only printing result)
def add(num1,num2):#parameters
    res=num1+num2
    print(res)
add(10,20)#arguments

#function with parameters and return value
def sub(num1,num2):
    res=num1-num2
    return res
data=sub(20,10)
print(data)

