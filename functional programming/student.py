class Student:
    def __init__(self,rollno,name,course,total):
        self.rollno=rollno
        self.name=name
        self.course=course
        self.total=total
    def __str__(self):
        return self.name
s1=Student(101,"renu","BBA",250)
s2=Student(102,"vedant","MBA",300)
s3=Student(103,"sanoj","MCA",270)
studentlist=[]
studentlist.append(s1)
studentlist.append(s2)
studentlist.append(s3)
studenttotal=list(map(lambda stud:stud.total,studentlist))
print(studenttotal)
#to find highest total
studenttotal=max(list(map(lambda stud:stud.total,studentlist)))
print(studenttotal)