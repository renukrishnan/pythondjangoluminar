#how to use inheritance using constructor
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

    def printvalue(self):
        print("name:", self.name)
        print("age:", self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):# in derived class, we should add parent class variables or attributes here.
        super().__init__(name,age)# we should call super class constructor here by uising super()
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print(self.rollno)
        print(self.mark)
cr=Student(2,32,"anu",22)
cr.printvalue()
cr.print()
