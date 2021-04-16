class Student:
    classteacher_name='renu'
    def m1(self,sub):
        self.sub=sub
        print("my name is", Student.classteacher_name)
        print("my subjcet:",self.sub)

class Stud(Student):
    def m2(self,cname):
        self.cname=cname
        print("class teacher :",Student.classteacher_name)
        print("subject:",self.sub)
        print("student name:",self.cname)

c=Stud()
c.m1("computer science")
c.m2("vedant")