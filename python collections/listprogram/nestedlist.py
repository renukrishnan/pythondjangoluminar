students=[
    [10,"ajay","bca",250],
    [11,"vijay","bca",280],
    [12,"sanoj","bca",240],
    [13,"vedant","bca",210],
    [14,"tom","mca",180],
    [15,"renu","mca",250]
]
print(students)
print(students[0])#will print only first list ie, [10,"ajay","bca",250]
print(students[0][0])# will print only the first value of first list ie, 10

#students name only
#for stud in students:
  #  print(stud[1])

#print student names whose total >240
#for stud in students:
   # if(stud[3]>240):
    #    print(stud[1])

#print total sum of total
sum=0
for stud in students:
    sum=sum+stud[3]
print("sum of total=", sum)

# calculate total of bca and mca separately
btotal=0
mtotal=0
for stud in students:
    if(stud[2]=="bca"):
        btotal=btotal+stud[3]
    else:
        mtotal=mtotal+stud[3]
print("BCA total=",btotal)
print("MCA total=", mtotal)



