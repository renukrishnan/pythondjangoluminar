class Stud:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name:",self.name)
        print("age:",self.age)
    def __str__(self):
        return self.name

f = open("/oop/demo_programs/student", "r")
for lines in f:
    data=lines.split(",")
    name=data[0]
    age=data[1]
    obj=Stud(name,age)
    print(obj)
    obj.printval()