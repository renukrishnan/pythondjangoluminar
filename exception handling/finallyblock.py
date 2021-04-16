#finally block will run for sure ...both try or exception cases.
lst=[18,4,5]
a=int(input("enter index"))
try:
    print(lst[a])
except:
    print("exception")
finally:
    print("inside finally")