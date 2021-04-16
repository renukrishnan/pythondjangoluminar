class Employee:
    compname="tcs"
    def setVal(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print("id:",self.id)
        print("name:", self.name)
        print("dept:", self.dept)
        print("salary:", self.salary)
        print("company name=",Employee.compname)
obj=Employee()
obj.setVal(101,"renu","Developer",50000)
obj.printvalue()
emp1=Employee()
emp1.setVal(102,"vedant","designer",100000)
emp1.printvalue()