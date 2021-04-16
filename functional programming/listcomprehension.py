lst=[1,2,3,4,5,6]
lst2=[10,20]
# to get squiares of each num
squares=[num**2 for num in lst]
print(squares)
# to get even numbers
even=[num for num in lst if num%2==0]
print(even)


# pairs program
#(1,10)(1,20)(2,10)(2,20).....

pairs=[(i,j) for i in lst for j in lst2]
print(pairs)