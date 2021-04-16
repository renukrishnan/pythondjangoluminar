class Stud:
    def __init__(self,name,rollno,dept,mark):
        self.name=name
        self.rollno=rollno
        self.dept=dept
        self.mark=mark
    def printval(self):
        print("name:",self.name)
        print("rollno:",self.rollno)
        print("dept:", self.dept)
        print("mark:", self.mark)
    def __str__(self):
        return self.name
f = open("/home/user/PycharmProjects/luminarpythonProject/oop/demo_programs/work", "r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    rollno=data[1]
    dept=data[2]
    mark=int(data[3])
    #obj = Stud(name, rollno, dept, mark) -->this can be given here or inside if loop
    if(mark>=190):
        obj=Stud(name,rollno,dept,mark)
        print(obj)#this if to work__str__ method.
        obj.printval()