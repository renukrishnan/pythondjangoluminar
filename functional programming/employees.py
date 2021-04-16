class Employee:
    def __init__(this,eid,ename,desig,salary):#instead of self we can use this also
        this.eid=eid
        this.ename=ename
        this.desig=desig
        this.salary=salary

    def print_emp(self):
        print(self.ename)

e1=Employee(1000,"varun","developer",25000)
e2=Employee(1000,"vivek","QA",26000)
e3=Employee(1000,"vedant","developer",50000)
e4=Employee(1000,"vidhya","marketing",20000)
employee=[]
employee.append(e1)
employee.append(e2)
employee.append(e3)
employee.append(e4)
sal=[]
for emp in employee:
    sal.append(emp.salary)
print(sal)



# using map function
class Employee:
    def __init__(this,eid,ename,desig,salary):#instead of self we can use this also
        this.eid=eid
        this.ename=ename
        this.desig=desig
        this.salary=salary

    def print_emp(self):
        print(self.ename)

e1=Employee(1000,"varun","developer",25000)
e2=Employee(1000,"vivek","QA",26000)
e3=Employee(1000,"vedant","developer",50000)
e4=Employee(1000,"vidhya","marketing",20000)
employee=[]
employee.append(e1)
employee.append(e2)
employee.append(e3)
employee.append(e4)
salary=list(map(lambda emp:emp.salary,employee))
print(salary)

#to print highest salary
class Employee:
    def __init__(this,eid,ename,desig,salary):#instead of self we can use this also
        this.eid=eid
        this.ename=ename
        this.desig=desig
        this.salary=salary

    def print_emp(self):
        print(self.ename)

e1=Employee(1000,"varun","developer",25000)
e2=Employee(1000,"vivek","QA",26000)
e3=Employee(1000,"vedant","developer",50000)
e4=Employee(1000,"vidhya","marketing",20000)
employee=[]
employee.append(e1)
employee.append(e2)
employee.append(e3)
employee.append(e4)
salary=max(list(map(lambda emp:emp.salary,employee)))
print(salary)