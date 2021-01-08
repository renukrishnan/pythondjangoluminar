#1
#12
#123
#1234

for row in range(1,5):
    for col in range(1,row+1):
        print(col,"\t",end="")
    print()


#another method

for row in range(1,5):
    for col in range(0,row):
        print(col+1,"\t",end="")
    print()