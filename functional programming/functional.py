#addTwonumbers()
#add_twonumber()


#
#add=Lambda num1,num2:num1+num2
#print(add(100,200))

sub=lambda num1,num2:num1-num2
print(sub(200,100))
#or
sub=lambda num1,num2:num1-num2
res=sub(200,100)
print(res)


cube=lambda num:num**3
print(cube(3))

#map()  --> if we have to do operations on all
#filter() --> if we have to get particular value from inputs as output,like print names starts with A
#reduce()

lst=[10,20,30,21,22,23,24]
def squ(no):
    return no**2
squares=list(map(squ,lst))#squares will be the new list
print(squares)

#map()--> it has 2 arguments
#1) which function using
#2) which iterable,here it is numbers in lst[]

#using lambda function
squares=list(map(lambda no:no**2,lst))#squares will be the new list
print(squares)

#program to find cubes
cubes=list(map(lambda no:no**3,lst))#list is used to convert map object into lit,cubes will be the new list
print(cubes)


#filter--> has 2 arguments
#1) function
#2) iterables
even=list(filter(lambda num:num%2==0,lst))
print(even)
lst=["akhil","aravind","varun","ram","akshay","vipin"]
anames=list(filter(lambda name:name[0]=='a',lst))
print(anames)


#reduce--> to perform sum , min,max
# reuce--> we have to importcoz it is not in builtins, it is in functools

from functools import reduce
lst=[10,20,30,50,80]
total=reduce(lambda no1,no2:no1+no2,lst)
print(total)
#to print hiohest num
max=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
print(max)
#to print lowest
min=reduce(lambda num1,num2:num1 if num1<num2 else num2,lst)
print(min)
