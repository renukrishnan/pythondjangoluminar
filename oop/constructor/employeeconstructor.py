class Employee:
    compname="TCS"
    def __init__(self,id,name,dept,salary):
        self.id=id
        self.name=name
        self.dept=dept
        self.salary=salary
    def printvalue(self):
        print("id:",self.id)
        print("name:", self.name)
        print("dept:", self.dept)
        print("salary:", self.salary)
        print("companyname:",Employee.compname)
obj=Employee(101,"renu","Developer",50000)
obj.printvalue()