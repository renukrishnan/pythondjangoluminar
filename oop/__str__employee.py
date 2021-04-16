class Employee:
    compname="tcs"
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
        print("company name=",Employee.compname)
    def __str__(self):
        return str(self.id)
obj=Employee(101,"renu","Developer",50000)
print(obj)
emp1=Employee(102,"vedant","designer",100000)
print(emp1)

